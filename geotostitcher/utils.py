import os
from os.path import exists
from pathlib import Path
from tqdm import tqdm
from boxprint import bprint, BoxTypes
from colors import color

from .filter_poses import filter_poses_file

def print_error(errors: list):
    errors = '\n'.join(errors)
    print('\n')
    bprint(errors,
           title=f"ERROR",
           width=190,
           box_type=BoxTypes.ROUND,
           stroke_func=lambda text: color(text, fg="red")
           )

 
def print_success(message: list):
    message = '\n'.join(message)
    print('\n')
    bprint(message,
           title=f"SUCCESS",
           width=190,
           box_type=BoxTypes.ROUND,
           stroke_func=lambda text: color(text, fg="green")
           )
    
def print_info(message: list):
    message = '\n'.join(message)
    print('\n')
    bprint(message,
           title=f"INFO",
           width=190,
           box_type=BoxTypes.ROUND,
           stroke_func=lambda text: color(text, fg="blue")
           )


def get_project_name_from_input_dir(input_dir):
    """
    Extract Project name from input dir path

    Parameters
    ----------
    input_dir: str
        Path to input directory
    
    Returns
    -------
    project_name: str
        Name of the project
    """
    splits = input_dir.split('/')
    return splits[-1]

def list_prj(path):
    files = os.listdir(path)

    for f in files:
        if f[-3:] == 'out':
            files.remove(f)

    return files



def get_recordings(input_dir):
    """
    Get the list of recordings
    
    Parameters
    ----------
    input_dir: str
        Path to input directory
        
    Returns
    -------
    recordings: list
        List of recording names
    """
    images_dir = input_dir + '/images'
    recordings = os.listdir(images_dir)
    return recordings


def get_cameras(input_dir, rec):
    """
    Get the list of cameras for a particular recording
    
    Parameters
    ----------
    input_dir: str
        Path to input directory
    rec: str
        Name of recording

    Returns
    -------
    cams: list
        List of names of cameras for recording 'rec'
    """
    input_dir = f"{input_dir}/images/{rec}"
    cams = [ name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name)) ]
    cams.sort()
    if 'dump' in cams:
        cams.remove('dump')
    # cams = os.listdir(f"{input_dir}/images/{rec}")
    return cams


def get_recordings_and_cameras(input_dir):
    """
    Get all the available recordings and cameras under each recordings

    Parameters
    ----------
    input_dir: str
        Path to input directory

    Returns
    -------
    recordings: dict
        Dictionary where key=rec_name and value=list of cameras for that recording
        eg: {
            '101': ['00', '01', '02', '03', '04', '05'],
            '102': ['00', '01', '02', '03', '04']
        }
    """
    r_and_c = {}
    recordings = get_recordings(input_dir)
    for rec in recordings:
        cameras = get_cameras(input_dir, rec)
        r_and_c[rec] = cameras
    return r_and_c


def build_output_dirs(rec_and_cams, output_dir):
    """
    Build the output directory structure (If doesn't exists)
    
    Parameters
    ----------
    rec_and_cams: dict
        Dictionary where key=rec_name and value=list of cameras for that recording
    output_dir: str
        Path to output dirctory

    Returns
    -------
    None 
    """
    #! For each recording:
    for r,cams in rec_and_cams.items():
        #! Build dir for each camera
        for c in cams:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            cam_dir.mkdir(parents=True, exist_ok=True)

        #! Build Blur cam directories
        jpgcamsblur = ['08_blur', '09_blur', '10_blur', '11_blur', '12_blur', '13_blur', '08_crop', '09_crop', '10_crop', '11_crop', '12_crop', '13_crop']
        for c in jpgcamsblur:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            cam_dir.mkdir(parents=True, exist_ok=True)

        #! Build dirs for 360low and 360high
        dir360low = Path(output_dir+'/images/'+r+'/360tiles')
        dir360low.mkdir(parents=True, exist_ok=True)

        dir360high = Path(output_dir+'/images/'+r+'/360high')
        dir360high.mkdir(parents=True, exist_ok=True)

    #! Build intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    intermediate_dir.mkdir(parents=True, exist_ok=True)

    #! Build dirs for pts files
    for r,cams in rec_and_cams.items():
        pts_dir = Path(output_dir+'/intermediate/pts/'+r)
        pts_dir.mkdir(parents=True, exist_ok=True)
        
    #! Build dirs for blur data
    for r,cams in rec_and_cams.items():
        cams_to_blur = ['08', '09', '10', '11', '12', '13']
        for c in cams_to_blur:
            pts_dir = Path(output_dir+'/intermediate/blur/'+r+'/'+c)
            pts_dir.mkdir(parents=True, exist_ok=True)


