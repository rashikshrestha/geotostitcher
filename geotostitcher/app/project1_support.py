#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Oct 15, 2022 02:17:30 PM +0545  platform: Linux
#    Oct 15, 2022 02:20:23 PM +0545  platform: Linux
#    Oct 15, 2022 02:57:27 PM +0545  platform: Linux
#    Oct 15, 2022 03:00:37 PM +0545  platform: Linux
#    Oct 18, 2022 02:14:44 PM +0545  platform: Linux
#    Oct 19, 2022 02:28:20 PM +0545  platform: Linux
#    Oct 19, 2022 03:32:59 PM +0545  platform: Linux
#    Jul 22, 2023 11:40:59 PM +0545  platform: Linux
#    Jul 23, 2023 12:17:43 AM +0545  platform: Linux
#    Jul 23, 2023 01:25:18 AM +0545  platform: Linux
#    Jul 23, 2023 10:51:29 AM EET  platform: Linux
#    Jul 24, 2023 04:56:43 AM EET  platform: Linux
#    Jul 24, 2023 05:23:23 AM EET  platform: Linux
#    Jul 24, 2023 06:47:10 AM EET  platform: Linux
#    Jul 24, 2023 07:23:13 AM EET  platform: Linux
#    Jul 24, 2023 08:09:51 AM EET  platform: Linux
#    Feb 05, 2024 08:39:24 AM +0545  platform: Linux
#    Mar 01, 2024 07:30:42 AM +0545  platform: Linux
#    Mar 01, 2024 11:36:33 AM +0545  platform: Linux
#    Mar 01, 2024 12:14:24 PM +0545  platform: Linux

import sys
import time
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter.constants import *

from stitcher_program import Stitcher
import project1

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)

    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = project1.geoto_stitcher(_top1)

    # _w1.pts_template.insert(0, '/home/leon/rashik/pts_templates/kona2-12mp.pts')

    # Backbone
    global stitcher
    stitcher = Stitcher() 

    # Main loop

    root.mainloop()

def auto_fill(*args):
    print('project1_support.auto_fill')
    global stitcher, _w1

    #! Stuffs to fill automatically
    input_dir = '/media/leon/BLUE/calibration_room/calibration'
    output_dir = '/media/leon/BLUE/calibration_room/calibration-out'
    config_file = '/media/leon/BLUE/calibration_room/config.yaml'
    template_path = '/media/leon/BLUE/calibration_room/template.pts'

    #! Add texts to the Entries
    _w1.input_dir.insert(0, input_dir)
    _w1.output_dir.insert(0, output_dir)
    _w1.config_file.insert(0, config_file)
    _w1.pts_template.insert(0, template_path)
    

def close_program(*args):
    print('project1_support.close_program')
    global _top1
    _top1.destroy()

def select_config_file(*args):
    print('project1_support.select_config_file')
    global stitcher, _w1
    file_path = filedialog.askopenfilename()
    _w1.config_file.insert(0, file_path)

def select_input_dir(*args):
    print('project1_support.select_input_dir')
    global stitcher, _w1
    dir = filedialog.askdirectory()
    _w1.input_dir.insert(0, dir)

def select_output_dir(*args):
    print('project1_support.select_output_dir')
    global stitcher, _w1
    dir = filedialog.askdirectory()
    _w1.output_dir.insert(0, dir)

def start_preprocess(*args):
    print('Preprocessing ...')
    
    stitcher.preprocess()
    # _w1.no_of_rec['text'] = len(stitcher.recs)
    # _w1.project_name['text'] = stitcher.project_name

def start_process_jpg(*args):
    print('Processing JPG ...')
    global stitcher, _w1, root
    threads = int(_w1.jpg_threads.get())

    recordings = stitcher.recs

    for rec in recordings:
        _w1.process_jpg_rec['text'] = rec
        stitcher.process_jpg(rec, threads)
        total = stitcher.exe.total_commands
    
        done = False
        while not done:
            percent, count, done = stitcher.exe.get_progress()
            _w1.process_jpg['value'] = percent
            _w1.process_jpg_status['text'] = f"{count}/{total}"
            root.update_idletasks()
            root.update()
            time.sleep(0.05)
    
    print("Finish JPG")

