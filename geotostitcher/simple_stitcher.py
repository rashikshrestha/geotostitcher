import os
import sys
import numpy as np
import cv2
import yaml


def get_io_images_path(output_dir, rec, seq, cam_seq):
    """
    Get the path of input and output images in the the given camera order

    Parameters
    ----------
    output_dir: str
        Output directory
    rec: str
        Recording number
    seq: str
        Sequence number
    cam_seq: list
        Sequence of cameras

    Returns
    -------
    ip_paths: list
        List of input images path in sequence of given camera order
    op_paths: str
        Path of output panaroma image 
    """
    ip_paths = []
    for c in cam_seq:
        ip_paths.append(f"{output_dir}/images/{rec}/{c}/image.{seq}.jpg") 

    op_path = f"{output_dir}/images/{rec}/360/image.{seq}.jpg"

    return ip_paths, op_path


def get_rot_axis(h,w,scale):
    rot_axis_x = scale*w
    rot_axis_y = scale*h + h
    return (rot_axis_x, rot_axis_y)


def rotate_and_shift(image, mask, angle, axis, shift):
    rot_mat = cv2.getRotationMatrix2D(axis, angle, 1.0)
    rot_mat[:,2] += np.array([0,shift]) 

    rot_image = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    rot_mask = cv2.warpAffine(mask, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return rot_image, rot_mask


def read_cfg(config_file):
    """
    Read config file
    """
    with open(config_file) as f:
        data = yaml.load(f, Loader=yaml.loader.SafeLoader)
    return data


def stitch(ip_paths, op_path, cfg):
    """
    Stitch images to create panaroma
    """

    #! Get some configs
    h = cfg['h']
    w = cfg['w']
    scale = cfg['scale']
    angle = cfg['angle']
    x_start = cfg['x_start']
    y_shift = cfg['y_shift']

    #! Some one time tasks
    mask = np.ones(((h, w, 3))).astype(np.float32)
    rot_axis = get_rot_axis(h, w, scale)
    panaroma = np.zeros((h+int(2*scale*h), int(x_start[-1]+w), 3)).astype(np.float32)

    no_of_cams = len(cfg['cam_seq'])
    error = 0
    for i in range(no_of_cams):
        # print("Loop: ", i)
        #! Break the loop if image doesn't exist
        if not os.path.exists(ip_paths[i]):
            print("Error: ", ip_paths[i], "doesn't exist!")
            error = 1
            break

        # Read image
        img = cv2.imread(ip_paths[i]).astype(np.float32)/255.
        # print(img.shape)

        # Rotate and y-shift both image and mask
        img_final, mask_final = rotate_and_shift(img,
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
        print("Failed to create panaroma!")
        return 0 

    # Prepare the output image
    output = np.copy(panaroma)
    output *= 255.
    # output = output.astype(np.uint8)[50:-50, :19874, :]
    output = output.astype(np.uint8)[:, :27784, :]

    # Save Low Quality (20% compression)
    cv2.imwrite(op_path, output, [int(cv2.IMWRITE_JPEG_QUALITY), cfg['quality']])

    return 1

if __name__=='__main__':

    #! Example Input arguments
    # output_dir = '/home/rashik/workspace/geoautomation/mrcsource-pave-out'
    # rec = '101'
    # seq = '101000000'
    # cfg_file = '/home/rashik/workspace/geoautomation/geotostitcher/scripts/stitch_config.yaml'

    #! Check the input arguments
    if len(sys.argv) != 5:
        print('Usage: python3 simple_stitcher.py output_dir rec seq config_file')
        sys.exit()

    #! Get Input Args
    output_dir = sys.argv[1] 
    rec = sys.argv[2] 
    seq = sys.argv[3] 
    cfg_file = sys.argv[4] 

    #! Stitch
    cfg = read_cfg(cfg_file)
    ip_paths, op_path = get_io_images_path(output_dir, rec, seq, cfg['cam_seq'])
    done = stitch(ip_paths, op_path, cfg)