def verify_output_dirs(rec_and_cams, output_dir):
    """
    Verify the output directory structure is correct
    
    Parameters
    ----------
    rec_and_cams: dict
        Dictionary where key=rec_name and value=list of cameras for that recording
    output_dir: str
        Path to output dirctory

    Returns
    -------
    success: bool
        Returns 1 if output dir okay, else 0
    """
    success = 1

    #! Function to check if dir exists
    def check_dir(path):
        if not path.exists():
            print(path, "doesn't exists")
            return 0
        else:
            return 1

    #! For each recording:
    for r,cams in rec_and_cams.items():
        #! Check dir for each camera
        for c in cams:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            success = check_dir(cam_dir) and success

        #! Check blur dir
        jpgcamsblur = ['08_blur', '09_blur', '10_blur', '11_blur', '12_blur', '13_blur', '08_crop', '09_crop', '10_crop', '11_crop', '12_crop', '13_crop']
        for c in jpgcamsblur:
            cam_dir = Path(output_dir+'/images/'+r+'/'+c)
            success = check_dir(cam_dir) and success

        #! Check dirs for 360 and 360low
        dir360 = Path(output_dir+'/images/'+r+'/360tiles')
        success = check_dir(dir360) and success
        dir360low = Path(output_dir+'/images/'+r+'/360high')
        success = check_dir(dir360low) and success

    #! Check intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    success = check_dir(intermediate_dir) and success

    return success


def search_files_for_this_rec(input_dir, rec, search_dir='poses', extension='.poses'):
    """
    Search files for a specific recording.
    If finds all the file of this format:
           {input_dir}/{search_dir}/anything__poses__{rec}anything/{*.extension}

    Parameters
    ----------
    input_dir: str
        Path to input directory
    rec: str
        Name of recording
    search_dir: str
    extension: str

    Returns
    -------
    files: list[str]
        Selected files
    """
    project_name = get_project_name_from_input_dir(input_dir)
    poses_dirs = os.listdir(f"{input_dir}/{search_dir}") 

    selected_poses_dirs = []
    for pd in poses_dirs:
        splits = pd.split('__')[2]
        if splits.startswith(f"{rec}"):
            selected_poses_dirs.append(pd)
       
    if len(selected_poses_dirs)==0:
        print("Couldn't find poses directory!")
        return None
       
    selected_poses_files = [] 
    for spd in selected_poses_dirs:
        poses_path = f"{input_dir}/{search_dir}/{spd}"
        files = os.listdir(poses_path)
        poses_files = []
        
        for fi in files:
            if fi.endswith(extension):
                #! removing this filter assuming that all the original .poses will be renamed to .orgposes
                # if not fi.endswith('filtered'+extension): # dont take 'filtered.poses' type files
                poses_files.append(fi)
                
        if len(poses_files)>1:
            print(f"Error: Multiple files found inside {poses_path}")
            first_poses_file = poses_files[0]
            print(f"But I am using the first one: {first_poses_file}")
            selected_poses_files.append(f"{poses_path}/{first_poses_file}")
        elif len(poses_files) == 1:
            first_poses_file = poses_files[0]
            selected_poses_files.append(f"{poses_path}/{first_poses_file}")
        elif len(poses_files) == 0:
            print(f"Error: No *{extension} file found inside {poses_path}. Ignoring this dir!")

        
    if len(selected_poses_files) == 0:
        print_error([f"No '*{extension}' file found inside '{search_dir}' directory.",
                     f"Are you sure you've kept '*{extension}' files inside '{search_dir}' directory for recording '{rec}' ??"])
        return None
       
    selected_poses_files_that_exists = [] 
    for spf in selected_poses_files:
        if Path(spf).exists():
            selected_poses_files_that_exists.append(spf)
        else:
            f"{spf} was selected but this file doesn't exist. So ignoring."
            
    print(f"\nUsing these {extension} files:") 
    for spfte in selected_poses_files_that_exists:
        print('  ->',spfte)
        
    if len(selected_poses_files_that_exists)>0:
        return selected_poses_files_that_exists
    else:
        print(f"No {extension} file found for rec {rec}. Returning None!!")
        return None
    

  
