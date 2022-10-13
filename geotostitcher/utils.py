import os
from pathlib import Path

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

def generate_filtered_images_list(rec, output_dir):
    """
    Generate filtered images list for each recording and store the list in a text file.
    The text file is saved under output_dir/intermediate/{rec_name}_filtered.txt

    Parameters
    ----------
    rec: 

    output_dir: str
        Path to output dirctory

    Returns
    -------

    """
    pass

def generate_pgftojpg_commands(path_to_converter, output_dir, input_dir):
    """
    Generate pgftojpg commands for each recordings and store them in a text file.
    The text file is saved under output_dir/intermediate/{rec_name}_convert_commands.txt

    Parameters
    ----------

    Returns
    -------

    """
    pass