def start_process_pgf(*args):
    print('Processing PGF ...')
    global stitcher, _w1, root
    threads = int(_w1.pgf_threads.get())

    recordings = stitcher.recs

    for rec in recordings:
        _w1.process_pgf_rec['text'] = rec
        stitcher.process_pgf(rec, threads)
        total = stitcher.exe.total_commands
    
        done = False
        while not done:
            percent, count, done = stitcher.exe.get_progress()
            _w1.process_pgf['value'] = percent
            _w1.process_pgf_status['text'] = f"{count}/{total}"
            root.update_idletasks()
            root.update()
            time.sleep(0.05)
    
    print("Finish PGF")

def start_stitch_360(*args):
    print('Unavailable Now')

    # global stitcher, _w1, root
    # threads = int(_w1.stitch_360_threads.get())

    # recordings = stitcher.recs

    # for rec in recordings:
    #     _w1.stitch_360_rec['text'] = rec
    #     stitcher.stitch_360(rec, threads)
    #     total = stitcher.exe.total_commands
    
    #     done = False
    #     while not done:
    #         percent, count, done = stitcher.exe.get_progress()
    #         _w1.stitch_360['value'] = percent
    #         _w1.stitch_360_status['text'] = f"{count}/{total}"
    #         root.update_idletasks()
    #         root.update()
    #         time.sleep(0.05)
    
    # print("Finish Stitch 360")

def select_all_rec(*args):
    print('project1_support.select_all_rec')
    global list_of_checks
    for check in list_of_checks:
        check.select()

def unselect_all_rec(*args):
    print('project1_support.unselect_all_rec')
    global list_of_checks
    for check in list_of_checks:
        check.deselect()

def close_select_rec(*args):
    global _top2, check_var, stitcher, _w1

    stitcher.recs = [check_var.get()]
    _w1.rec_num['text'] = stitcher.recs[0]

    stitcher.update_recs_to_execute(stitcher.recs)

    _top2.destroy()

def add_proj_as_radio(holder, prj_all):
    # global list_of_prj_radio_btn, list_of_prj_radio_var
    global prj_var

    list_of_prj_radio_btn = []
    # list_of_prj_radio_var = []

    prj_var = tk.StringVar()

    y = 0.1
    for i in range(len(prj_all)):

        cb = tk.Radiobutton(holder)

        cb.place(relx=0.018, rely=y+i*0.075, relheight=0.073, relwidth=0.7, bordermode='ignore')
        cb.configure(activebackground="beige")
        cb.configure(anchor='w')
        cb.configure(compound='left')
        cb.configure(justify='left')
        cb.configure(selectcolor="#d9d9d9")
        cb.configure(text=prj_all[i])
        cb.configure(value=prj_all[i])
        cb.configure(variable=prj_var)

        # list_of_prj_radio_var.append(tkvar)
        list_of_prj_radio_btn.append(cb)

    list_of_prj_radio_btn[0].select() # Select first radio button

