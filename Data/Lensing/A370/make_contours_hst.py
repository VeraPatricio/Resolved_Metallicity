from pycleanlens import cleanlens
  
model = cleanlens()
model.read_cleanset('A370_HST.par')
model.imframe = 'hst_regions.fits'
model.sframe = 'TEST_pycleanset.fits'
model.print_param()

model.draw_dwcs_region(output='test.dwcs',update=True)
~                                                         