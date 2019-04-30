#!/usr/bin/env python
import os
import glob
import numpy as np

for f in glob.glob('Spectra/Sp_bin*.fits'):
    if '_with_continuum' in f:
        pass
    else:
        os.system('/Users/vera/Soft/ALFA/alfa %s -o Alfa -vtol2 10 -sc muse.cat -dc optical_deep.cat -n 0 -g 1000'%f)

