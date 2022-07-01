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

def output_rule_size(stl_file):
	# Using an existing stl file:
	your_mesh = mesh.Mesh.from_file(stl_file)
	# data_mesh = your_mesh.centroids
	data_mesh = your_mesh.v0
	data_mesh.shape
	x = data_mesh[:, 0]
	unique_x = numpy.array(sorted(list(set(numpy.round_(x, decimals=6)))))

	delta = numpy.mean(numpy.diff(unique_x))
	print(" > mean: %e" % delta)

	dict_out = {
		"delta": [delta]
	}

	df = pd.DataFrame.from_dict(dict_out)
	csv_path = stl_file.replace('.stl', '_rule_size.csv')
	df.to_csv(csv_path, index=False)

	if PLOT or  "005" in stl_file:
		plt.figure()
		plt.plot(numpy.diff(unique_x), 'o', label="Measured dx")
		plt.plot(delta * numpy.ones_like(numpy.diff(unique_x)), '--', label="mean dx")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.legend()

		plt.figure()
		plt.title(stl_file.split("/")[-1])
		y = data_mesh[:, 1]
		plt.plot(x, y, 'x')
		# plt.plot(x - numpy.min(x), y, 'x')
		plt.xlabel("x")
		plt.ylabel("y")
		plt.show()

if __name__ =="__main__":
	# stl_file = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/H2/isosurf_T1120K_iso_surf_00001871_0006.stl'
	# output_rule_size(stl_file)

	pattern = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/*/*.stl'
	for stl_file in sorted(glob.glob(pattern)):
		print(" > %s" % stl_file)
		output_rule_size(stl_file)