def get_final_poses_and_closest_file_for_this_rec(input_dir, rec):
    """
    Get the path to poses file for this recording

    Parameters
    ----------
    input_dir: str
        Path to input directory
    rec: str
        Name of recording

    Returns
    -------
    poses_file_path: str
        Path of the poses file
    """
    project_name = get_project_name_from_input_dir(input_dir)
    poses_dirs = os.listdir(f"{input_dir}/posesfinal") 

    for pd in poses_dirs:
        if pd.startswith(f"{project_name}__poses__{rec}"):
            break

    splits = pd.split('__')
    if splits[2][:3] != rec:
        print("Couldn't find poses directory!")
        return None, None

    poses_file_name = f"{splits[0]}_{splits[-1]}.poses"
    poses_file_path = f"{input_dir}/posesfinal/{pd}/{poses_file_name}"

    closest_file_name = f"{splits[0]}_{splits[-1]}.closest"
    closest_file_path = f"{input_dir}/posesfinal/{pd}/{closest_file_name}"

    if not Path(poses_file_path).exists():
        print(f"Poses file unavailable for recording {rec}")
    
    if not Path(poses_file_path).exists():
        print(f"Closest file unavailable for recording {rec}")

    if Path(poses_file_path).exists() and Path(poses_file_path).exists(): 
        return poses_file_path, closest_file_path
    else:
        return None, None


def get_image_seq_from_poses_file(poses_file_path):
    """
    Get the image sequence from poses file

    Parameters
    ----------
    poses_file_path: str
        Poses file path

    Returns
    -------
    seq_list: list
        Sequence of images available in the poses file
    
    """
    with open(poses_file_path, 'r') as f:
        seq_list = [line.split(None, 1)[0] for line in f]
        seq_list = seq_list[4:]
    return seq_list


