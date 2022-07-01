import bpy
import numpy as np

def import_stl(filepath):
  bpy.ops.import_mesh.stl(filepath=filepath)

def clean_workspace():
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete(use_global=False)

def merge_by_distance(stl_file, distance=0.1):
  clean_workspace()
  import_stl(stl_file)
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.editmode_toggle()
  # bpy.ops.mesh.remove_doubles()
  # bpy.data.window_managers["WinMan"].(null) = distance
  bpy.ops.mesh.remove_doubles(threshold=distance)
  bpy.ops.object.editmode_toggle()
  bpy.ops.object.select_all(action='SELECT')
  # bpy.context.space_data.recent_folders_active = 2
  # bpy.context.space_data.params.filename = "sphere_MBD_dist_0.10000m.stl"

  stl_out_path = STL_FILE.replace("input", "output").replace(".stl", "_MBD_%f_.stl" % distance)

  bpy.ops.export_mesh.stl(filepath=stl_out_path, check_existing=False, filter_glob="*.stl", 
                          use_selection=True, global_scale=1, use_scene_unit=False, 
                          ascii=False, use_mesh_modifiers=True, batch_mode='OFF', 
                          axis_forward='Y', axis_up='Z')
  return

if __name__ == "__main__":
  clean_workspace()
  # # STL_FILE = "/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/input/H2/isosurf_T1120K_iso_surf_00001871.stl"
  STL_FILE = "/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/input/Sphere/sphere.stl"
  
  # In meters
  distance_min = 0.001
  distance_max = 0.95
  n_steps = 40

  for distance in np.logspace(np.log10(distance_min), np.log10(distance_max), n_steps):
    print("Merge by distance: %e" % distance)
    merge_by_distance(STL_FILE, distance)
    # merge_by_distance(STL_FILE, 0.1)



