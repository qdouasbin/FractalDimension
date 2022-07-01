# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# create a new 'XDMF Reader'
isosurf_T1120K_iso_surf_00001871xmf = XDMFReader(registrationName='isosurf_T1120K_iso_surf_00001871.xmf', FileNames=['/scratch/cfd/qdouasbin/LEFEX/FractalDimension/Blender/input/H2/isosurf_T1120K_iso_surf_00001871.xmf'])

# Properties modified on isosurf_T1120K_iso_surf_00001871xmf
isosurf_T1120K_iso_surf_00001871xmf.PointArrayStatus = []
isosurf_T1120K_iso_surf_00001871xmf.GridStatus = ['isosurf_T1120K']

UpdatePipeline(time=0.00187190373236, proxy=isosurf_T1120K_iso_surf_00001871xmf)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=isosurf_T1120K_iso_surf_00001871xmf)

UpdatePipeline(time=0.00187190373236, proxy=extractSurface1)

# save data
SaveData('/scratch/cfd/qdouasbin/LEFEX/FractalDimension/Blender/input/H2/isosurf_T1120K_iso_surf_00001871.stl', proxy=extractSurface1)