def generate_filtered_images_list(input_dir, output_dir, rec, cams):
    """
    Generate filtered images list for each recording and store the list in a text file.
    The text file is saved under output_dir/intermediate/filtered_{rec_name}.txt

    Parameters
    ----------
    input_dir: str
        Path to input directory
    output_dir: str
        Path to output dirctory
    rec: str
        Name of the recording 
    cams: list
        List of cameras of this rec

    Returns
    -------
    None

    """
    output_filename = f"{output_dir}/intermediate/filtered_{rec}.txt"
    f = open(output_filename, "w")

    #! Filter poses by distance
    poses_files = search_files_for_this_rec(input_dir, rec, 'poses', '.poses')
    closest_files = search_files_for_this_rec(input_dir, rec, 'poses', '.closest')
   
    
    for pf,cf in zip(poses_files, closest_files): 
        filter_poses_file(pf, cf, 150, 200)
       
    #! Upload poses dir 
    for pf in poses_files: 
        pf_dir = Path(pf).parent
        splits = str(pf_dir).rsplit('/',3)[1:]
        pose_unique_path = '/'.join(splits)
        aws_path = f"s3://geoto-projects-recon/{pose_unique_path}"
        pose_dir_upload_command = f"aws s3 sync {pf_dir} {aws_path}"
        print(f"Uploading to Recon: {pf_dir}") 
        os.system(pose_dir_upload_command)
        print("Done")
        
    #! Filter poses common to images in all the camers
    poses_files = search_files_for_this_rec(input_dir, rec, 'poses', 'filtered.poses')
   
    img_seq_from_poses = [] 
    for pf in poses_files:
        img_seq_from_poses += get_image_seq_from_poses_file(pf)
    
    print(f"{len(img_seq_from_poses)} seq available in poses file.")

    #TODO Here I have set the camera names explicitely
    #TODO But the number/names of cameras might vary in future!
    #TODO No, make this flexible!!
    #Here, top_cams = cams with pgf images and doesn't participate in panaroma generation
    #      bottom_cams = cams with jpg images and participates in panaroma creation
    top_cams = ['00','01','02','03','04','05','06','07']
    bottom_cams = ['08', '09', '10', '11', '12', '13']

    unav_cams = [] # Unavailable top cams
    for tc in top_cams:
        if not os.path.isdir(f"{input_dir}/images/{rec}/{tc}"):
            unav_cams.append(tc)

    for uc in unav_cams:
        top_cams.remove(uc)
        
    unav_cams = [] # Unavailable bottomcams
    for tc in bottom_cams:
        if not os.path.isdir(f"{input_dir}/images/{rec}/{tc}"):
            unav_cams.append(tc)

    for uc in unav_cams:
        bottom_cams.remove(uc)
    
    print("\nAvailable cams:") 
    print(f"  -> Top PGF cams: {top_cams}")
    print(f"  -> Bottom JPG cams: {bottom_cams}")

    print("\nFiltering the poses that are common to all the available Cam directories and the poses file:")
    good_seq_count = 0
    for seq in tqdm(img_seq_from_poses):
        seq_good = True

        for c in top_cams:
            file_to_search = f"{input_dir}/images/{rec}/{c}/image.{seq}.pgf"
            if not exists(file_to_search):
                seq_good = False
                break

        if not seq_good:
            continue

        for c in bottom_cams:
            file_to_search_1 = f"{input_dir}/images/{rec}/{c}/image.{seq}.jpg"
            file_to_search_2 = f"{output_dir}/images/{rec}/{c}/image.{seq}.jpg"
            if not exists(file_to_search_1) and not exists(file_to_search_2):
                seq_good = False
                break
                
        if seq_good:
            good_seq_count += 1
            f.write(seq)
            f.write('\n')

    f.close()
    
    print(f"{good_seq_count} poses are good ones!")
    print(f"Filter Poses completed for rec {rec}")


def generate_filtered_images_list_forall(input_dir, output_dir, r_and_c):
    """
    Generate filtered image list for all
    
    Parameters
    ----------
    r_and_c: dict
        Dictionary where key=rec_name and value=list of cameras for that recording
        eg: {
            '101': ['00', '01', '02', '03', '04', '05'],
            '102': ['00', '01', '02', '03', '04']
        } 
    """
    for r,c in r_and_c.items():
        generate_filtered_images_list(input_dir, output_dir, r, c)


def get_list_from_filtered_images_file(file_path):
    """
    Get list of image sequence from filtered images file

    Parameters
    ----------
    file_path: str
        Path to filtered images file
    
    Returns
    -------
    seq: list
        List of sequence numbers from file
    """
    with open(file_path, 'r') as f:
        seq_list = [line[:-1] for line in f]
    
    return seq_list


