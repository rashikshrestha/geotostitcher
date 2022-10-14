import os
from pathlib import Path

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

        #! Build dirs for 360 and 360low
        dir360 = Path(output_dir+'/images/'+r+'/360')
        dir360low = Path(output_dir+'/images/'+r+'/360low')
        dir360.mkdir(parents=True, exist_ok=True)
        dir360low.mkdir(parents=True, exist_ok=True)

    #! Build intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    intermediate_dir.mkdir(parents=True, exist_ok=True)


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

        #! Check dirs for 360 and 360low
        dir360 = Path(output_dir+'/images/'+r+'/360')
        success = check_dir(dir360) and success
        dir360low = Path(output_dir+'/images/'+r+'/360low')
        success = check_dir(dir360low) and success

    #! Check intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    success = check_dir(intermediate_dir) and success

    return success


def get_poses_file_path_for_this_rec(input_dir, rec):
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
    poses_dirs = os.listdir(f"{input_dir}/poses") 

    for pd in poses_dirs:
        if pd.startswith(f"{project_name}__poses__{rec}"):
            break

    splits = pd.split('__')
    poses_file_name = f"{splits[0]}_{splits[-1]}.poses"
    poses_file_path = f"{input_dir}/poses/{pd}/{poses_file_name}"

    if Path(poses_file_path).exists():
        return poses_file_path
    else:
        print(f"Poses file unavailable for recording {rec}")
        return None


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

    poses_file = get_poses_file_path_for_this_rec(input_dir, rec)
    img_seq_from_poses = get_image_seq_from_poses_file(poses_file)

    seq_in_dirs = {}
    for c in cams:
        dir_to_check = f"{input_dir}/images/{rec}/{c}"
        images = os.listdir(dir_to_check)
        seq = []

        #! Extract only sequence number from the image name
        for i in images:
            seq.append(i.split('.')[1])

        seq.sort()
        seq_in_dirs[c] = seq

    # filetred_poses = []
    #! For each sequence number we get from poses file
    for pose_seq in img_seq_from_poses:
        available = 1
        #! Check this seq inside each camera
        for c in cams:
            if pose_seq not in seq_in_dirs[c]:
                # print(f"{pose_seq} not available in cam {c}")
                available = 0
                break
        if available:
            # filetred_poses.append(pose_seq)
            f.write(pose_seq)
            f.write('\n')

    f.close()


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


def generate_pgftojpg_commands_all(input_dir, output_dir, r_and_c, path_to_converter):
    """
    Generate pgftojpg commands for each recordings and store them in a text file.
    The text file is saved under output_dir/intermediate/pgf2jpg_{rec}.txt

    Parameters
    ----------

    Returns
    -------

    """
    #! For each recording:
    for r,c in r_and_c.items():

        #! Get the seq from filtred_{rec}.txt file
        filtered_filepath = f"{output_dir}/intermediate/filtered_{r}.txt"
        if not Path(filtered_filepath).exists():
            print(filtered_filepath, "doesn't exists") 
            continue
        else:
            seq = get_list_from_filtered_images_file(filtered_filepath)

        #TODO Scan and prepare the list of cameras which has PGF images
        cam_pgf = ['00', '01', '02', '03', '04', '05', '06', '07']

        #! Open file to store the commands
        output_filepath = f"{output_dir}/intermediate/pgf2jpg_{r}.txt"
        f = open(output_filepath, "w")

        #! For each camera with pgf images:
        for c_pgf in cam_pgf:
            for s in seq:
                cmd = f"{path_to_converter} {input_dir}/images/{r}/{c_pgf}/image.{s}.pgf {output_dir}/images/{r}/{c_pgf}/image/{s}.jpg"
                f.write(cmd)
                f.write('\n')

        #! Close the file
        f.close()


