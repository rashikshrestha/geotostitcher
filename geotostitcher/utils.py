import os

def get_recordings(input_dir):
    '''
    Get the list of recordings
    
    Parameters
    ----------
    input_dir: str
        Path to input directory
        
    Returns
    -------
    recordings: list
        List of recording names
    '''
    images_dir = input_dir + '/images'
    recordings = os.listdir(images_dir)
    return recordings

def get_cameras(input_dir, rec):
    '''
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
    '''
    cams = os.listdir(f"{input_dir}/images/{rec}")
    return cams

def get_recordings_and_cameras(input_dir):
    '''
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
    '''
    pass

def build_output_dirs(rec_and_cams, output_dir):
    '''
    Build the output directory structure
    
    Parameters
    ----------
    rec_and_cams: dict
        Dictionary where key=rec_name and value=list of cameras for that recording
    output_dir: str
        Path to output dirctory

    Returns
    -------
    None 
    '''
    pass

def verify_output_dirs(rec_and_cams, output_dir):
    '''
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
    '''
    pass

def generate_filtered_images_list(rec, output_dir):
    '''
    Generate filtered images list for each recording and store the list in a text file.
    The text file is saved under output_dir/intermediate/{rec_name}_filtered.txt

    Parameters
    ----------
    rec: 

    output_dir: str
        Path to output dirctory

    Returns
    -------

    '''
    pass

def generate_pgftojpg_commands(path_to_converter, output_dir, input_dir):
    '''
    Generate pgftojpg commands for each recordings and store them in a text file.
    The text file is saved under output_dir/intermediate/{rec_name}_convert_commands.txt

    Parameters
    ----------

    Returns
    -------

    '''
    pass