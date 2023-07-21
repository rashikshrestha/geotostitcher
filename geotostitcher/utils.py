import os
from os.path import exists
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

        #! Build dirs for 360 and 360high
        dir360 = Path(output_dir+'/images/'+r+'/360')
        dir360low = Path(output_dir+'/images/'+r+'/360high')
        dir360.mkdir(parents=True, exist_ok=True)
        dir360low.mkdir(parents=True, exist_ok=True)

    #! Build intermediate dir
    intermediate_dir = Path(output_dir+'/intermediate')
    intermediate_dir.mkdir(parents=True, exist_ok=True)

    #! Build dirs for pts files
    for r,cams in rec_and_cams.items():
        pts_dir = Path(output_dir+'/intermediate/pts/'+r)
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

        #! Check dirs for 360 and 360low
        dir360 = Path(output_dir+'/images/'+r+'/360')
        success = check_dir(dir360) and success
        dir360low = Path(output_dir+'/images/'+r+'/360high')
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
    print(img_seq_from_poses)

    #TODO Here I have set the camera names explicitely
    #TODO But the number/names of cameras might vary in future!
    #TODO No, make this flexible!!
    #Here, top_cams = cams with pgf images and doesn't participate in panaroma generation
    #      bottom_cams = cams with jpg images and participates in panaroma creation
    top_cams = ['00','01','02','03','04','05','06','07']
    bottom_cams = ['08', '09', '10', '11', '12', '13']

    #! Check if the file correspondig to given seq number exists in the expected directories:
    for seq in img_seq_from_poses:
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
            f.write(seq)
            f.write('\n')

    f.close()
    print(f"Filter Images completed for rec {rec}")


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
    for s in seq:
        output_file = f"{output_dir}/intermediate/pts/{r}/image.{s}.pts"
        f = open(output_file, "w")


        #! Read the template file
        with open(template_path, "r") as file:
            for line_number, line in enumerate(file, start=1):  

                #! For each line in template:
                if word in line:
                    # print(f"Word '{word}' found on line {line_number}")
                    splits = line.split('$$$')
                    new_line_list = []
                    #! For each word in the line:
                    for w in splits:
                        if w == 'output_file_path':
                            w = f"{output_dir}/images/{r}/360high/image.{s}.jpg"
                        elif w == 'output_jpg_quality':
                            w = '70' #TODO Get jpg quality from some config or as parameters
                        elif w.startswith('image_from_camera'):
                            # print(w.split('_'))
                            # input()
                            camera = w.split('_')[-1]
                            # print(camera)
                            # input()
                            w = f"{output_dir}/images/{r}/{camera}/image.{s}.jpg"
                            # print(w)
                            # input()

                        new_line_list.append(w)


                    new_line = ''.join(new_line_list)

                    f.write(new_line)

                else:
                    f.write(line)

        print(f"Generated pts file for sequence {s} of recording {r}")

    generate_batch_files(output_dir, r)



    




