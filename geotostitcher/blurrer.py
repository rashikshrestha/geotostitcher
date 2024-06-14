import cv2
import sys
from pathlib import Path
import pickle
import shutil

def blur_multiple_squares(image, regions):
    """
    Blurs multiple square regions within an image.

    Parameters
    ----------
    image: np.array
        The input image as a NumPy array.
    regions: np.array
        (N, 4)
        [[top_left_x, top_left_y, bottom_right_x, bottom_right_y], ...]
        
    Returns
    -------
    blurred: np.array
        Blurred image
    """
    blurred_image = image.copy()


    for region in regions:
        try:
            top_left_x = int(region[0])
            top_left_y = int(region[1])
            bottom_right_x = int(region[2])
            bottom_right_y = int(region[3])

            square = blurred_image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
            blurred_square = cv2.blur(square, (128,128))
            blurred_image[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = blurred_square
        except:
            print(f"Region: {region} couldn't be blurred!")

    return blurred_image

if __name__=='__main__':
    image_path = sys.argv[1]
    
    #! Blur pkl file
    splits = image_path.split('/')
    rec = splits[-3]
    cam = splits[-2]
    filename = splits[-1].split('.')[1] + '.pkl'
    pkl_path_splits = splits[:-4] + ['intermediate/blur/'] + [rec] + [cam] + [filename]
    pkl_path = Path('/'.join(pkl_path_splits))
    
    #! Output image path
    out_splits = splits[:-2] + [cam+'_blur'] + [splits[-1]]
    out_image_path = '/'.join(out_splits)

    #! Pathlib
    if pkl_path.exists():
        with open(pkl_path, 'rb') as f:
            blur_regions = pickle.load(f)
            image = cv2.imread(image_path)
            blurred_image = blur_multiple_squares(image, blur_regions)
            cv2.imwrite(out_image_path, blurred_image)
    else:
        shutil.copy(image_path, out_image_path)