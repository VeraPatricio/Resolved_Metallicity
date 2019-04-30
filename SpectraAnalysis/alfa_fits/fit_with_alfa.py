#!/usr/bin/env python
import os
import glob
import numpy as np

spectra_list = ['Spectrum_A370_ContSub_pPXF_restframe.fits',
                'Spectrum_AS1063_ContSub_pPXF_restframe.fits',
                'Spectrum_MACS1206_ContSub_pPXF_restframe.fits']


dir = '../../Data/P18_spectra/'

for f in spectra_list:
    os.system('/Users/vera/Soft/ALFA/alfa %s  -vtol2 10 -sc muse.cat -dc optical_deep.cat -n 0 -g 1000'%(dir+f))

