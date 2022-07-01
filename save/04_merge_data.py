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
	pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/Sphere/*.stl'
	for stl_file in sorted(glob.glob(pattern)):
		print(" > %s" % stl_file)

		# rule_size
		delta_file = stl_file.replace(".stl", '_rule_size.csv')
		df_delta = pd.read_csv(delta_file)
		print(df_delta)
		res['delta'].append(df_delta["delta"].values[0])

		# surfaces
		surface_file = stl_file.replace(".stl", '_surfaces.csv')
		df_surface = pd.read_csv(surface_file)
		print(df_surface)
		res['surface'].append(df_surface["Area"].values[0])

df_res = pd.DataFrame.from_dict(res)
print(df_res)

df_res.to_csv(pattern.replace("*.stl", "fractal_dimension.csv"), index=False)