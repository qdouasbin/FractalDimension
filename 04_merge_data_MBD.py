import os
import glob
import numpy
from stl import mesh
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('~/cerfacs-black-ClearSans.mplstyle')

## OPTIONS
PLOT = 0
##########

res = {
	'delta': [],
	'surface': [],
}

if __name__ =="__main__":
	# pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/H2/*.stl'
	pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/Sphere/*MBD*.stl'
	for stl_file in sorted(glob.glob(pattern)):
		print(" > %s" % stl_file)
		str_delta = stl_file.split('_')[-2]
		delta_MBD = float(str_delta)

		# rule_size
		print(str_delta, delta_MBD)
		res['delta'].append(delta_MBD)

		# surfaces
		surface_file = stl_file.replace(".stl", '_surfaces.csv')
		df_surface = pd.read_csv(surface_file)
		print(df_surface)
		res['surface'].append(df_surface["Area"].values[0])

df_res = pd.DataFrame.from_dict(res)
print(df_res)

df_res.to_csv(pattern.replace("*MBD*.stl", "fractal_dimension_MBD.csv"), index=False)