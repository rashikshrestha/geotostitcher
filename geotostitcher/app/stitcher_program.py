import geotostitcher.utils as utils
from geotostitcher.executer import Executer

class Stitcher():
    def __init__(self) -> None:
        self.input_dir = None
        self.output_dir = None
        self.config_file = None
        self.exe = Executer()

    def preprocess(self):
        #! Get project name
        self.project_name = utils.get_project_name_from_input_dir(self.input_dir)
        print(f"Project: {self.project_name}")

        #! Get recordings and cameras
        self.r_and_c = utils.get_recordings_and_cameras(self.input_dir)
        self.recs = list(self.r_and_c.keys())

        #! Make Output dirs
        utils.build_output_dirs(self.r_and_c, self.output_dir)

        #! Verify that output dirs structure is good
        out_dir_ok = utils.verify_output_dirs(self.r_and_c, self.output_dir)
        print(f"Output dirs status = {out_dir_ok}")

        #! Generate filetred images list
        utils.generate_filtered_images_list_forall(self.input_dir, self.output_dir, self.r_and_c)

        #! Generate pgf to jpg commands
        utils.generate_pgftojpg_commands_all(self.input_dir, self.output_dir, self.r_and_c,
        '/home/rashik/workspace/geoautomation/geotostitcher/bin/pgf2jpg.dms')

        #! Generate Move JPG commands
        utils.generate_movejpg_commands_all(self.input_dir, self.output_dir, self.r_and_c)

        #! Generate Stitch 360 commands
        stitcher = '/home/rashik/workspace/geoautomation/geotostitcher/geotostitcher/simple_stitcher.py'
        utils.generate_stitch_commands_all(stitcher, self.output_dir, self.recs, self.config_file)

    def process_pgf(self, rec, no_of_threads):
        """
        
        Parameters
        ----------
        no_of_threads: int
            No of Threads to run
        """
        execution_file = utils.get_commands_file(self.output_dir, 'pgf2jpg', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()

    def process_jpg(self, rec, no_of_threads):
        """
        
        Parameters
        ----------
        no_of_threads: int
            No of Threads to run
        """
        execution_file = utils.get_commands_file(self.output_dir, 'movejpgs', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()

    def stitch_360(self, rec, no_of_threads):
        """
        
        Parameters
        ----------
        no_of_threads: int
            No of Threads to run
        """
        execution_file = utils.get_commands_file(self.output_dir, 'stitch', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
