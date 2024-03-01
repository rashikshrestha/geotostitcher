import geotostitcher.utils as utils
from geotostitcher.executer import Executer
import subprocess
import os
import time

class Stitcher():
    def __init__(self) -> None:
        self.main_dir = f"/home/leon/rashik/s16/360_process"
        self.input_dir = None
        self.output_dir = None
        self.config_file = None
        self.project_name = None
        self.rec_num = None
        self.exe = Executer()
        self.recs = None


    def get_projects(self):
        self.prj_all = utils.list_prj(self.main_dir)

    def select_recordings(self):
        #! Get project name
        # self.project_name = utils.get_project_name_from_input_dir(self.input_dir)
        # print(f"Project: {self.project_name}")

        #! Get recordings and cameras
        self.r_and_c_all = utils.get_recordings_and_cameras(self.input_dir)
        self.recs_all = list(self.r_and_c_all.keys())

        self.r_and_c = self.r_and_c_all
        # self.recs = self.recs_all

    def update_recs_to_execute(self, new_recs):
        self.recs = new_recs

        new_r_and_c = {}     
        for r in self.recs:
            new_r_and_c[r] = self.r_and_c_all[r]

        self.r_and_c = new_r_and_c

        print('Choosen Ones:')
        print(self.recs)
        print(self.r_and_c)


    def preprocess(self):
        #! Make Output dirs
        utils.build_output_dirs(self.r_and_c, self.output_dir)

        #! Verify that output dirs structure is good
        out_dir_ok = utils.verify_output_dirs(self.r_and_c, self.output_dir)
        print(f"Output dirs status = {out_dir_ok}")

        #! Generate filetred images list
        utils.generate_filtered_images_list_forall(self.input_dir, self.output_dir, self.r_and_c)

        #! Generate pgf to jpg commands
        utils.generate_pgftojpg_commands_all(self.input_dir, self.output_dir, self.r_and_c)

        #! Generate Move JPG commands
        utils.generate_movejpg_commands_all(self.input_dir, self.output_dir, self.r_and_c)

        #! Generate Stitch 360 commands
        # utils.generate_stitch_commands_all(self.output_dir, self.recs, self.config_file)

        #! Generate Stitch 360low commands
        utils.generate_360low_commands_all(self.output_dir, self.recs)

        #! Generate Upload commands
        utils.generate_upload_commands_all(self.output_dir, self.recs, self.project_name)

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

    def process_360low(self, rec, no_of_threads):
        """
        
        Parameters
        ----------
        no_of_threads: int
            No of Threads to run
        """
        execution_file = utils.get_commands_file(self.output_dir, '360low', rec)
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

    def generate_pts(self, rec, template_path):
        """
        Generate PTS files
        
        """
        utils.generate_pts_files(self.output_dir, rec, template_path)

    def stitch_360high(self, rec):
        """
        Stitch 360 low using PTGui
        """
        #! Start PTGui
        command = f"/opt/ptgui/PTGui -stitchnogui {self.output_dir}/intermediate/pts/{rec}_batch.ptgbatch"
        os.system(command)
        # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

        time.sleep(1)

    def get_stitch_360high_status(self):
        """
        Check PTGui Status
        """
        command = "pgrep PTGui"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        if len(output) == 0:
            return True
        else:
            return False


    def upload_pgf(self, rec, no_of_threads):
        execution_file = utils.get_commands_file(self.output_dir, 'uploadpgf', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
        print(f"Started Upload PGF cams for rec {rec}. Please Wait ...")

    def upload_jpg(self, rec, no_of_threads):
        execution_file = utils.get_commands_file(self.output_dir, 'uploadjpg', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
        print(f"Started Upload JPG cams for rec {rec}. Please Wait ...")

    def upload_jpgblur(self, rec, no_of_threads):
        execution_file = utils.get_commands_file(self.output_dir, 'uploadjpgblur', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
        print(f"Started Upload JPG Blur cams for rec {rec}. Please Wait ...")

    def upload_360high(self, rec, no_of_threads):
        execution_file = utils.get_commands_file(self.output_dir, 'upload360high', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
        print(f"Started Upload 360high for rec {rec}. Please Wait ...")

    def upload_360low(self, rec, no_of_threads):
        execution_file = utils.get_commands_file(self.output_dir, 'upload360low', rec)
        self.exe.prepare_execution(execution_file, no_of_threads)
        self.exe.start()
        print(f"Started Upload 360low for rec {rec}. Please Wait ...")
