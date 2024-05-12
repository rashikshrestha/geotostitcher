import cv2
from pathlib import Path
import sys
import math
import numpy as np

def tileit(image_path: str):
    #! Configuration
    tile_height, tile_width = 2724, 2724
    vtiles, htiles = 2, 8
    all_black_row_top = 1
    all_black_row_bottom = 1
   
    #! Rest of the code 
    expected_img_height = tile_height*vtiles
    
    image_path_split = image_path.split('/')
    tiles_dir = '/'.join(image_path_split[:-2]) + '/360tiles'

    # Create tiles dir if doesn't exixts
    Path(tiles_dir).mkdir(parents=True, exist_ok=True)
    # Read the image
    img = cv2.imread(image_path)
    img_name = image_path_split[-1]

    # Check if image loaded successfully
    if img is None:
        print("Error: Could not load image.")
        exit(1)

    # Crop top and bottom of image
    img_height, img_width = img.shape[0], img.shape[1]

    if tile_width*htiles != img_width:
        print(f"Error: this image width {img_width} doesn't fit the {htiles} tiles of width {tile_width}")
        print("Exiting...")
        exit(1)
    
    if img_height < expected_img_height:
        pad_height = (expected_img_height-img_height)/2
        
        if pad_height.is_integer():
            top_pad_height = pad_height
            bottom_pad_height = pad_height
        else:
            top_pad_height = math.floor(pad_height)
            bottom_pad_height = math.ceil(pad_height)
            
        pad_width = img_width
        
        top_pad = np.zeros((top_pad_height, pad_width,3))    
        bottom_pad = np.zeros((bottom_pad_height, pad_width,3))    
        
        img = np.vstack((top_pad, img, bottom_pad))
        
    elif img_height > expected_img_height:
        crop_height = (img_height-expected_img_height)/2
        
        if crop_height.is_integer():
            top_crop_height = crop_height
            bottom_crop_height = crop_height
        else:
            top_crop_height = math.ceil(crop_height)
            bottom_crop_height = math.floor(crop_height)
            
        img = img[top_crop_height:bottom_crop_height,:,:]
        
    else:
        ...
        
    # Initialize counter for tile naming
    tile_count = all_black_row_top*htiles

    # Iterate through rows and columns to extract tiles
    for row in range(vtiles):
        for col in range(htiles):
            # Define top-left corner coordinates for current tile
            y_start = row * tile_height
            x_start = col * tile_width

            # Extract the tile
            tile = img[y_start:y_start + tile_height, x_start:x_start + tile_width]

            # Save the tile
            # tile_name = f"tile_{tile_count}.jpg"
            tile_name = f"{tiles_dir}/{img_name[:-4]}_{tile_count}.jpg"
            cv2.imwrite(tile_name, tile, [int(cv2.IMWRITE_JPEG_QUALITY), 75])

            # print(f"Saved tile: {tile_name}")

            tile_count += 1
            
    print(image_path)


if __name__=='__main__':
    tileit(sys.argv[1])