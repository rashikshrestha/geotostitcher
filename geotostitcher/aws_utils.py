import s3fs
import boto3

s3_fs = s3fs.S3FileSystem()
s3_client = boto3.client('s3')

def s3_ls(path, full_path=False):
    """
    List the files of the dir
    """
    files = s3_fs.ls(path)

    if full_path:
        return files
    else:
        only_files = []
        for f in files:
            only_files.append(f.rsplit('/',1)[-1])
        return only_files
    

def s3_count_files(path):
    """
    Count Number of files in the given path
    """
    return len(s3_ls(path, full_path=True))


def get_s3_object(path):
    bucket_name, key = path.split('/', 1)

    #! Get the file inside the S3 Bucket
    try:
        s3_response = s3_client.get_object(
            Bucket=bucket_name,
            Key=key
        )

    #! If S3 Bucket does not exist
    except s3_client.exceptions.NoSuchBucket as e:
        print(f"For path: {path}")
        print('The S3 bucket does not exist.')
        print(e)
        return None

    #! Object does not exist in the S3 Bucket
    except s3_client.exceptions.NoSuchKey as e:
        print(f"For path: {path}")
        print('The S3 objects does not exist in the S3 bucket.')
        print(e)
        return None
    
    return s3_response

    
def read_txt_file(path):
    """
    Read text file and returns its contents as String
    """
    s3_obj = get_s3_object(path)
    if s3_obj:
        s3_object_body = s3_obj.get('Body')
        content_str = s3_object_body.read().decode()
        return content_str
    else:
        return None


def s3_download(s3_path, local_path):
    """
    Download a file from s3
    """
    try:
        s3_fs.download(s3_path, local_path)
    except Exception as e: 
        print(f"Error getting file: {s3_path}")
        print(e)
        return False
    return True


def s3_upload(local_path, s3_path):
    """
    Upload a file to s3
    """
    try:
        s3_fs.upload(local_path, s3_path)
    except Exception as e: 
        print(f"Error uploading file: {local_path} to {s3_path}")
        print(e)
        return False
    return True


def s3_rm(path):
    """
    Delete a file in s3    
    """
    bucket_name, key = path.split('/', 1)

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=key)
    except Exception as e: 
        print(f"Error deleting file: {path}")
        print(e)
        return False
    return True


def s3_mv(s3_path_1, s3_path_2):
    """
    Download a file from s3
    """
    try:
        s3_fs.mv(s3_path_1, s3_path_2)
    except Exception as e: 
        print(f"Error moving file")
        print(e)
        return False
    return True


def s3_exists(path):
    """
    Check it the path exists in s3
    """
    bucket_name, key = path.split('/', 1)

    #! Get the file object
    try:
        s3_response = s3_client.get_object(
            Bucket=bucket_name,
            Key=key
        )

    #! If S3 Bucket does not exist
    except:
        return False

    return True