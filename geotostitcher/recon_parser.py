"""
This program simply reads the recon file, parse it and then generate number
of Blur files, each containing blur regions for a particular cam-pose pair
"""

import sys
import pandas as pd
from pathlib import Path
import pickle
from tqdm import tqdm


def get_blur_region_from_csv(csv_file):
    """
    This takes in the object detection file and returns the blur regions
    Currently it blurs: car-plate and face
    """
    df = pd.read_csv(csv_file)
    filtered_df = df[(df['detected_class'] == 'car-plate') | (df['detected_class'] == 'face')][['camera_index', 'pose_number', 'bounding_box_top_left_x', 'bounding_box_top_left_y', 'bounding_box_bottom_right_x', 'bounding_box_bottom_right_y']]
    filtered_df = filtered_df.sort_values(by = ['camera_index','pose_number']) 
    return filtered_df.values.tolist()


def generate_blur_files(out_dir, rec):
    print("\nExtracting Blurring information from the Recon file:")

    csv_dir = Path(f"{out_dir}/intermediate/blur/{rec}")
    csv_files = [str(file) for file in csv_dir.iterdir() if file.is_file() and file.suffix == ".csv"]
    
    if len(csv_files) == 0:
        print("No CSV files available. Returning None")
        return None
    elif len(csv_files)>1:
        print("Multiple CSV files available.")
        csv_file = csv_files[0]
        print(f"Using: {csv_file}")
    else:
        csv_file = csv_files[0]
        print(f"Using: {csv_file}")
        
    blur_regions = get_blur_region_from_csv(csv_file)
    print(f"Total {len(blur_regions)} blur regions available!")
    
    for br in tqdm(blur_regions):
        cam, pose, tlx, tly, brx, bry = br
        blur_region = [tlx, tly, brx, bry]
        blur_file = Path(f"{csv_dir}/{int(cam):02d}/{pose}.pkl")
        
        if blur_file.exists():
            with open(blur_file, 'rb') as f:
                all_blur_regions = pickle.load(f)
                if blur_region not in all_blur_regions:
                    all_blur_regions.append(blur_region)
                    
            with open(blur_file, 'wb') as f:
                pickle.dump(all_blur_regions, f)
                
        else:
            with open(blur_file, 'wb') as f:
                all_blur_regions = [blur_region]
                pickle.dump(all_blur_regions, f)
                
    print("Done generating blur files!")
        

if __name__=='__main__':
    #! Params: (output_dir , recording number)
    generate_blur_files(sys.argv[1], sys.argv[2])