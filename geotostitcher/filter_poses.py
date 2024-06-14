from pathlib import Path
from boxprint import bprint, BoxTypes
from colors import *
import numpy as np
# import matplotlib.pyplot as plt


def print_error(fn: str, errors: list):
    errors = '\n'.join(errors)
    bprint(errors,
           title=f"ERROR: {fn}",
           width=190,
           box_type=BoxTypes.ROUND,
           stroke_func=lambda text: color(text, fg="red")
           )


def get_xyz_from_pose_line(line):
    splits = line.strip().split(' ')
    X, Y, Z = float(splits[-3]), float(splits[-2]), float(splits[-1])
    return np.array([X, Y, Z])


def dist(p1, p2):
    # get distance in centimeters
    return np.sqrt(np.sum(np.square(p1-p2)))*100  


def plot_poses_diff(poses, name):
    
    # poses = poses[:50]
    distances = []
    for i in range(len(poses)-1):
        first = get_xyz_from_pose_line(poses[i])
        second = get_xyz_from_pose_line(poses[i+1])
        distances.append(dist(first, second))
    distances = np.array(distances)
    
    x = np.arange(distances.shape[0])
   
    # fig = plt.figure(figsize=(10,4))
    # ax = fig.add_subplot(111) 
    # ax.set_title(f"Distance between Consecutive poses ({name})")
    # ax.set_ylim(0,210)
    # ax.set_xlabel("Poses")
    # ax.set_ylabel("Distance in cm")
    # ax.bar(x, distances)
    # fig.savefig(f"{name}.jpg")
    
    
def filter_poses(poses, cposes):
    min_dist = 150 
    max_dist = 200
    
    filtered_poses = []
    filtered_cposes = []
    # indeces = []
    i = 0
    while i<len(poses)-2:
        first = get_xyz_from_pose_line(poses[i])
        second = get_xyz_from_pose_line(poses[i+1])
        third = get_xyz_from_pose_line(poses[i+2])
        
        f2s = dist(first, second)
        f2t = dist(first, third)
       
        # print('f2s:', f2s) 
        if f2s < min_dist:
            # print('f2s < min_dist')
            # print('f2t:', f2t) 
            if f2t < max_dist:
                # print('f2t < max_dist')
                # remove second
                # indeces.append(i+2)
                filtered_poses.append(poses[i+2])
                filtered_cposes.append(cposes[i+2])
                i += 2
            else:
                # print('f2t > max_dist')
                # indeces.append(i+1) 
                filtered_poses.append(poses[i+1])
                filtered_cposes.append(cposes[i+1])
                i += 1
        else:
            # print('f2s > min_dist')
            # do nothing
            filtered_poses.append(poses[i+1])
            filtered_cposes.append(cposes[i+1])
            i += 1
    
    # indeces = np.array(indeces) 
    # fig = plt.figure(figsize=(10,4))
    # ax = fig.add_subplot(111) 
    # ax.set_title(f"Removal")
    # ax.set_xlabel("Poses")
    # ax.set_ylabel("Distance in cm")
    # print(indeces.shape)
    # y = np.random.uniform(0, 1, indeces.shape[0])
    # print(y.shape)
    # ax.scatter(indeces, y, s=0.1)
    # fig.savefig(f"removal.jpg")
    # print('removal saved')
            
    return filtered_poses, filtered_cposes


def save_poses_file(poses, filename):
    first_pose = poses[0].strip().split(' ', 1)[0]
    end_pose = poses[-1].strip().split(' ', 1)[0]
    len_poses = len(poses)
    
    with open(filename, 'w') as fp:
        fp.write('200\n1\n')
        fp.write(f"{first_pose} {end_pose}\n")
        fp.write(f"{len_poses}\n")
        fp.writelines(poses)
        
    print(f"Writted filtered poses to: {filename}")

 
def save_closest_file(cposes, header, filename):
    with open(filename, 'w') as fp:
        fp.write(header)
        fp.writelines(cposes)
    print(f"Writted filtered closest to: {filename}")
    

def filter_poses_file(poses_file: Path, closest_file: Path, min_dist: float = 150, max_dist: float = 200):
    """
    Filter Poses file by distance

    Parameters
    ----------
    poses_file: Path
        Path to the .poses file
    min_dist: float
    max_dist: float

    Returns
    -------
    success 
    """
    #! Input error handling
    if type(poses_file) == str:
        poses_file = Path(poses_file)
    elif type(poses_file) == Path:
        ...
    else:
        print_error('filter_poses_file', [
            f"Poses file requested: {poses_file}",
            f"Error: Poses file should be either 'str' or 'Path', but {type(poses_file)} was given!"
        ])
        return None
    if not str(poses_file).endswith('.poses'):
        print_error('filter_poses_file', [
            f"Poses file requested: {poses_file}",
            f"Error: Extension for poses file incorrect! .poses is only accepted."
        ])
        return None
    if not poses_file.exists():
        print_error('filter_poses_file', [
            f"Poses file requested: {poses_file}",
            f"Error: poses file doesn't exists!"
        ])
        return None
    if type(min_dist)==float or type(min_dist)==int:
        min_dist = float(min_dist)
    else:
        print_error('filter_poses_file', [
            f"Given min_dist: {min_dist}",
            f"Error: only int|float is accepted, got {type(min_dist)}"
        ])
        return None
    if type(max_dist)==float or type(max_dist)==int:
        max_dist = float(max_dist)
    else:
        print_error('filter_poses_file', [
            f"Given max_dist: {max_dist}",
            f"Error: only int|float is accepted, got {type(max_dist)}"
        ])
        return None
    
    if max_dist < min_dist:
        print_error('filter_poses_file', [
            f"max_dist {max_dist} < min_dist {min_dist}"
        ])
        return None
    
    print("Input Good for filter_poses_file")
    #!-----------------------------------------------
    
    with open(poses_file, 'r') as fp:
        data = fp.readlines()

    no_of_poses = int(data[3])
    poses = data[4:] 

    if no_of_poses != len(poses):
        print("poses thik xa")
    
    # Remove the leading 1 poses because they have brightness issues 
    poses = poses[1:]
    print(f"Original no of poses: {len(poses)}") 
    
    with open(closest_file, 'r') as fp:
        cdata = fp.readlines()
    
    cposes = cdata[1:] # remove header
    cposes = cposes[1:] # remove leading 1
    
    if len(poses) != len(cposes):
        print_error('filter_poses_file', [
            f"len(poses) {len(poses)} not equal to len(cposes) {len(cposes)}"
        ])
        return None
  
    #! Run Filtering
    print("Running distance threshold filter...")
    for _ in range(3):
        poses, cposes = filter_poses(poses, cposes) 
    
    print(f"Filtered no of poses: {len(poses)}") 
    
    #! Saving
    filter_poses_file_path = str(poses_file).rsplit('.',1)[0]+'.filtered.poses'
    save_poses_file(poses, filter_poses_file_path)

    filter_cposes_file_path = str(closest_file).rsplit('.',1)[0]+'.filtered.closest'
    save_closest_file(cposes, cdata[0], filter_cposes_file_path)
            

if __name__ == '__main__':
    filter_poses_file('terrebone.poses', 1500, 200)