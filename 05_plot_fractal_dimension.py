import os
import glob
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt 
import pandas as pd
#plt.style.use('~/cerfacs-black-ClearSans.mplstyle')
plt.style.use('bmh')

## OPTIONS
PLOT = 0
radius = 1.0
area = 4.0 * np.pi * radius**2
##########

if __name__ =="__main__":
	# file_fd = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/H2/fractal_dimension.csv'
	file_fd = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/Sphere/fractal_dimension.csv'
	file_fd_mbd = '/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/output/Sphere/fractal_dimension_MBD.csv'

	df_fd = pd.read_csv(file_fd)
	df_fd_mbd = pd.read_csv(file_fd_mbd)

	plt.figure()
	# plt.loglog(df_fd.delta, df_fd.surface / df_fd.surface.max(), '-o', label='box')
	plt.loglog(df_fd.delta, df_fd.surface / area, '-o', label='box')
	# plt.loglog(df_fd_mbd.delta, df_fd_mbd.surface / df_fd_mbd.surface.max(), '--x', label='Merge by distance')
	plt.loglog(df_fd_mbd.delta, df_fd_mbd.surface / area, '--x', label='Merge by distance')
	plt.xlabel(r"$\Delta [m]$")
	plt.ylabel(r"$\frac{S}{S_{\rm max}} [-]$")
	plt.legend()
	plt.tight_layout()
	plt.savefig(file_fd.replace(".csv", ".png"))

	plt.figure()
	plt.plot(df_fd.delta, df_fd.surface, '-o', label='box')
	plt.semilogx(df_fd_mbd.delta, df_fd_mbd.surface, '--x', label='Merge by distance')
	plt.plot(df_fd_mbd.delta, area * np.ones_like(df_fd_mbd.delta), ':', label=r'$A = 4 \pi r^2$')
	plt.xlabel(r"$\Delta [m]$")
	plt.ylabel(r"$S$ [m$^2$]")
	plt.legend()
	plt.tight_layout()
	plt.savefig(file_fd.replace(".csv", "_surface.png"))

	plt.figure()
	frac_dim = np.gradient(np.log(df_fd.surface), np.log(df_fd.delta))
	frac_dim_mbd = np.gradient(np.log(df_fd_mbd.surface), np.log(df_fd_mbd.delta))
	plt.semilogx(df_fd.delta, frac_dim, '-o')
	plt.semilogx(df_fd_mbd.delta, frac_dim_mbd, '--x', label='Merge by distance')
	plt.xlabel(r"$\Delta [m]$")
	plt.ylabel(r"$\frac{\partial\log(S)}{\partial \log(\Delta)} [-]$")
	plt.tight_layout()
	plt.savefig(file_fd.replace(".csv", "_FD.png"))

	plt.show()
