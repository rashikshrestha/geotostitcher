import geotostitcher.utils as utils

ind = '/home/rashik/workspace/geoautomation/mrcsource-pave'
oud = '/home/rashik/workspace/geoautomation/mrcsource-pave-out'

#! Get project name
project_name = utils.get_project_name_from_input_dir(ind)
print(f"Project: {project_name}")

#! Get recordings and cameras
r_and_c = utils.get_recordings_and_cameras(ind)
print(r_and_c)
recs = list(r_and_c.keys())

#! Make Output dirs
utils.build_output_dirs(r_and_c, oud)

#! Verify that output dirs structure is good
out_dir_ok = utils.verify_output_dirs(r_and_c, oud)
print(f"Output dirs status = {out_dir_ok}")

#! Get poses file path of this rec
# poses_path = utils.get_poses_file_path_for_this_rec(ind, recs[0])
# print(poses_path)

#! Get image seq from poses file
# img_seq = utils.get_image_seq_from_poses_file(poses_path)

#! Generate Filtered images list
utils.generate_filtered_images_list_forall(ind, oud, r_and_c)

utils.generate_pgftojpg_commands_all(ind, oud, r_and_c,
'/home/rashik/workspace/geoautomation/geotostitcher/bin/pgf2jpg.dms')

utils.generate_movejpg_commands_all(ind, oud, r_and_c)

stitcher = '/home/rashik/workspace/geoautomation/geotostitcher/geotostitcher/simple_stitcher.py'
cfg_file = '/home/rashik/workspace/geoautomation/geotostitcher/scripts/stitch_config.yaml'
utils.generate_stitch_commands_all(stitcher, oud, recs, cfg_file)
