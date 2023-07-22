#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Jul 22, 2023 09:35:51 PM EET  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import project1_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class geoto_stitcher:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("726x827+688+125")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("GeoTo Stitcher")
        top.configure(highlightcolor="black")

        self.top = top
        self.selectedButton = tk.IntVar()

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        _style_code()
        self.configs_block = ttk.Labelframe(self.top)
        self.configs_block.place(relx=0.028, rely=0.012, relheight=0.163
                , relwidth=0.942)
        self.configs_block.configure(relief='')
        self.configs_block.configure(text='''Configs''')
        self.Label1_1 = tk.Label(self.configs_block)
        self.Label1_1.place(relx=0.287, rely=1.481, height=23, width=77
                , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(text='''Input Dir''')
        self.select_project = tk.Button(self.configs_block)
        self.select_project.place(relx=0.278, rely=0.222, height=33, width=133
                , bordermode='ignore')
        self.select_project.configure(activebackground="beige")
        self.select_project.configure(borderwidth="2")
        self.select_project.configure(command=project1_support.select_project)
        self.select_project.configure(compound='left')
        self.select_project.configure(text='''Select Project''')
        self.select_recording = tk.Button(self.configs_block)
        self.select_recording.place(relx=0.281, rely=0.607, height=33, width=133
                , bordermode='ignore')
        self.select_recording.configure(activebackground="beige")
        self.select_recording.configure(borderwidth="2")
        self.select_recording.configure(command=project1_support.select_recording)
        self.select_recording.configure(compound='left')
        self.select_recording.configure(text='''Select Recording''')
        self.select_s17 = tk.Radiobutton(self.configs_block)
        self.select_s17.place(relx=0.088, rely=0.437, relheight=0.17
                , relwidth=0.099, bordermode='ignore')
        self.select_s17.configure(activebackground="beige")
        self.select_s17.configure(anchor='w')
        self.select_s17.configure(command=project1_support.select_s17)
        self.select_s17.configure(compound='left')
        self.select_s17.configure(justify='left')
        self.select_s17.configure(selectcolor="#d9d9d9")
        self.select_s17.configure(text='''s17''')
        self.select_s17.configure(value='0')
        self.select_s17.configure(variable=self.selectedButton)
        self.select_s18 = tk.Radiobutton(self.configs_block)
        self.select_s18.place(relx=0.088, rely=0.578, relheight=0.17
                , relwidth=0.098, bordermode='ignore')
        self.select_s18.configure(activebackground="beige")
        self.select_s18.configure(anchor='w')
        self.select_s18.configure(command=project1_support.select_s18)
        self.select_s18.configure(compound='left')
        self.select_s18.configure(justify='left')
        self.select_s18.configure(selectcolor="#d9d9d9")
        self.select_s18.configure(text='''s18''')
        self.select_s18.configure(value='1')
        self.select_s18.configure(variable=self.selectedButton)
        self.Label4_1_1 = tk.Label(self.configs_block)
        self.Label4_1_1.place(relx=0.629, rely=0.222, height=18, width=69
                , bordermode='ignore')
        self.Label4_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1.configure(anchor='w')
        self.Label4_1_1.configure(compound='left')
        self.Label4_1_1.configure(text='''Project:''')
        self.project_name = tk.Label(self.configs_block)
        self.project_name.place(relx=0.746, rely=0.222, height=17, width=110
                , bordermode='ignore')
        self.project_name.configure(activebackground="#f9f9f9")
        self.project_name.configure(anchor='w')
        self.project_name.configure(compound='left')
        self.project_name.configure(text='''Unknown''')
        self.Label4_2 = tk.Label(self.configs_block)
        self.Label4_2.place(relx=0.629, rely=0.519, height=26, width=80
                , bordermode='ignore')
        self.Label4_2.configure(activebackground="#f9f9f9")
        self.Label4_2.configure(anchor='w')
        self.Label4_2.configure(compound='left')
        self.Label4_2.configure(text='''Recording:''')
        self.rec_num = tk.Label(self.configs_block)
        self.rec_num.place(relx=0.759, rely=0.548, height=16, width=59
                , bordermode='ignore')
        self.rec_num.configure(activebackground="#f9f9f9")
        self.rec_num.configure(anchor='w')
        self.rec_num.configure(compound='left')
        self.rec_num.configure(text='''0''')
        self.Label1 = tk.Label(self.configs_block)
        self.Label1.place(relx=0.076, rely=0.267, height=21, width=78
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Select Disk''')
        self.preprocess_block = tk.LabelFrame(self.top)
        self.preprocess_block.place(relx=0.028, rely=0.187, relheight=0.105
                , relwidth=0.945)
        self.preprocess_block.configure(relief='groove')
        self.preprocess_block.configure(text='''Pre Process''')
        self.start_preprocess = ttk.Button(self.preprocess_block)
        self.start_preprocess.place(relx=0.073, rely=0.345, height=31, width=80
                , bordermode='ignore')
        self.start_preprocess.configure(command=project1_support.start_preprocess)
        self.start_preprocess.configure(takefocus="")
        self.start_preprocess.configure(text='''Start''')
        self.start_preprocess.configure(compound='left')
        self.process_pgf_block = tk.LabelFrame(self.top)
        self.process_pgf_block.place(relx=0.028, rely=0.3, relheight=0.143
                , relwidth=0.945)
        self.process_pgf_block.configure(relief='groove')
        self.process_pgf_block.configure(text='''Process PGF''')
        self.process_pgf = ttk.Progressbar(self.process_pgf_block)
        self.process_pgf.place(relx=0.554, rely=0.254, relwidth=0.41
                , relheight=0.0, height=19, bordermode='ignore')
        self.process_pgf.configure(length="281")
        self.start_process_pgf = ttk.Button(self.process_pgf_block)
        self.start_process_pgf.place(relx=0.073, rely=0.585, height=31, width=80
                , bordermode='ignore')
        self.start_process_pgf.configure(command=project1_support.start_process_pgf)
        self.start_process_pgf.configure(takefocus="")
        self.start_process_pgf.configure(text='''Start''')
        self.start_process_pgf.configure(compound='left')
        self.Label5 = tk.Label(self.process_pgf_block)
        self.Label5.place(relx=0.633, rely=0.458, height=23, width=109
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(compound='left')
        self.Label5.configure(text='''Recording:''')
        self.process_pgf_rec = tk.Label(self.process_pgf_block)
        self.process_pgf_rec.place(relx=0.783, rely=0.458, height=23, width=69
                , bordermode='ignore')
        self.process_pgf_rec.configure(activebackground="#f9f9f9")
        self.process_pgf_rec.configure(anchor='w')
        self.process_pgf_rec.configure(compound='left')
        self.process_pgf_rec.configure(text='''0''')
        self.Label7 = tk.Label(self.process_pgf_block)
        self.Label7.place(relx=0.624, rely=0.678, height=24, width=70
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(text='''Status:''')
        self.process_pgf_status = tk.Label(self.process_pgf_block)
        self.process_pgf_status.place(relx=0.72, rely=0.678, height=24, width=149
                , bordermode='ignore')
        self.process_pgf_status.configure(activebackground="#f9f9f9")
        self.process_pgf_status.configure(anchor='w')
        self.process_pgf_status.configure(compound='left')
        self.process_pgf_status.configure(text='''None''')
        self.pgf_threads = tk.Spinbox(self.process_pgf_block, from_=1.0, to=100.0)
        self.pgf_threads.place(relx=0.219, rely=0.254, relheight=0.212
                , relwidth=0.118, bordermode='ignore')
        self.pgf_threads.configure(activebackground="#f9f9f9")
        self.pgf_threads.configure(background="white")
        self.pgf_threads.configure(font="TkDefaultFont")
        self.pgf_threads.configure(highlightbackground="black")
        self.pgf_threads.configure(selectbackground="#c4c4c4")
        self.value_list = ['5',]
        self.pgf_threads.configure(values=self.value_list)
        self.pgf_label = tk.Label(self.process_pgf_block)
        self.pgf_label.place(relx=0.029, rely=0.254, height=29, width=130
                , bordermode='ignore')
        self.pgf_label.configure(activebackground="#f9f9f9")
        self.pgf_label.configure(anchor='w')
        self.pgf_label.configure(compound='left')
        self.pgf_label.configure(text='''No of Threads''')
        self.auto_fill = ttk.Button(self.top)
        self.auto_fill.place(relx=0.853, rely=0.937, height=31, width=80)
        self.auto_fill.configure(command=project1_support.auto_fill)
        self.auto_fill.configure(takefocus="")
        self.auto_fill.configure(text='''Auto Fill''')
        self.auto_fill.configure(compound='left')
        self.process_jpg_block = tk.LabelFrame(self.top)
        self.process_jpg_block.place(relx=0.028, rely=0.447, relheight=0.14
                , relwidth=0.945)
        self.process_jpg_block.configure(relief='groove')
        self.process_jpg_block.configure(text='''Process JPG''')
        self.process_jpg = ttk.Progressbar(self.process_jpg_block)
        self.process_jpg.place(relx=0.554, rely=0.25, relwidth=0.41
                , relheight=0.0, height=19, bordermode='ignore')
        self.process_jpg.configure(length="281")
        self.start_process_jpg = ttk.Button(self.process_jpg_block)
        self.start_process_jpg.place(relx=0.073, rely=0.586, height=31, width=80
                , bordermode='ignore')
        self.start_process_jpg.configure(command=project1_support.start_process_jpg)
        self.start_process_jpg.configure(takefocus="")
        self.start_process_jpg.configure(text='''Start''')
        self.start_process_jpg.configure(compound='left')
        self.Label5_2 = tk.Label(self.process_jpg_block)
        self.Label5_2.place(relx=0.633, rely=0.457, height=23, width=109
                , bordermode='ignore')
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(anchor='w')
        self.Label5_2.configure(compound='left')
        self.Label5_2.configure(text='''Recording:''')
        self.process_jpg_rec = tk.Label(self.process_jpg_block)
        self.process_jpg_rec.place(relx=0.783, rely=0.457, height=23, width=69
                , bordermode='ignore')
        self.process_jpg_rec.configure(activebackground="#f9f9f9")
        self.process_jpg_rec.configure(anchor='w')
        self.process_jpg_rec.configure(compound='left')
        self.process_jpg_rec.configure(text='''0''')
        self.Label7_2 = tk.Label(self.process_jpg_block)
        self.Label7_2.place(relx=0.624, rely=0.681, height=23, width=70
                , bordermode='ignore')
        self.Label7_2.configure(activebackground="#f9f9f9")
        self.Label7_2.configure(anchor='w')
        self.Label7_2.configure(compound='left')
        self.Label7_2.configure(text='''Status:''')
        self.process_jpg_status = tk.Label(self.process_jpg_block)
        self.process_jpg_status.place(relx=0.72, rely=0.681, height=23, width=149
                , bordermode='ignore')
        self.process_jpg_status.configure(activebackground="#f9f9f9")
        self.process_jpg_status.configure(anchor='w')
        self.process_jpg_status.configure(compound='left')
        self.process_jpg_status.configure(text='''None''')
        self.jpg_threads = tk.Spinbox(self.process_jpg_block, from_=1.0, to=100.0)
        self.jpg_threads.place(relx=0.219, rely=0.25, relheight=0.224
                , relwidth=0.118, bordermode='ignore')
        self.jpg_threads.configure(activebackground="#f9f9f9")
        self.jpg_threads.configure(background="white")
        self.jpg_threads.configure(font="TkDefaultFont")
        self.jpg_threads.configure(highlightbackground="black")
        self.jpg_threads.configure(selectbackground="#c4c4c4")
        self.value_list = ['5',]
        self.jpg_threads.configure(values=self.value_list)
        self.jpg_label = tk.Label(self.process_jpg_block)
        self.jpg_label.place(relx=0.029, rely=0.25, height=29, width=130
                , bordermode='ignore')
        self.jpg_label.configure(activebackground="#f9f9f9")
        self.jpg_label.configure(anchor='w')
        self.jpg_label.configure(compound='left')
        self.jpg_label.configure(text='''No of Threads''')
        self.stitch_360low_block = tk.LabelFrame(self.top)
        self.stitch_360low_block.place(relx=0.028, rely=0.765, relheight=0.139
                , relwidth=0.945)
        self.stitch_360low_block.configure(relief='groove')
        self.stitch_360low_block.configure(text='''Stitch 360low''')
        self.stitch_360 = ttk.Progressbar(self.stitch_360low_block)
        self.stitch_360.place(relx=0.554, rely=0.252, relwidth=0.41
                , relheight=0.0, height=19, bordermode='ignore')
        self.stitch_360.configure(length="281")
        self.start_sitch_360 = ttk.Button(self.stitch_360low_block)
        self.start_sitch_360.place(relx=0.073, rely=0.591, height=31, width=80
                , bordermode='ignore')
        self.start_sitch_360.configure(command=project1_support.start_stitch_360)
        self.start_sitch_360.configure(takefocus="")
        self.start_sitch_360.configure(text='''Start''')
        self.start_sitch_360.configure(compound='left')
        self.Label5_2_1 = tk.Label(self.stitch_360low_block)
        self.Label5_2_1.place(relx=0.633, rely=0.452, height=23, width=109
                , bordermode='ignore')
        self.Label5_2_1.configure(activebackground="#f9f9f9")
        self.Label5_2_1.configure(anchor='w')
        self.Label5_2_1.configure(compound='left')
        self.Label5_2_1.configure(text='''Recording:''')
        self.stitch_360_rec = tk.Label(self.stitch_360low_block)
        self.stitch_360_rec.place(relx=0.783, rely=0.452, height=23, width=69
                , bordermode='ignore')
        self.stitch_360_rec.configure(activebackground="#f9f9f9")
        self.stitch_360_rec.configure(anchor='w')
        self.stitch_360_rec.configure(compound='left')
        self.stitch_360_rec.configure(text='''0''')
        self.Label7_2_1 = tk.Label(self.stitch_360low_block)
        self.Label7_2_1.place(relx=0.624, rely=0.678, height=24, width=70
                , bordermode='ignore')
        self.Label7_2_1.configure(activebackground="#f9f9f9")
        self.Label7_2_1.configure(anchor='w')
        self.Label7_2_1.configure(compound='left')
        self.Label7_2_1.configure(text='''Status:''')
        self.stitch_360_status = tk.Label(self.stitch_360low_block)
        self.stitch_360_status.place(relx=0.72, rely=0.678, height=24, width=149
                , bordermode='ignore')
        self.stitch_360_status.configure(activebackground="#f9f9f9")
        self.stitch_360_status.configure(anchor='w')
        self.stitch_360_status.configure(compound='left')
        self.stitch_360_status.configure(text='''None''')
        self.stitch_360_threads = tk.Spinbox(self.stitch_360low_block, from_=1.0, to=100.0)
        self.stitch_360_threads.place(relx=0.219, rely=0.252, relheight=0.217
                , relwidth=0.118, bordermode='ignore')
        self.stitch_360_threads.configure(activebackground="#f9f9f9")
        self.stitch_360_threads.configure(background="white")
        self.stitch_360_threads.configure(font="TkDefaultFont")
        self.stitch_360_threads.configure(highlightbackground="black")
        self.stitch_360_threads.configure(selectbackground="#c4c4c4")
        self.value_list = ['1',]
        self.stitch_360_threads.configure(values=self.value_list)
        self.stitch_360_threads.configure(wrap="1")
        self.stitch_360_label = tk.Label(self.stitch_360low_block)
        self.stitch_360_label.place(relx=0.029, rely=0.252, height=29, width=130
                , bordermode='ignore')
        self.stitch_360_label.configure(activebackground="#f9f9f9")
        self.stitch_360_label.configure(anchor='w')
        self.stitch_360_label.configure(compound='left')
        self.stitch_360_label.configure(text='''No of Threads''')
        self.close_program = ttk.Button(self.top)
        self.close_program.place(relx=0.413, rely=0.933, height=31, width=80)
        self.close_program.configure(command=project1_support.close_program)
        self.close_program.configure(takefocus="")
        self.close_program.configure(text='''Close''')
        self.close_program.configure(compound='left')
        self.stitch_360high_block = tk.LabelFrame(self.top)
        self.stitch_360high_block.place(relx=0.028, rely=0.595, relheight=0.162
                , relwidth=0.945)
        self.stitch_360high_block.configure(relief='groove')
        self.stitch_360high_block.configure(text='''Stitch 360high''')
        self.Label6 = tk.Label(self.stitch_360high_block)
        self.Label6.place(relx=0.022, rely=0.224, height=24, width=129
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(text='''PTS Template''')
        self.pts_template = tk.Entry(self.stitch_360high_block)
        self.pts_template.place(relx=0.201, rely=0.224, height=26, relwidth=0.636
                , bordermode='ignore')
        self.pts_template.configure(background="white")
        self.pts_template.configure(font="TkFixedFont")
        self.pts_template.configure(selectbackground="#c4c4c4")
        self.TButton1_1 = ttk.Button(self.stitch_360high_block)
        self.TButton1_1.place(relx=0.854, rely=0.224, height=31, width=80
                , bordermode='ignore')
        self.TButton1_1.configure(command=project1_support.select_template)
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''Select''')
        self.TButton1_1.configure(compound='left')
        self.generate_pts = ttk.Button(self.stitch_360high_block)
        self.generate_pts.place(relx=0.233, rely=0.597, height=31, width=130
                , bordermode='ignore')
        self.generate_pts.configure(command=project1_support.generate_pts)
        self.generate_pts.configure(takefocus="")
        self.generate_pts.configure(text='''Generate PTS''')
        self.generate_pts.configure(compound='left')
        self.start_stitch_360low = ttk.Button(self.stitch_360high_block)
        self.start_stitch_360low.place(relx=0.598, rely=0.597, height=31
                , width=90, bordermode='ignore')
        self.start_stitch_360low.configure(command=project1_support.generate_ptsstart_stitch_360low)
        self.start_stitch_360low.configure(takefocus="")
        self.start_stitch_360low.configure(text='''Start''')
        self.start_stitch_360low.configure(compound='left')

class select_rec:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x431+1008+592")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Select Recordings")
        top.configure(highlightcolor="black")

        self.top = top

        self.recordings = tk.LabelFrame(self.top)
        self.recordings.place(relx=0.033, rely=0.023, relheight=0.824
                , relwidth=0.917)
        self.recordings.configure(relief='groove')
        self.recordings.configure(text='''Recordings''')
        self.close_select_rec = tk.Button(self.top)
        self.close_select_rec.place(relx=0.433, rely=0.882, height=36, width=89)
        self.close_select_rec.configure(activebackground="beige")
        self.close_select_rec.configure(borderwidth="2")
        self.close_select_rec.configure(command=project1_support.close_select_rec)
        self.close_select_rec.configure(compound='left')
        self.close_select_rec.configure(text='''Select''')

class project:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("370x422+306+315")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Select Project")
        top.configure(highlightcolor="black")

        self.top = top

        self.projects = tk.LabelFrame(self.top)
        self.projects.place(relx=0.051, rely=0.024, relheight=0.815
                , relwidth=0.911)
        self.projects.configure(relief='groove')
        self.projects.configure(text='''Projects''')
        self.close_select_prj = tk.Button(self.top)
        self.close_select_prj.place(relx=0.405, rely=0.877, height=33, width=73)
        self.close_select_prj.configure(activebackground="beige")
        self.close_select_prj.configure(borderwidth="2")
        self.close_select_prj.configure(command=project1_support.close_select_prj)
        self.close_select_prj.configure(compound='left')
        self.close_select_prj.configure(text='''Select''')

def start_up():
    project1_support.main()

if __name__ == '__main__':
    project1_support.main()




