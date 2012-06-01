'''
by Ciro D. Santilli 29/01/2012

the file structure:

this file       root/no_matter_which_folder_1/generate_plots.py
plot file	root/relative_input_path/PLOT-FILE-NAME.py
output file	root/relative_output_path/PLOT-FILE-NAME.svg

this contains global parameters and does the actual plotting of plot files.

disponible at:
https://docs.google.com/open?id=0B02Qah_J_vUEOWY5MWNkN2ItYjE3OC00YjYwLThkOTEtNDAxYjUwZDlmNzFi
https://docs.google.com/open?id=0B02Qah_J_vUEMDYxNzBmYWYtNWMwMy00YWMwLWIwMmYtMzBjYjUxZGUzZDk5

'''

import os.path
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


#- useful copy and paste. must be used in the individual plots ------------------------#
#--  transDataAxes = transforms.blended_transform_factory(ax.transData, ax.transAxes) --#
#--  transAxesData = transforms.blended_transform_factory(ax.transAxes,ax.transData) --#

#- style params common to all plots ------------------------------------------------------------#

#- zorder of things (who is on top of who) -#
axis_order = -1
helper_zorder = 1
plot_zorder = 0
open_ball_zorder = 2
title_font_size = 30
spines_off = False		    #- wether to turn spines off or not -#

#- axes -#
axis_line_width = 0.01 
axis_label_font_size = 24
axis_arrow_head_frac_x = 0.03    #- fraction of arrow length that is the head in the x direction. for y, must scale apropriately (depends on
axis_arrow_head_width = 10
y_label_position = [-0.05,0.5]
under_tick_labels_axes = -0.01 #deplacement for text under tick labels
tick_label_font_size = 20
anotation_font_size = 12
open_interval_ball_radius_x = 0.03

#- anotation parameters ---------------------------#

#- helpers -#
helper_linestyle='--'
helper_color = 'black'

#- open interval balls -#

#- file path parameters ------------------------------------------------------------#
root = os.path.dirname(os.path.dirname(__file__))
relative_input_path = "site-dev/plots_code"
relative_output_path = "uploads"
extension = '.py'
output_format = 'svg'

#- list of all files inside relative_output_path that will be plotted -#
file_names = [
#"x-minus-y-in-0-2-0-2"
#"2-minus-x-in-0-2-helper-x-equals-1"
#"x-pow-2-plus-y-pow-2-equals-1"
#"t-pow-2-in-minus-2-2"
#"test_plot"
#"e-pow-x-in-minus-2-2",
#"e-pow-x-in-minus-1-3",
#"e-pow-x-in-minus-1-1-2-4",
#"e-pow-x-in-r",
"e-pow-x-in-minus-2-2-view-x-minus-2-3",
#"e-pow-x-in-minus-1-3-view-x-minus-2-3",
#"e-pow-x-in-minus-2-3-view-x-minus-2-3",

];

    
for file_name in file_names:
    #- generate a plot from file -#
    plt.close()
    input_path = os.path.join( root, relative_input_path, os.path.normpath(file_name) + extension)
    execfile(input_path)
    plt.show()
    
    #- save last generated plot -#
    output_path = os.path.join( root, relative_output_path, os.path.splitext(file_name)[0] + "." + output_format)
    print output_path
    plt.savefig(output_path, format=output_format, bbox_inches='tight')
    
    