def generate_pgftojpg_commands(input_dir, output_dir, r, c):
    """
    Generate pgftojpg commands for each recordings and store them in a text file.
    The text file is saved under output_dir/intermediate/pgf2jpg_{rec}.txt

    Parameters
    ----------

    Returns
    -------
    success: bool
        1 if succeed else 0
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #TODO Scan and prepare the list of cameras which has PGF images
    cam_pgf = ['00', '01', '02', '03', '04', '05', '06', '07']

    unav_cams = []
    for tc in cam_pgf:
        if not os.path.isdir(f"{input_dir}/images/{r}/{tc}"):
            unav_cams.append(tc)

    for uc in unav_cams:
        cam_pgf.remove(uc)


    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/pgf2jpg_{r}.txt"
    f = open(output_filepath, "w")

    #! For each camera with pgf images:
    for c_pgf in cam_pgf:
        for s in seq:
            cmd = f"pgf2jpg {input_dir}/images/{r}/{c_pgf}/image.{s}.pgf {output_dir}/images/{r}/{c_pgf}/image.{s}.jpg"
            f.write(cmd)
            f.write('\n')

    #! Close the file
    f.close()

    print(f"Generate pgf2jpg commands completed for rec {r}")

    return 1


def generate_pgftojpg_commands_all(input_dir, output_dir, r_and_c):
    """
    Generate pgf2jpg commands for all recordings
    """
    for r,c in r_and_c.items():
        generate_pgftojpg_commands(input_dir, output_dir, r, c)


def generate_movejpg_commands(input_dir, output_dir, r, c):
    """
    Generate movejpg Commands for a particular recording
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #TODO Scan and prepare the list of cameras which has JPG images
    cam_jpg = ['08', '09', '10', '11', '12', '13']

    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/movejpgs_{r}.txt"
    f = open(output_filepath, "w")

    #! For each camera with pgf images:
    for c_jpg in cam_jpg:
        for s in seq:
            cmd = f"mv {input_dir}/images/{r}/{c_jpg}/image.{s}.jpg {output_dir}/images/{r}/{c_jpg}/image.{s}.jpg"
            f.write(cmd)
            f.write('\n')

    #! Close the file
    f.close()

    print(f"Generate movejpg commands completed for rec {r}")

    return 1


def generate_movejpg_commands_all(input_dir, output_dir, r_and_c):
    """
    Generate movejpg commands for all recordings
    """
    for r,c in r_and_c.items():
        generate_movejpg_commands(input_dir, output_dir, r, c)


def generate_stitch_commands(output_dir, r, cfg_file):
    """
    Generate stitch commands for a recording
    
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/stitch_{r}.txt"
    f = open(output_filepath, "w")

    for s in seq:
        command = f"stitcher {output_dir} {r} {s} {cfg_file}"
        f.write(command)
        f.write('\n')

    f.close()

    return 1

def generate_stitch_commands_all(output_dir, recs, cfg_file):
    """
    Generate stitch commands for all recordings
    """
    for r in recs:
        generate_stitch_commands(output_dir, r, cfg_file)

def generate_360low_commands(output_dir, r):
    """
    Generate 360low commands for a recording
    # convert -quality 27 360high/image.104000000.jpg 360low/image.104000000.jpg
    
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/360low_{r}.txt"
    f = open(output_filepath, "w")

    for s in seq:
        # command = f"convert -quality 27 {output_dir}/images/{r}/360high/image.{s}.jpg {output_dir}/images/{r}/360low/image.{s}.jpg"
        command = f"python3 /home/leon/rashik/geotostitcher/geotostitcher/tiler.py {output_dir}/images/{r}/360high/image.{s}.jpg"
        f.write(command)
        f.write('\n')

    f.close()

    print(f"Generate 360low commands completed for rec {r}")

    return 1

def generate_360low_commands_all(output_dir, recs):
    """
    Generate 360low commands for all recordings
    """
    for r in recs:
        generate_360low_commands(output_dir, r)


