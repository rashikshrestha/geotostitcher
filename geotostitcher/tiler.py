import cv2
from pathlib import Path
import sys

def tileit(image_path: str):
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
    crop = 284
    img = img[crop:-crop,:,:]

    # Calculate tile dimensions
    tile_height = img.shape[0] // 2
    tile_width = img.shape[1] // 12

    # Initialize counter for tile naming
    tile_count = 24

    # Iterate through rows and columns to extract tiles
    for row in range(2):
        for col in range(12):
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


if __name__=='__main__':
    tileit(sys.argv[1])