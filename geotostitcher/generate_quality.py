import os
import sys
from datetime import datetime
import numpy as np
from tqdm import tqdm
from datetime import datetime, timedelta 

def get_timestamps_from_gz_file(file_path):
    os.system(f"gunzip -kf {file_path}")
    timestamps = []
    extraction_started = 0
    with open(file_path[:-3]) as fp:
        for line in fp:
            line = line.strip()

            if line.startswith("Original images in directory 1"):
                print("Found END idx of timestamp extraction!")
                break

            if not extraction_started:
                if line.startswith("Original images in directory 0"):
                    print("Found START idx of timestamp extraction!")
                    extraction_started = 1
                continue

            timestamp = line.split('.')[2]
            timestamp_full = '17' + timestamp
            date_object = datetime.fromtimestamp(int(timestamp_full))
            timestamps.append(f"{date_object.date()}-{date_object.time()}")

    return np.array(timestamps)

def gps_to_utc(gps_week, gps_seconds): 
    # GPS epoch 
    gps_epoch = datetime(1980, 1, 6, 0, 0, 0) 
    
    # Number of weeks since GPS epoch 
    weeks_delta = timedelta(weeks=gps_week) 
    
    # Number of seconds since GPS epoch 
    seconds_delta = timedelta(seconds=gps_seconds) 
    
    # Calculate the date and time in GPS time 
    gps_time = gps_epoch + weeks_delta + seconds_delta 
    
    # Add leap seconds (as of 2022) 
    
    leap_seconds = 18 
    gps_time += timedelta(seconds=leap_seconds) 
    
    return gps_time 

def get_timestamps_from_gps_trigger(file_path):
    with open(file_path) as fp:
        data = fp.readlines()

    timestamps = []
    for line in data:
        line = line.strip()
        count, week, sec = line.split(' ')
        gps_time = gps_to_utc(int(week), int(sec[:6]))
        timestamps.append(f"{gps_time.date()}-{gps_time.time()}")

    return np.array(timestamps)

def get_qualities_from_closest_file(closest_file):
    #! Read data
    data = np.loadtxt(closest_file, delimiter=" ", dtype=str, skiprows=1)
    poses, qualites = data[:,0], data[:,6]

    poses_int = []
    for p in poses:
        poses_int.append(int(p[3:]))
    poses_int = np.array(poses_int)

    #! Update Quality
    if 'GCP' in closest_file:
        qualites[:] = '2'
    else:
        mask = np.logical_and(qualites!='2', qualites!='3')
        qualites[mask] = '2'

    qualites_int = []
    for q in qualites:
        qualites_int.append(int(q))
    qualites_int = np.array(qualites_int)

    return poses_int, qualites_int

def generate_quality_file(pfile, timestamps, pose_count, qualities):
    print("\nGenerating .qtl file:")
    # print(np.min(pose_count), np.max(pose_count))
    timestamps_filter = timestamps[pose_count]

    with open(pfile) as pf:
        poses = pf.readlines()

        assert len(poses) == pose_count.shape[0]+4, f"Assertin Failed for {poses}"

        for i in range(4, len(poses)):
            poses[i] = f"{poses[i].strip()} {qualities[i-4]} {timestamps_filter[i-4]}\n"

    #! Write Quality File
    pfile_splits = pfile.split('/')
    pfile_path, pfile_name = pfile_splits[:-1], pfile_splits[-1]
    rec = pfile_name.split('_')[1][:3]
    qfile_name = f"{rec}.qtl"
    pfile_path.append(qfile_name)
    qfile = '/'.join(pfile_path)

    print(f"Writing data to {qfile}") 
    with open(qfile, 'w') as qf:
        qf.writelines(poses)
    print("Done!")
    return qfile

def generate_quality(tfile, cfile, pfile):
    timestamps = get_timestamps_from_gps_trigger(tfile)
    poses, qualities = get_qualities_from_closest_file(cfile)
    return generate_quality_file(pfile, timestamps, poses, qualities)


if __name__=='__main__':

    #! Data from args
    gps_trigger_data = sys.argv[1]
    closest = sys.argv[2]
    pfile = sys.argv[3]

    #! Mock Data
    # gz_file = '/home/rashik/Downloads/test/rename_details.log.gz'
    # gps_trigger_data = '/home/rashik/Downloads/test/gps_trigger_data.txt'
    # closest = '/home/rashik/Downloads/test/k2-12-hampstead2024-pilot-projection2_101000000-101001981.1707875712.closest'
    # pfile = "/home/rashik/Downloads/test/k2-12-hampstead2024-pilot-projection2_101000000-101001981.1707875712.poses"

    # timestamps = get_timestamps_from_gz_file(gz_file)
    timestamps = get_timestamps_from_gps_trigger(gps_trigger_data)
    poses, qualities = get_qualities_from_closest_file(closest)

    generate_quality_file(pfile, timestamps, poses, qualities)


