import os
import sys
from pathlib import Path
from colorama import Fore, Back, Style

print('Output Directory Configuration')
print('------------------------------')

input_dir = input('Input Directory: ')
output_dir = input('Output Directory: ')

# Program Inputs
# input_dir = '/media/leon/New Volume/mrcsource-pave-2022-gps_input'
# output_dir = '/media/leon/New Volume/mrcsource-pave-2022-gps'
# 
# input_dir = '/media/leon/Terrebonne_2021_part1_8TB/Terrebonne_2022_part1_8TB/Rashik/mrcsource-pave/2022'

cameras = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13']

# Start Program
abort = 0

# Check level 1 dir
level_1_dir = os.listdir(input_dir)
if 'images' not in level_1_dir:
    print("'images' directory is not available in Input Directory. Aborting...")
    abort = 1

if 'poses' not in level_1_dir:
    print(Fore.RED + "'poses' directory is not available in Input Directory. Aborting..." + Fore.WHITE)
    abort = 1

if not abort:
    print(Fore.GREEN + "Level 1 dir Okay" + Fore.WHITE)
else:
    print('Aborting...')
    sys.exit()

# Check images dir
images_dir = input_dir + '/images'
recordings = os.listdir(images_dir)
no_of_rec = len(recordings)
print(no_of_rec, 'recordings found')

for rec in recordings:
    d = os.listdir(images_dir + '/' + rec)
    for cam in range(14):
        cam_name = str(cam).zfill(2)
        if cam_name not in d:
            print('Camera ' + cam_name + ' not available in recording ' + rec)
            abort = 1
            
if not abort:
    print('All cameras 00-13 available in all the recordings')
else:
    print('Aborting...')
    sys.exit()


def build_output_dirs(output_dir, recordings, cameras):
    '''Builds the directory structure of output
    
    Parameters
    ----------
    output_dir: str
        Output Directory
    recordings: list
        List of strings of names of recordings
    cameras: list
        List of strings of names of cameras
    '''

    # Build cameras dir 00-13,360,360low for each recordings
    for r in recordings:
        for c in cameras:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            cam_dir.mkdir(parents=True, exist_ok=True)

        dir360 = Path(output_dir+'/images/'+r+'/360')
        dir360low = Path(output_dir+'/images/'+r+'/360low')
        dir360.mkdir(parents=True, exist_ok=True)
        dir360low.mkdir(parents=True, exist_ok=True)

    # Build intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    intermediate_dir.mkdir(parents=True, exist_ok=True)

def verify_output_dirs(output_dir, recordings, cameras):
    '''Verify output dir structure
    
    Parameters
    ----------
    output_dir: str
        Output Directory
    recordings: list
        List of strings of names of recordings
    cameras: list
        List of strings of names of cameras
    '''
    success = 1

    def check_dir(path):
        if not path.exists():
            print(path, "doesn't exists")
            return 0
        else:
            return 1

    # Build cameras dir 00-13,360,360low for each recordings
    for r in recordings:
        for c in cameras:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            success = check_dir(cam_dir) and success

        dir360 = Path(output_dir+'/images/'+r+'/360')
        success = check_dir(dir360) and success
        dir360low = Path(output_dir+'/images/'+r+'/360low')
        success = check_dir(dir360low) and success

    # Build intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    success = check_dir(intermediate_dir) and success

    return success


build_output_dirs(output_dir, recordings, cameras)

if not verify_output_dirs(output_dir, recordings, cameras):
    print("Incomplete Output Directory structure. Aborting...")
    sys.exit()