import bpy

def import_stl(filepath):
  bpy.ops.import_mesh.stl(filepath=filepath)

def clean_worksapce():
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete(use_global=False)

if __name__ == "__main__":
  clean_worksapce()
  # STL_FILE = "/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/input/H2/isosurf_T1120K_iso_surf_00001871.stl"
  STL_FILE = "/Users/qdouasbin/share/kraken/received/FractalDimension/Blender/input/Sphere/sphere.stl"
  import_stl(STL_FILE)

  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.modifier_add(type='REMESH')
  bpy.context.object.modifiers["Remesh"].mode = 'BLOCKS'
  bpy.context.object.modifiers["Remesh"].scale = 0.5
  bpy.context.object.modifiers["Remesh"].threshold = 1

  for _octree_depth in range(5, 11, 1):
      bpy.context.object.modifiers["Remesh"].octree_depth = _octree_depth
      stl_out_path = STL_FILE.replace("input", "output").replace(".stl", "_%04d.stl" % _octree_depth)
      bpy.ops.export_mesh.stl(filepath=stl_out_path, check_existing=False, filter_glob="*.stl", 
                              use_selection=True, global_scale=1, use_scene_unit=False, 
                              ascii=False, use_mesh_modifiers=True, batch_mode='OFF', 
                              axis_forward='Y', axis_up='Z')