def add_rec_as_radio(holder, rec_all):
    global check_var

    print(f"Total {len(rec_all)} recordings available!")

    list_of_checks = []

    check_var = tk.StringVar()
    y = 0.03
    x = 0.018
    x_skip = 0.194
    y_skip = 0.045
    for i in range(len(rec_all)):
        if i%20==0: y=0.03

        cb = tk.Radiobutton(holder)

        cb.place(relx=x+(i//20)*x_skip, rely=y, relheight=0.073
                , relwidth=0.193, bordermode='ignore')
        cb.configure(activebackground="beige")
        cb.configure(anchor='w')
        cb.configure(compound='left')
        cb.configure(justify='left')
        cb.configure(selectcolor="#d9d9d9")
        cb.configure(text=rec_all[i])
        cb.configure(value=rec_all[i])
        cb.configure(variable=check_var)

        list_of_checks.append(cb)

        y += y_skip

    list_of_checks[0].select()

    

# def select_rec(*args):
#     print('project1_support.select_rec')
#     global stitcher, _w1

#     #! Get the input_dir, output_dir and config_file form GUI
#     stitcher.input_dir = _w1.input_dir.get()
#     stitcher.output_dir = _w1.output_dir.get()
#     stitcher.config_file = _w1.config_file.get()

#     #! Run select_rec of Stitcher
#     stitcher.select_recordings()

#     #! Creates a toplevel widget "Select Recording"
#     global _top2, _w2
#     _top2 = tk.Toplevel(root)
#     _w2 = project1.select_rec(_top2)

#     add_rec_as_checklist(_w2.recordings, stitcher.recs, stitcher.recs_all)

def select_template(*args):
    print('project1_support.select_template')
    global stitcher, _w1
    file_path = filedialog.askopenfilename()
    _w1.pts_template.insert(0, file_path)

def generate_pts(*args):
    print('\nGenerating PTS ..')
    global stitcher, _w1
    #! Get template path from GUI
    template_path = _w1.pts_template.get()

    recordings = stitcher.recs

    for rec in recordings:
        stitcher.generate_pts(rec, template_path)

def select_project(*args):
    print("Select Project")

    global stitcher, _w1
    disk = _w1.selectedButton.get()

    # Creates a toplevel widget.
    global _top3, _w3
    _top3 = tk.Toplevel(root)
    _w3 = project1.project(_top3)

    print(stitcher.get_projects())

    add_proj_as_radio(_w3.projects, stitcher.prj_all)

def select_recording(*args):
    print('Select Recording')
    global stitcher, _w1

    #! Run select_rec of Stitcher
    stitcher.select_recordings()

    #! Creates a toplevel widget "Select Recording"
    global _top2, _w2
    _top2 = tk.Toplevel(root)
    _w2 = project1.select_rec(_top2)

    add_rec_as_radio(_w2.recordings, stitcher.recs_all)

def select_s16(*args):
    print("Select s16")
    stitcher.main_dir = f"/home/leon/rashik/s16/360_process"
    print(f"Main dir: {stitcher.main_dir}")

def select_s17(*args):
    print("Select s17")
    stitcher.main_dir = f"/home/leon/rashik/s17/360_process"
    print(f"Main dir: {stitcher.main_dir}")

def select_s18(*args):
    print("Select s18")
    stitcher.main_dir = f"/home/leon/rashik/s18/360_process"
    print(f"Main dir: {stitcher.main_dir}")

def select_s17e(*args):
    print("Select s17e")
    stitcher.main_dir = f"/home/leon/rashik/s17e/360_process"
    print(f"Main dir: {stitcher.main_dir}")

def select_s18g(*args):
    print("Select s18g")
    stitcher.main_dir = f"/home/leon/rashik/s18g/360_process"
    print(f"Main dir: {stitcher.main_dir}")

def close_select_prj(*args):
    global _top3, prj_var, stitcher, _w1

    stitcher.project_name = prj_var.get()
    stitcher.input_dir = f"{stitcher.main_dir}/{prj_var.get()}"
    stitcher.output_dir = f"{stitcher.main_dir}/{prj_var.get()}-out"

    print(f"{stitcher.input_dir}")
    print(f"{stitcher.output_dir}")

    _w1.project_name['text'] = stitcher.project_name

    _top3.destroy()

def start_stitch_360low(*args):
    print('Processing 360low ...')
    global stitcher, _w1, root
    threads = int(_w1.stitch_360low_threads.get())

    # print(threads)

    recordings = stitcher.recs

    for rec in recordings:
        _w1.stitch_360low_rec['text'] = rec
        stitcher.process_360low(rec, threads)
        total = stitcher.exe.total_commands

    
        done = False
        while not done:
            percent, count, done = stitcher.exe.get_progress()
            _w1.process_stitch_360low['value'] = percent
            _w1.stitch_360low_status['text'] = f"{count}/{total}"
            root.update_idletasks()
            root.update()
            time.sleep(0.05)
    
    print("Finish processing 360low")

def start_stitch_360high(*args):
    print('Stitching 360high ...')

    recordings = stitcher.recs

    for rec in recordings:
        stitcher.stitch_360high(rec)

        done = False
        while not done:
            done = stitcher.get_stitch_360high_status()
            root.update_idletasks()
            root.update()
            time.sleep(0.05)

        print(f"Completed stitching 360high for rec {rec}")

def count_avail_pgf_cams(avail_cams):
    total_pgf_cams = ['00', '01', '02', '03', '04', '05', '06', '07']
    count = 0
    for c in total_pgf_cams:
        if c in avail_cams:
            count += 1
    return count

def upload_pgf(*args):
    recordings = stitcher.recs
    for rec in recordings:
        no_of_cams = count_avail_pgf_cams(stitcher.r_and_c[rec])
        stitcher.upload_pgf(rec, no_of_cams)

def upload_jpg(*args):
    recordings = stitcher.recs
    for rec in recordings:
        stitcher.upload_jpg(rec, 6)

def upload_jpgblur(*args):
    recordings = stitcher.recs
    for rec in recordings:
        stitcher.upload_jpgblur(rec, 6)

def upload_360high(*args):
    recordings = stitcher.recs
    for rec in recordings:
        stitcher.upload_360high(rec, 1)

def upload_360low(*args):
    recordings = stitcher.recs
    for rec in recordings:
        stitcher.upload_360low(rec, 1)

def download_recon(*args):
    recordings = stitcher.recs
    for rec in recordings:
        stitcher.download_recon(rec, 1)

def start_blurring(*args):
    print('Blurring ...')
    global stitcher, _w1, root
    threads = int(_w1.blur_threads.get())

    recordings = stitcher.recs

    for rec in recordings:
        _w1.blurring_rec['text'] = rec
        stitcher.blurring(rec, threads)
        total = stitcher.exe.total_commands
    
        done = False
        while not done:
            percent, count, done = stitcher.exe.get_progress()
            _w1.blurring['value'] = percent
            _w1.blurring_status['text'] = f"{count}/{total}"
            root.update_idletasks()
            root.update()
            time.sleep(0.05)
    
    print("Finish Blurring")

import os

def upload_pts(*args):
    print('project1_support.upload_pts')
    global _w1, root

    prj = _w1.project_name['text']
    rec = _w1.rec_num['text']
    pts_template_local = _w1.pts_template.get()
    pts_template_big_local = _w1.pts_template_big.get()

    # extract names
    pts_small_name = pts_template_local.split('/')[-1]
    pts_big_name = pts_template_big_local.split('/')[-1]

    print(prj, rec, pts_template_local, pts_template_big_local)

    command1 = f"aws s3 cp {pts_template_local} s3://geoto-projects-prod/{prj}/ptgui/{rec}/{pts_small_name}.standard"
    command2 = f"aws s3 cp {pts_template_big_local} s3://geoto-projects-prod/{prj}/ptgui/{rec}/{pts_big_name}"

    path_split = pts_template_local.split('/')[:-1]
    path_split.append('2724_black.jpg')
    black_path = '/'.join(path_split)

    command3 = f"aws s3 cp {black_path} s3://geoto-projects-prod/{prj}/ptgui/{rec}/image.{rec}000000_0.jpg"

    os.system(command1)  
    os.system(command2)
    os.system(command3)

    print('Done uploading PTS!')


def select_template_big(*args):
    print('project1_support.select_template_big')
    global stitcher, _w1
    file_path = filedialog.askopenfilename()
    _w1.pts_template_big.insert(0, file_path)

if __name__ == '__main__':
    project1.start_up()





