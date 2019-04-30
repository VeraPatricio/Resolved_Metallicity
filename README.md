# Resolved scaling relations and metallicity gradients onsub-kiloparsec scales at z≈1

Data and analysis done for PUT PAPER.

## Summary

The  existence  of  a  spatially  resolved  Star-Forming  Main  Sequence  (rSFMS)  and  aspatially  resolved  Mass-Metallicity  (rMZR)  relationis nowwell  established  for  lo-cal galaxies.Moreover, gradients with with metallicity decreasing with ra-dius seem to be common in local disc galaxies. These observations suggestthat galaxy formation is a self-regulating process, and provide constraintfor galaxy evolution models. Studying the evolution of these relations athigher redshifts is still however very challenging.In  this  paper,  we  analysethree gravitationally lensed galaxies atz=0.6, 0.7 and 1, observed withMUSE andSINFONI.  These  galaxies  are  highly  magnified  by  galaxy  clusters,  which  allow  usto observe resolved scaling relations and metallicity gradients on physical scales of acouple of hundred parsecs, comparable to studies of local galaxies. We confirm thatthe rSFMS is already in place at these redshifts on sub-kpc scales, and establish, forthe first time, the existence of the rMZR at higher redshifts. We develop a forward-modelling approach to fit 2D metallicity gradients of multiply imaged lensed galaxiesin the image plane. We derive gradients of -0.027±0.003, -0.019±0.003 and -0.039±0.060dex/kpc. Despite the fact that these are clumpy galaxies, typical of high redshift discs,the metallicity variations in the galaxies are well described by global linear gradients,and we do not see any increase/decrease of metallicity associated with the star-forming clumps.

## Files in this repository

### Data

Data used in this work. Divided into

	* Cubes - MUSE (cut-out cubes) and SINFONI cubes
	* HST - HST imaging
	* Galfit - Galfit fit results
	* P18_spectra - integrated spectra from Patricio et al 2018 a
	* Lensing - Lensing models 
	* Images - a bit of what was left (white lights, speudo narrow bands mainly from the cubes)

### Metallicity

Section 3 and 5 of the paper.

See GALAXY/GALAXY_measure_metallicity.ipynb notebook for measuring emission lines and deriving metallicities.

See GALAXY/GALAXY__2D_fit_FRApy.ipynb notebook for the metallicity gradient fitting

See GALAXY/GALAXY_mass_density.ipynb for the derivation of stellar mass density

## Scalar Relation

Section 4 of the paper.

See resolved_scalar_relations.ipynb notebook


### SinfoniAnalysis

Inspection of SINFONI cubes and extraction of spectra and narrow bands


### SpectralAnalysis

For Appendix A of the paper


### Plots

Plots used in the paper

## RGB

RGB images made from HST imaging
