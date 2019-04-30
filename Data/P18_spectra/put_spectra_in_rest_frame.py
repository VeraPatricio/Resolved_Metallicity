from astropy.io import fits

def to_rest_frame(filein,z):

	data = fits.getdata(filein)
	header = fits.getheader(filein,ext=1)
	header['CRVAL1'] = header['CRVAL1'] /(1+z)
	header['CDELT1'] = header['CDELT1']/(1+z)
	fits.writeto(filein.replace('.fits','_restframe.fits'),data,header)
	print('Created file %s'%filein.replace('.fits','_restframe.fits'))


to_rest_frame('Spectrum_A370_ContSub_pPXF.fits',0.725)
to_rest_frame('Spectrum_A370_mosaic_CMSub.fits',0.725)