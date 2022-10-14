import os
import scratchpad.stitch_utils as utils
import numpy as np
import cv2
from tqdm import tqdm

# Setup Paths
input_path = '/media/leon/Terrebonne_2021_part1_8TB/Terrebonne_2021_part1_8TB/Rashik/test-terrebonne360_antenna-calib/1/zone/2022.05.31/2'
output_path = '/media/leon/Terrebonne_2021_part1_8TB/Terrebonne_2021_part1_8TB/Rashik/test-terrebonne360_antenna-calib_out_with14/1/zone/2022.05.31/2'

def get_sequence_number(poses_file_path):
    with open(poses_file_path, 'r') as f:
        seq_list = [line.split(None, 1)[0] for line in f]
        seq_list = seq_list[4:]
    return seq_list

# Get Data Length
images = os.listdir(input_path+'/08')
data_length = len(images)
print("Total data: ", data_length) #3299

# Other Setups
trig_start = 2000
trig_end = data_length

print("Section: ", trig_start, " to ", trig_end)

cam_seq = ['08', '12', '11', '10', '13', '09', '08']
# cam_seq = ['09', '10', '11', '12', '13', '08', '09']
angle = [0, 1.2373, 2.203, 2.9077, 3.3411, 4.2181, 3.2181]
y_shift = [0, 39, -54, -216, -420, -635, -938]
x_start = [0, 3951, 7920, 11818, 15785, 19811, 23911]

scale = 0
h = 3008
w = 4112
mask = np.ones(((h, w,3))).astype(np.float32)
rot_axis = utils.get_rot_axis(h, w, scale)
panaroma = np.zeros((h+int(2*scale*h), int(w*7), 3)).astype(np.float32)
# print("Panaroma Shape= ")
# print(panaroma.shape)

# Get the input and output paths
def get_io_paths(input_dir, output_dir, cam_seq, image):
    ip_paths = []
    for c in cam_seq:
        ip_paths.append(input_dir+'/'+c+'/'+image)

    op_paths = []
    op_paths.append(output_dir+'/360/'+image)
    op_paths.append(output_dir+'/360low/'+image)

    return ip_paths, op_paths

# Start Stitching
# For each trigger
for j in tqdm(range(trig_start, trig_end)):
    # print("Trigger no: ", j)
    error = 0

    # Get input and output images path
    ip_paths, op_paths = get_io_paths(input_path, output_path, cam_seq, images[j])

    # Create Panaroma
    # For each of 7 images
    for i in range(7):
        # print("Loop: ", i)
        # Break the loop if image doesn't exist
        if not os.path.exists(ip_paths[i]):
            print("error: ", ip_paths[i], "doesn't exist!")
            error = 1
            break

        # Read image
        img = cv2.imread(ip_paths[i]).astype(np.float32)/255.
        # print(img.shape)

        # Rotate and y-shift both image and mask
        img_final, mask_final = utils.rotate_and_shift(img,
                                                   mask,
                                                   -angle[i],
                                                   rot_axis,
                                                   -y_shift[i])

        # Add image to panaroma
        start = x_start[i]
        end = start+w+int(2*scale*w)
        to_replace = panaroma[:, start:end, :]

        # print('start: ', start, 'end: ', end)
        # print(to_replace.shape , "and", mask_final.shape)

        bg = np.multiply(to_replace, 1-mask_final)
        replace_by = np.add(bg, img_final)
        panaroma[:, start:end, :] = replace_by

    if error:
        continue 

    # Prepare the output image
    output = np.copy(panaroma)
    output *= 255.
    # output = output.astype(np.uint8)[50:-50, :19874, :]
    output = output.astype(np.uint8)[:, :27784, :]

    # Save Low Quality (20% compression)
    cv2.imwrite(op_paths[1], output, [int(cv2.IMWRITE_JPEG_QUALITY), 20])

    # Save High Quality (75% compression)
    cv2.imwrite(op_paths[0], output, [int(cv2.IMWRITE_JPEG_QUALITY), 75])

    # input()