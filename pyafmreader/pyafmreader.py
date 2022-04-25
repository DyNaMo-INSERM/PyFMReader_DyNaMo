import os
from pyafmreader.constants import *
from jpk.loadjpkfile import loadJPKfile
from nanosc.loadnanoscfile import loadNANOSCfile
from pyafmreader.load_uff import loadUFFtxt
from pyafmreader.uff import UFF

def loadfile(filepath):
    filesuffix = os.path.splitext(filepath)[-1]

    uffobj = UFF()

    if filesuffix in jpkfiles:
        uffobj = loadJPKfile(filepath, uffobj, filesuffix)
    
    elif filesuffix in nanoscfiles:
        uffobj = loadNANOSCfile(filepath, uffobj)
    
    elif filesuffix in ufffiles:
        uffobj = loadUFFtxt(filepath, uffobj)
    
    return uffobj