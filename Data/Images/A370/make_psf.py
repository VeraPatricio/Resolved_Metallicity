from astropy.io import fits
from astropy.modeling import models

im = fits.getdata('Im_A370_mosaic_OII_ContSub_CMSub.fits')
header = fits.getheader('Im_A370_mosaic_OII_ContSub_CMSub.fits',ext=1)


g_head = models.Gaussian2D(amplitude=1,x_mean=24,y_mean=72,x_stddev=1.5,y_stddev=1.5)
g_reg1 = models.Gaussian2D(amplitude=1,x_mean=53,y_mean=42,x_stddev=1.5,y_stddev=1.5)
g_reg2 = models.Gaussian2D(amplitude=1,x_mean=82,y_mean=27,x_stddev=1.5,y_stddev=1.5)
g_reg3 = models.Gaussian2D(amplitude=1,x_mean=116,y_mean=25,x_stddev=1.5,y_stddev=1.5)
g = g_head + g_reg1 + g_reg2 + g_reg3



psf_im = np.zeros_like(im)
x, y = np.meshgrid(range(im.shape[1]),range(im.shape[0]))
psf_im[:,:] = g(x,y)


plt.imshow(im)
plt.contour(psf_im)

fits.writeto('a370_psf_image.fits',psf_im,header)