def generate_upload_commands(output_dir, r, prj_name):
    """
    Generate Upload PGF commands for a recording
        aws s3 sync 101/360high/  s3://geoto-projects/test-repentigny-2023-k1-8/images/101/360high/
    """
    pgfcams = ['00','01','02','03','04','05','06','07']
    jpgcams = ['08', '09', '10', '11', '12', '13']
    jpgcamsblur = ['08_blur', '09_blur', '10_blur', '11_blur', '12_blur', '13_blur']
    jpgcamscrop = ['08_crop', '09_crop', '10_crop', '11_crop', '12_crop', '13_crop']
    highs = ['360high']
    lows = ['360tiles']

    unav_cams = []
    for tc in pgfcams:
        if not os.path.isdir(f"{output_dir}/images/{r}/{tc}"):
            unav_cams.append(tc)

    for uc in unav_cams:
        pgfcams.remove(uc)

    names = ['uploadpgf', 'uploadjpg', 'uploadjpgblur', 'uploadjpgcrop', 'upload360high', 'upload360low']
    all_cams = [pgfcams, jpgcams, jpgcamsblur, jpgcamscrop, highs, lows]

    for i in range(len(names)):
        name = names[i]
        cam_list = all_cams[i]
        print(name, cam_list)

        output_filepath = f"{output_dir}/intermediate/{name}_{r}.txt"
        f = open(output_filepath, "w")

        for c in all_cams[i]:
            if c in jpgcams:
                command = f"aws s3 sync {output_dir}/images/{r}/{c}/ s3://geoto-projects-recon/{prj_name}/images/{r}/{c}/"
            elif c in jpgcamscrop:
                command = f"aws s3 sync {output_dir}/images/{r}/{c}/ s3://geoto-projects-recon/{prj_name}/images/{r}/{c[:-5]}/"
            elif c in jpgcamsblur:
                command = f"aws s3 sync {output_dir}/images/{r}/{c}/ s3://geoto-projects-prod/{prj_name}/images/{r}/{c[:-5]}/"
            else:
                command = f"aws s3 sync {output_dir}/images/{r}/{c}/ s3://geoto-projects-prod/{prj_name}/images/{r}/{c}/"

            f.write(command)
            f.write('\n')

        f.close()

    print(f"Generate Upload commands completed for rec {r}")

    return 1

def generate_upload_commands_all(output_dir, recs, prj_name):
    """
    Generate Upload PGF commands for all recordings
    """
    for r in recs:
        generate_upload_commands(output_dir, r, prj_name)


def generate_download_recon_commands(output_dir, r, prj_name):
    """
    Generate Download Recon commands for a recording
        aws s3 cp s3://geoto-projects-prod/{prj_name}/ptgui/{r}/recon.csv {output_dir}/recon.csv
    """
    output_filepath = f"{output_dir}/intermediate/download_recon_{r}.txt"
    f = open(output_filepath, "w")
    command = f"aws s3 cp s3://geoto-projects-prod/{prj_name}/ptgui/{r}/{r}recon.csv {output_dir}/intermediate/recon_{r}.csv"
    f.write(command)
    f.write('\n')
    f.close()

    print(f"Generate Download Recon commands completed for rec {r}")

    return 1

def generate_download_recon_commands_all(output_dir, recs, prj_name):
    """
    Generate Download Recon commands for all recordings
    """
    for r in recs:
        generate_download_recon_commands(output_dir, r, prj_name)


