#!/usr/bin/env python
import os
import glob
import numpy as np

for f in glob.glob('Spectra/sp_anuli*.fits'):
    os.system('/Users/vera/Soft/ALFA/alfa %s -o Alfa -vtol2 10 -n 0 -g 1000'%f)

