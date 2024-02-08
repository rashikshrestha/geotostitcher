#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Feb 05, 2024 09:09:33 AM +0545  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


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
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
set vTcl(project_theme) page-legacy



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
        -menu $top.m49 -background #d9d9d9 
    wm focusmodel $top passive
    wm geometry $top 726x827+611+989
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
    vTcl:DefineAlias "$top" "geoto_stitcher" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m49" \
        -activebackground #ececec -activeforeground black \
        -font "-family {DejaVu Sans} -size 10" -tearoff 0 
    labelframe "$top.lab53" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Process PGF" -background #d9d9d9 -height 119 \
        -highlightcolor #000000 -width 686 
    vTcl:DefineAlias "$top.lab53" "process_pgf_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.lab53
    ttk::progressbar "$site_3_0.tPr67" \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_pgf" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu73" \
        -command "start_process_pgf" -text "Start" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_process_pgf" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab75" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Recording:" 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab76" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "0" 
    vTcl:DefineAlias "$site_3_0.lab76" "process_pgf_rec" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab77" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Status:" 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab78" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "None" 
    vTcl:DefineAlias "$site_3_0.lab78" "process_pgf_status" vTcl:WidgetProc "geoto_stitcher" 1
    spinbox "$site_3_0.spi86" \
        -activebackground #f9f9f9 -background white \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 -from 1.0 \
        -highlightbackground black -highlightcolor #000000 -increment 1.0 \
        -insertbackground #000000 -selectbackground #c4c4c4 \
        -selectforeground black -to 100.0 -values "100" 
    vTcl:DefineAlias "$site_3_0.spi86" "pgf_threads" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab87" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "No of Threads" 
    vTcl:DefineAlias "$site_3_0.lab87" "pgf_label" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but47" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "upload_pgf" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Upload" 
    vTcl:DefineAlias "$site_3_0.but47" "upload_pgf" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.41 -height 19 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.585 -width 80 -relwidth 0 \
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
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -relx 0.292 -y 0 -rely 0.585 -width 73 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$top.tBu62" \
        -command "auto_fill" -text "Auto Fill" -compound left 
    vTcl:DefineAlias "$top.tBu62" "auto_fill" vTcl:WidgetProc "geoto_stitcher" 1
    labelframe "$top.lab90" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Process JPG" -background #d9d9d9 -height 118 \
        -highlightcolor #000000 -width 686 
    vTcl:DefineAlias "$top.lab90" "process_jpg_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.lab90
    ttk::progressbar "$site_3_0.tPr67" \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_jpg" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu73" \
        -command "start_process_jpg" -text "Start" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_process_jpg" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab75" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Recording:" 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5_2" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab76" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "0" 
    vTcl:DefineAlias "$site_3_0.lab76" "process_jpg_rec" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab77" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Status:" 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7_2" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab78" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "None" 
    vTcl:DefineAlias "$site_3_0.lab78" "process_jpg_status" vTcl:WidgetProc "geoto_stitcher" 1
    spinbox "$site_3_0.spi86" \
        -activebackground #f9f9f9 -background white \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 -from 1.0 \
        -highlightbackground black -highlightcolor #000000 -increment 1.0 \
        -insertbackground #000000 -selectbackground #c4c4c4 \
        -selectforeground black -to 100.0 -values "200" 
    vTcl:DefineAlias "$site_3_0.spi86" "jpg_threads" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab87" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "No of Threads" 
    vTcl:DefineAlias "$site_3_0.lab87" "jpg_label" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but48" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "upload_jpg" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Upload" 
    vTcl:DefineAlias "$site_3_0.but48" "upload_jpg" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.259 -width 0 \
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
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.306 -y 0 -rely 0.595 -width 73 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    labelframe "$top.lab91" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Stitch 360low" -background #d9d9d9 -height 119 \
        -highlightcolor #000000 -width 686 
    vTcl:DefineAlias "$top.lab91" "stitch_360low_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.lab91
    ttk::progressbar "$site_3_0.tPr67" \
        -length 281 
    vTcl:DefineAlias "$site_3_0.tPr67" "process_stitch_360low" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu73" \
        -command "start_stitch_360low" -text "Start" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu73" "start_sitch_360low" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab75" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Recording:" 
    vTcl:DefineAlias "$site_3_0.lab75" "Label5_2_1" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab76" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "0" 
    vTcl:DefineAlias "$site_3_0.lab76" "stitch_360low_rec" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab77" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Status:" 
    vTcl:DefineAlias "$site_3_0.lab77" "Label7_2_1" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab78" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "None" 
    vTcl:DefineAlias "$site_3_0.lab78" "stitch_360low_status" vTcl:WidgetProc "geoto_stitcher" 1
    spinbox "$site_3_0.spi86" \
        -activebackground #f9f9f9 -background white \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 -from 1.0 \
        -highlightbackground black -highlightcolor #000000 -increment 1.0 \
        -insertbackground #000000 -selectbackground #c4c4c4 \
        -selectforeground black -to 100.0 -values "5" -wrap 1 
    vTcl:DefineAlias "$site_3_0.spi86" "stitch_360low_threads" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab87" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "No of Threads" 
    vTcl:DefineAlias "$site_3_0.lab87" "stitch_360_label" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but47" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "upload_360low" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Upload" 
    vTcl:DefineAlias "$site_3_0.but47" "upload_360low" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.tPr67 \
        -in $site_3_0 -x 0 -relx 0.554 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.41 -height 19 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.6 -width 80 -relwidth 0 \
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
        -in $site_3_0 -x 0 -relx 0.223 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab87 \
        -in $site_3_0 -x 0 -relx 0.029 -y 0 -rely 0.252 -width 0 \
        -relwidth 0.19 -height 0 -relheight 0.252 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -relx 0.292 -y 0 -rely 0.6 -width 73 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$top.tBu92" \
        -command "close_program" -text "Close" -compound left 
    vTcl:DefineAlias "$top.tBu92" "close_program" vTcl:WidgetProc "geoto_stitcher" 1
    labelframe "$top.lab46" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Stitch 360high" -background #d9d9d9 -height 136 \
        -highlightcolor #000000 -width 681 
    vTcl:DefineAlias "$top.lab46" "stitch_360high_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.lab46
    label "$site_3_0.lab47" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "PTS Template" 
    vTcl:DefineAlias "$site_3_0.lab47" "Label6" vTcl:WidgetProc "geoto_stitcher" 1
    entry "$site_3_0.ent49" \
        -background white -font "-family {DejaVu Sans Mono} -size 10" \
        -foreground #000000 -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #c4c4c4 -selectforeground black -width 436 
    vTcl:DefineAlias "$site_3_0.ent49" "pts_template" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu50" \
        -command "select_template" -text "Select" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu50" "TButton1_1" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu46" \
        -command "generate_pts" -text "Generate PTS" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu46" "generate_pts" vTcl:WidgetProc "geoto_stitcher" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu47" \
        -command "start_stitch_360high" -text "Start" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu47" "start_stitch_360high" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but47" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "upload_360high" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Upload" 
    vTcl:DefineAlias "$site_3_0.but47" "upload_360high" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.022 -y 0 -rely 0.224 -width 0 \
        -relwidth 0.188 -height 0 -relheight 0.179 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 0 -relx 0.201 -y 0 -rely 0.224 -width 436 \
        -relwidth 0 -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu50 \
        -in $site_3_0 -x 0 -relx 0.854 -y 0 -rely 0.224 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu46 \
        -in $site_3_0 -x 0 -relx 0.087 -y 0 -rely 0.597 -width 130 \
        -relwidth 0 -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu47 \
        -in $site_3_0 -x 0 -relx 0.437 -y 0 -rely 0.597 -width 90 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -relx 0.729 -y 0 -rely 0.597 -width 73 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    labelframe "$top.lab52" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Pre Process" -background #d9d9d9 -height 88 \
        -highlightcolor #000000 -width 686 
    vTcl:DefineAlias "$top.lab52" "preprocess_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.lab52
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TButton -background  [list disabled #d9d9d9 !disabled #d9d9d9]
    ttk::button "$site_3_0.tBu61" \
        -command "start_preprocess" -text "Start" -compound left 
    vTcl:DefineAlias "$site_3_0.tBu61" "start_preprocess" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.tBu61 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.345 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ::vTcl::widgets::ttk::labelframe::createCmd "$top.tLa51" \
        -text "Configs" -width 684 -height 138 
    vTcl:DefineAlias "$top.tLa51" "configs_block" vTcl:WidgetProc "geoto_stitcher" 1
    set site_3_0 $top.tLa51
    label "$site_3_0.lab46" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Input Dir" 
    vTcl:DefineAlias "$site_3_0.lab46" "Label1_1" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but55" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "select_project" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Select Project" 
    vTcl:DefineAlias "$site_3_0.but55" "select_project" vTcl:WidgetProc "geoto_stitcher" 1
    button "$site_3_0.but56" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "select_recording" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Select Recording" 
    vTcl:DefineAlias "$site_3_0.but56" "select_recording" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab47" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Project: " 
    vTcl:DefineAlias "$site_3_0.lab47" "Label4_1_1" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab49" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Recording:" 
    vTcl:DefineAlias "$site_3_0.lab49" "Label4_2" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab50" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "0" 
    vTcl:DefineAlias "$site_3_0.lab50" "rec_num" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab51" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Select Disk" 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1" vTcl:WidgetProc "geoto_stitcher" 1
    label "$site_3_0.lab48" \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Unknown" 
    vTcl:DefineAlias "$site_3_0.lab48" "project_name" vTcl:WidgetProc "geoto_stitcher" 1
    radiobutton "$site_3_0.rad49" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_s16" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "s16" -value "0" -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad49" "select_s16" vTcl:WidgetProc "geoto_stitcher" 1
    radiobutton "$site_3_0.rad47" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_s17" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "s17" -value "1" -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad47" "select_s17" vTcl:WidgetProc "geoto_stitcher" 1
    radiobutton "$site_3_0.rad48" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_s18" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -justify left -selectcolor #d9d9d9 \
        -text "s18" -value "2" -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad48" "select_s18" vTcl:WidgetProc "geoto_stitcher" 1
    radiobutton "$site_3_0.rad51" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_s17e" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -justify left -selectcolor #d9d9d9 -text "s17e" -value "3" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad51" "select_s16_1_1" vTcl:WidgetProc "geoto_stitcher" 1
    radiobutton "$site_3_0.rad52" \
        -activebackground beige -activeforeground black -anchor w \
        -background #d9d9d9 -command "select_s18g" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -justify left -selectcolor #d9d9d9 -text "s18g" -value "4" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad52" "select_s16_1_1_1" vTcl:WidgetProc "geoto_stitcher" 1
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.286 -y 0 -rely 1.483 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.166 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 0 -relx 0.278 -y 0 -rely 0.222 -width 133 \
        -relwidth 0 -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.281 -y 0 -rely 0.607 -width 133 \
        -relwidth 0 -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.541 -y 0 -rely 0.296 -width 0 \
        -relwidth 0.101 -height 0 -relheight 0.133 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.541 -y 0 -rely 0.593 -width 0 \
        -relwidth 0.117 -height 0 -relheight 0.193 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.671 -y 0 -rely 0.63 -width 0 \
        -relwidth 0.145 -height 0 -relheight 0.119 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.076 -y 0 -rely 0.267 -width 0 \
        -relwidth 0.114 -height 0 -relheight 0.156 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.643 -y 0 -rely 0.296 -width 0 \
        -relwidth 0.336 -height 0 -relheight 0.126 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad49 \
        -in $site_3_0 -x 0 -relx 0.044 -y 0 -rely 0.444 -width 0 \
        -relwidth 0.098 -height 0 -relheight 0.17 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad47 \
        -in $site_3_0 -x 0 -relx 0.044 -y 0 -rely 0.593 -width 0 \
        -relwidth 0.099 -height 0 -relheight 0.17 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad48 \
        -in $site_3_0 -x 0 -relx 0.044 -y 0 -rely 0.741 -width 0 \
        -relwidth 0.098 -height 0 -relheight 0.17 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad51 \
        -in $site_3_0 -x 0 -relx 0.132 -y 0 -rely 0.593 -width 0 \
        -relwidth 0.098 -height 0 -relheight 0.17 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad52 \
        -in $site_3_0 -x 0 -relx 0.132 -y 0 -rely 0.741 -width 0 \
        -relwidth 0.098 -height 0 -relheight 0.17 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab53 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.3 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.142 -anchor nw -bordermode ignore 
    place $top.tBu62 \
        -in $top -x 0 -relx 0.853 -y 0 -rely 0.937 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab90 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.447 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.141 -anchor nw -bordermode ignore 
    place $top.lab91 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.765 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.139 -anchor nw -bordermode ignore 
    place $top.tBu92 \
        -in $top -x 0 -relx 0.413 -y 0 -rely 0.933 -width 80 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.595 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.162 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.181 -width 0 -relwidth 0.945 \
        -height 0 -relheight 0.105 -anchor nw -bordermode ignore 
    place $top.tLa51 \
        -in $top -x 0 -relx 0.028 -y 0 -rely 0.012 -width 0 -relwidth 0.942 \
        -height 0 -relheight 0.163 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top2 {base} {
    global vTcl
    if {$base == ""} {
        set base .top2
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
        -background #d9d9d9 -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 361x750+1368+969
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
    set toptitle "Select Recordings"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "select_rec" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    button "$top.but48" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "close_select_rec" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Select" 
    vTcl:DefineAlias "$top.but48" "close_select_rec" vTcl:WidgetProc "select_rec" 1
    labelframe "$top.lab47" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Recordings" -background #d9d9d9 -height 355 \
        -highlightcolor #000000 -width 550 
    vTcl:DefineAlias "$top.lab47" "recordings" vTcl:WidgetProc "select_rec" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but48 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.882 -width 89 -relwidth 0 \
        -height 36 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.023 -width 0 -relwidth 0.917 \
        -height 0 -relheight 0.824 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top3 {base} {
    global vTcl
    if {$base == ""} {
        set base .top3
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
        -menu $top.m52 -background #d9d9d9 -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 370x422+164+936
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
    set toptitle "Select Project"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "project" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m52" \
        -activebackground #ececec -activeforeground black \
        -font "-family {DejaVu Sans} -size 10" -tearoff 0 
    labelframe "$top.lab53" \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -text "Projects" -background #d9d9d9 -height 344 \
        -highlightcolor #000000 -width 337 
    vTcl:DefineAlias "$top.lab53" "projects" vTcl:WidgetProc "project" 1
    button "$top.but54" \
        -activebackground beige -activeforeground black -background #d9d9d9 \
        -borderwidth 2 -command "close_select_prj" -compound left \
        -font "-family {DejaVu Sans} -size 10" -foreground #000000 \
        -highlightcolor #000000 -text "Select" 
    vTcl:DefineAlias "$top.but54" "close_select_prj" vTcl:WidgetProc "project" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab53 \
        -in $top -x 0 -relx 0.051 -y 0 -rely 0.024 -width 0 -relwidth 0.911 \
        -height 0 -relheight 0.815 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.405 -y 0 -rely 0.877 -width 73 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 

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
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top2 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}
set btop3 ""
if {$vTcl(borrow)} {
    set btop3 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop3 $vTcl(tops)] != -1} {
        set btop3 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop3
Window show .top3 $btop3
if {$vTcl(borrow)} {
    $btop3 configure -background plum
}