def generate_blurring_commands(output_dir, r):
    """
    Generate Blurring commands for a recording
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #TODO Scan and prepare the list of cameras which has JPG images
    cam_jpg = ['08', '09', '10', '11', '12', '13']

    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/blurring_{r}.txt"
    f = open(output_filepath, "w")

    #! For each camera with pgf images:
    for c_jpg in cam_jpg:
        for s in seq:
            cmd = f"python3 /home/leon/rashik/geotostitcher/geotostitcher/blurrer.py {output_dir}/images/{r}/{c_jpg}/image.{s}.jpg"
            f.write(cmd)
            f.write('\n')

    #! Close the file
    f.close()

    print(f"Generate Blurring commands completed for rec {r}")

    return 1


def generate_cropping_commands(output_dir, r):
    """
    Generate Cropping commands for a recording
    """
    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #TODO Scan and prepare the list of cameras which has JPG images
    cam_jpg = ['08', '09', '10', '11', '12', '13']

    #! Open file to store the commands
    output_filepath = f"{output_dir}/intermediate/cropping_{r}.txt"
    f = open(output_filepath, "w")

    #! For each camera with pgf images:
    for c_jpg in cam_jpg:
        for s in seq:
            cmd = f"echo image.{s}.jpg;convert {output_dir}/images/{r}/{c_jpg}/image.{s}.jpg -crop 4096x3008+0+0 {output_dir}/images/{r}/{c_jpg}_crop/image.{s}.jpg"
            f.write(cmd)
            f.write('\n')

    #! Close the file
    f.close()

    print(f"Generate Cropping commands completed for rec {r}")

    return 1

def generate_cropping_commands_all(output_dir, recs):
    """
    Generate cropping commands for all recordings
    """
    for r in recs:
        generate_cropping_commands(output_dir, r)
        
        
def generate_blurring_commands_all(output_dir, recs):
    """
    Generate Blurring commands for all recordings
    """
    for r in recs:
        generate_blurring_commands(output_dir, r)


def get_commands_file(output_dir, command, rec):
    """
    Get particular command file path of given rec
    """
    file = f"{output_dir}/intermediate/{command}_{rec}.txt"
    return file


def generate_batch_files(output_dir, r):
    """
    Generate Batch files for a set of pts files
    """

    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    batch_file_path = f"{output_dir}/intermediate/pts/{r}_batch.ptgbatch"
    f = open(batch_file_path, "w") 

    #! Starting of a batch file
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<PTGuiBatchList>\n')
    
    #! Middle of batch file
    for s in seq:
        to_write = f"<Project FileName=\"{output_dir}/intermediate/pts/{r}/image.{s}.pts\" Enabled=\"true\" DeleteWhenDone=\"false\"/>\n"
        f.write(to_write)


    #! End of a batch file
    f.write('</PTGuiBatchList>\n')

    f.close()

    print(f"Done writing batch file for rec {r}")


def generate_pts_files(output_dir, r, template_path):
    """
    Generate PTS files for a recording 
    
    """
    #! Keyword selector
    word = '$$$'

    #! Get the seq from filtred_{rec}.txt file
    filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
    if not Path(filtered_filepath).exists():
        print(filtered_filepath, "doesn't exists") 
        return 0
    else:
        seq = get_list_from_filtered_images_file(filtered_filepath)

    #! For each seq:
    for s in tqdm(seq):
        # print(f"Generating pts file for sequence {s} of recording {r}")
        output_file = f"{output_dir}/intermediate/pts/{r}/image.{s}.pts"
        f = open(output_file, "w")


        #! Read the template file
        with open(template_path, "r") as file:
            for line_number, line in enumerate(file, start=1):  

                # #! For each line in template:
                # if word in line:
                #     # print(f"Word '{word}' found on line {line_number}")
                #     splits = line.split('$$$')
                #     new_line_list = []
                #     #! For each word in the line:
                #     for w in splits:
                #         if w == 'output_file_path':
                #             w = f"{output_dir}/images/{r}/360high/image.{s}.jpg"
                #         elif w == 'output_jpg_quality':
                #             w = '70' #TODO Get jpg quality from some config or as parameters
                #         elif w.startswith('image_from_camera'):
                #             # print(w.split('_'))
                #             # input()
                #             camera = w.split('_')[-1]
                #             # print(camera)
                #             # input()
                #             w = f"{output_dir}/images/{r}/{camera}_blur/image.{s}.jpg"
                #             # print(w)
                #             # input()

                #         new_line_list.append(w)

                    # new_line = ''.join(new_line_list)

                    # f.write(new_line)

                # else:
                    # f.write(line)

                if '08.jpg' in line:
                    line = line.replace('08.jpg', f"{output_dir}/images/{r}/08_blur/image.{s}.jpg")
                elif '09.jpg' in line:
                    line = line.replace('09.jpg', f"{output_dir}/images/{r}/09_blur/image.{s}.jpg")
                elif '10.jpg' in line:
                    line = line.replace('10.jpg', f"{output_dir}/images/{r}/10_blur/image.{s}.jpg")
                elif '11.jpg' in line:
                    line = line.replace('11.jpg', f"{output_dir}/images/{r}/11_blur/image.{s}.jpg")
                elif '12.jpg' in line:
                    line = line.replace('12.jpg', f"{output_dir}/images/{r}/12_blur/image.{s}.jpg")
                elif '13.jpg' in line:
                    line = line.replace('13.jpg', f"{output_dir}/images/{r}/13_blur/image.{s}.jpg")
                elif '360high.jpg' in line:
                    line = line.replace('360high.jpg', f"{output_dir}/images/{r}/360high/image.{s}.jpg")
                else:
                    line = line

                f.write(line)
                

        # print(f"Generated pts file for sequence {s} of recording {r}")

    generate_batch_files(output_dir, r)



    




