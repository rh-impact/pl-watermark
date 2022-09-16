#
# watermark ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import sys
from chrisapp.base import ChrisApp

from PIL import Image

EXTS = ('.jpg', '.jpeg', '.png')

Gstr_title = r"""
               _                                 _    
              | |                               | |   
__      ____ _| |_ ___ _ __ _ __ ___   __ _ _ __| | __
\ \ /\ / / _` | __/ _ \ '__| '_ ` _ \ / _` | '__| |/ /
 \ V  V / (_| | ||  __/ |  | | | | | | (_| | |  |   < 
  \_/\_/ \__,_|\__\___|_|  |_| |_| |_|\__,_|_|  |_|\_\
                                                      
                                                      
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       watermark

    SYNOPSIS

        docker run --rm fnndsc/pl-watermark watermark                     \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-watermark watermark                        \
                /incoming /outgoing

    DESCRIPTION

        `watermark` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""

if len(sys.argv) < 3:
    print('Usage: watermark.py \'image folder path\' \'logo path\' [--topleft, --topright, --bottomleft, --bottomright, --center]')
    sys.exit()
elif len(sys.argv) == 4:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
else:
    path = sys.argv[1]
    lgo = sys.argv[2]

logo = Image.open(lgo)
logoWidth = logo.width
logoHeight = logo.height

for filename in os.listdir(path):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
        image = Image.open(path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height

        try:
            if pos == '--topleft':
                image.paste(logo, (0, 0), logo)
            elif pos == 'topright':
                image.paste(logo, (imageWidth - logoWidth, 0), logo)
            elif pos == 'bottomleft':
                image.paste(logo, (0, imageHeight - logoHeight), logo)
            elif pos == 'bottomright':
                image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight), logo)
            elif pos == 'center':
                image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: watermark.py \'image path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')

            image.save(path + '/' + filename)
            print('Added watermark to ' + path + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            image.save(path + '/' + filename)
            print('Added default watermark to ' + path + '/' + filename)

class Watermark(ChrisApp):
    """
    Add watermark to images
    """
    PACKAGE                 = __package__
    TITLE                   = 'pl-watermark'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
