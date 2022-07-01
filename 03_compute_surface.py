# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
import os
import glob
from paraview.simple import *

# pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/H2/isosurf_T1120K_iso_surf_00001871_*.stl'
pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/Sphere/*MBD*.stl'
folder, file = os.path.split(pattern)
file_list = sorted(glob.glob(pattern))

for _file in file_list:
    print(_file)
    # create a new 'STL Reader'
    my_file = STLReader(registrationName='my_file', FileNames=_file)

    UpdatePipeline(time=0.0, proxy=my_file)

    # create a new 'Integrate Variables'
    integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=my_file)

    UpdatePipeline(time=0.0, proxy=integrateVariables1)

    # save data
    SaveData(os.path.join(folder, '%s_surfaces.csv' % _file.replace(".stl", "")), 
        proxy=integrateVariables1,
        WriteTimeSteps=1,
        CellDataArrays=['Area'],
        FieldAssociation='Cell Data',
        AddMetaData=0)