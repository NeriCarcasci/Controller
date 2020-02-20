#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  Feb 07, 2020 12:56:03 PM GMT  platform: Windows NT
set vTcl(timestamp) ""


#############################################################################
## vTcl Code to Load User Images see vTcl:save2 in file.tcl

catch {package require Img}

foreach img {

        {{[file join C:/ Users neri Pictures coderdojo Untitled-1.png]} {user image} user {}}
        {{[file join C:/ Users neri Pictures coderdojo vector-hills-pixel-6.png]} {user image} user {}}

            } {
# from vTcl:image:dump_create_image_footer
    eval set _file [lindex $img 0]
    vTcl:image:create_new_image\
        $_file [lindex $img 1] [lindex $img 2] [lindex $img 3]
}

if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Fixedsys -size 43 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font13
vTcl:font:add_font \
    "-family Fixedsys -size 22 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font14
vTcl:font:add_font \
    "-family Fixedsys -size 36 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font15
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#ffffff} 
    wm focusmodel $top passive
    wm geometry $top 744x567+518+176
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Echo Controller"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab44 \
        -background {#fffcff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font13,object) -foreground {#000000} \
        -image [vTcl:image:get_image [file join C:/ Users neri Pictures coderdojo vector-hills-pixel-6.png]] \
        -text {Echo Controller} 
    vTcl:DefineAlias "$top.lab44" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#41ff3b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {New Path} 
    vTcl:DefineAlias "$top.but46" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#41ff3b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text EchoRt 
    vTcl:DefineAlias "$top.but48" "Button1_1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but50 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#41ff3b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Options 
    vTcl:DefineAlias "$top.but50" "Button1_3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but51 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#41ff3b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Vcontrol 
    vTcl:DefineAlias "$top.but51" "Button1_4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -background {#d9d9d9} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -image [vTcl:image:get_image [file join C:/ Users neri Pictures coderdojo Untitled-1.png]] \
        -text joystick -underline 0 
    vTcl:DefineAlias "$top.lab57" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -background {#fff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font15,object) -foreground {#000000} \
        -takefocus 0 -text {Echo Controller} 
    vTcl:DefineAlias "$top.lab58" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab44 \
        -in $top -x -20 -y 170 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 270 -y 150 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 270 -y 250 -width 190 -height 68 -anchor nw \
        -bordermode ignore 
    place $top.but50 \
        -in $top -x 170 -y 350 -width 186 -relwidth 0 -height 63 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 390 -y 350 -width 186 -height 63 -anchor nw \
        -bordermode ignore 
    place $top.lab57 \
        -in $top -x 510 -y 150 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 90 -y 20 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

