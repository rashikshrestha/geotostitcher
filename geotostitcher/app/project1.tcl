#############################################################################
# Generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#  Oct 14, 2022 07:08:52 PM +0545  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m49" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 726x750+706+105
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "GeoTo Stitcher"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu $top.m49 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa51 \
        -text Configs -width 684 -height 150 
    vTcl:DefineAlias "$top.tLa51" "configs_block" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa51
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu52 \
        -command select_input_dir -takefocus {} -text Select -compound left 
    vTcl:DefineAlias "$site_3_0.tBu52" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu53 \
        -command select_output_dir -takefocus {} -text Select -compound left 
    vTcl:DefineAlias "$site_3_0.tBu53" "TButton2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent55 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -width 456 
    vTcl:DefineAlias "$site_3_0.ent55" "input_dir" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Input Dir} 
    vTcl:DefineAlias "$site_3_0.lab56" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Input Dir} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab47 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Output Dir} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Config File} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent49 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -width 456 
    vTcl:DefineAlias "$site_3_0.ent49" "output_dir" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent50 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -width 456 
    vTcl:DefineAlias "$site_3_0.ent50" "config_file" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu51 \
        -command select_config_file -takefocus {} -text Select -compound left 
    vTcl:DefineAlias "$site_3_0.tBu51" "TButton2_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tBu52 \
        -in $site_3_0 -x 0 -relx 0.857 -y 0 -rely 0.169 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu53 \
        -in $site_3_0 -x 0 -relx 0.857 -y 0 -rely 0.451 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent55 \
        -in $site_3_0 -x 0 -relx 0.177 -y 0 -rely 0.169 -width 456 \
        -relwidth 0 -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.022 -y 0 -rely 0.172 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.166 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.286 -y 0 -rely 1.483 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.166 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.022 -y 0 -rely 0.414 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.166 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.022 -y 0 -rely 0.69 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.166 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 0 -relx 0.177 -y 0 -rely 0.451 -width 456 \
        -relwidth 0 -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent50 \
        -in $site_3_0 -x 0 -relx 0.177 -y 0 -rely 0.725 -width 456 \
        -relwidth 0 -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu51 \
        -in $site_3_0 -x 0 -relx 0.857 -y 0 -rely 0.718 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab52 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Pre Process} -background $vTcl(actual_gui_bg) -height 89 \
        -width 686 
    vTcl:DefineAlias "$top.lab52" "preprocess_block" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab52
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu61 \
        -command start_preprocess -takefocus {} -text Start -compound left 
    vTcl:DefineAlias "$site_3_0.tBu61" "start_preprocess" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab66 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {No of recordings:} 
    vTcl:DefineAlias "$site_3_0.lab66" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab69 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text 0 
    vTcl:DefineAlias "$site_3_0.lab69" "no_of_rec" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab93 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Project Name: } 
    vTcl:DefineAlias "$site_3_0.lab93" "Label4_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab94 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Unknown 
    vTcl:DefineAlias "$site_3_0.lab94" "project_name" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tBu61 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.404 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab66 \
        -in $site_3_0 -x 0 -relx 0.481 -y 0 -rely 0.562 -width 0 \
        -relwidth 0.22 -height 0 -relheight 0.303 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab69 \
        -in $site_3_0 -x 0 -relx 0.706 -y 0 -rely 0.607 -width 0 \
        -relwidth 0.086 -height 0 -relheight 0.191 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab93 \
        -in $site_3_0 -x 0 -relx 0.481 -y 0 -rely 0.258 -width 0 \
        -relwidth 0.191 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab94 \
        -in $site_3_0 -x 0 -relx 0.671 -y 0 -rely 0.258 -width 0 \
        -relwidth 0.277 -height 0 -relheight 0.191 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab53 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Process PGF} -background $vTcl(actual_gui_bg) -height 126 \
        -width 686 
    vTcl:DefineAlias "$top.lab53" "process_pgf_block" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab53
    ttk::progressbar $site_3_0.tPr67 \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_pgf" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu73 \
        -command start_process_pgf -takefocus {} -text Start -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_process_pgf" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab75 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text Recording: 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab76 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text 0 
    vTcl:DefineAlias "$site_3_0.lab76" "process_pgf_rec" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab77 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text Status: 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab78 \
        -activeforeground #000000 -anchor w -background $vTcl(actual_gui_bg) \
        -compound left -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text None 
    vTcl:DefineAlias "$site_3_0.lab78" "process_pgf_status" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_3_0.spi86 \
        -activebackground #f9f9f9 -background white -font TkDefaultFont \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -to 100.0 -values 5 
    vTcl:DefineAlias "$site_3_0.spi86" "pgf_threads" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab87 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {No of Threads} 
    vTcl:DefineAlias "$site_3_0.lab87" "pgf_label" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.41 -height 19 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.588 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 0 -relx 0.633 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.159 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab76 \
        -in $site_3_0 -x 0 -relx 0.783 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.101 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 0 -relx 0.624 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.102 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 0 -relx 0.72 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.217 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.spi86 \
        -in $site_3_0 -x 0 -relx 0.219 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.218 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab87 \
        -in $site_3_0 -x 0 -relx 0.029 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.19 -height 0 -relheight 0.252 -anchor nw \
        -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu62 \
        -command auto_fill -takefocus {} -text {Auto Fill} -compound left 
    vTcl:DefineAlias "$top.tBu62" "auto_fill" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab90 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Process JPG} -background $vTcl(actual_gui_bg) -height 116 \
        -highlightcolor black -width 686 
    vTcl:DefineAlias "$top.lab90" "process_jpg_block" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab90
    ttk::progressbar $site_3_0.tPr67 \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_pgf_2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu73 \
        -command start_process_pgf -takefocus {} -text Start -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_process_pgf_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab75 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Recording: 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab76 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text 0 
    vTcl:DefineAlias "$site_3_0.lab76" "process_pgf_rec_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab77 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Status: 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab78 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text None 
    vTcl:DefineAlias "$site_3_0.lab78" "process_pgf_status_2" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_3_0.spi86 \
        -activebackground #f9f9f9 -background white -font TkDefaultFont \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -to 100.0 \
        -values 100 
    vTcl:DefineAlias "$site_3_0.spi86" "jpg_threads" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab87 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {No of Threads} 
    vTcl:DefineAlias "$site_3_0.lab87" "pgf_label_2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.41 -height 19 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.588 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 0 -relx 0.633 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.159 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab76 \
        -in $site_3_0 -x 0 -relx 0.783 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.101 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 0 -relx 0.624 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.102 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 0 -relx 0.72 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.217 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.spi86 \
        -in $site_3_0 -x 0 -relx 0.219 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.218 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab87 \
        -in $site_3_0 -x 0 -relx 0.029 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.19 -height 0 -relheight 0.252 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab91 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {Stitch 360} -background $vTcl(actual_gui_bg) -height 125 \
        -highlightcolor black -width 686 
    vTcl:DefineAlias "$top.lab91" "process_jpg_block_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab91
    ttk::progressbar $site_3_0.tPr67 \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_pgf_2_1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu73 \
        -command start_process_pgf -takefocus {} -text Start -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_process_pgf_2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab75 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Recording: 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5_2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab76 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text 0 
    vTcl:DefineAlias "$site_3_0.lab76" "process_pgf_rec_2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab77 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Status: 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7_2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab78 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text None 
    vTcl:DefineAlias "$site_3_0.lab78" "process_pgf_status_2_1" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_3_0.spi86 \
        -activebackground #f9f9f9 -background white -font TkDefaultFont \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -to 100.0 \
        -values 100 
    vTcl:DefineAlias "$site_3_0.spi86" "jpg_threads_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab87 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {No of Threads} 
    vTcl:DefineAlias "$site_3_0.lab87" "pgf_label_2_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.41 -height 19 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.588 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 0 -relx 0.633 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.159 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab76 \
        -in $site_3_0 -x 0 -relx 0.783 -y 0 -rely 0.454 -width 0 \
        -relwidth 0.101 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 0 -relx 0.624 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.102 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 0 -relx 0.72 -y 0 -rely 0.681 -width 0 \
        -relwidth 0.217 -height 0 -relheight 0.202 -anchor nw \
        -bordermode ignore 
    place $site_3_0.spi86 \
        -in $site_3_0 -x 0 -relx 0.219 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.218 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab87 \
        -in $site_3_0 -x 0 -relx 0.029 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.19 -height 0 -relheight 0.252 -anchor nw \
        -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu92 \
        -command close_program -takefocus {} -text Close -compound left 
    vTcl:DefineAlias "$top.tBu92" "close_program" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa51 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.015 -width 0 -relwidth 0.942 \
        -height 0 -relheight 0.2 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.223 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.12 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.356 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.168 -anchor nw -bordermode ignore 
    place $top.tBu62 \
        -in $top -x 0 -relx 0.854 -y 0 -rely 0.933 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab90 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.539 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.155 -anchor nw -bordermode ignore 
    place $top.lab91 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.707 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.167 -anchor nw -bordermode ignore 
    place $top.tBu92 \
        -in $top -x 0 -relx 0.413 -y 0 -rely 0.92 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
