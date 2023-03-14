import bpy
import random

class AddRandomObjectButton(bpy.types.Panel):
    bl_label = "Add Random Object"
    bl_idname = "OBJECT_PT_add_random_object"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.add_random_object", text="Add Random Object")

class OBJECT_OT_add_random_object(bpy.types.Operator):
    bl_idname = "object.add_random_object"
    bl_label = "Add Random Object"

    def execute(self, context):
        objects = ['Cube', 'Sphere', 'Cone', 'Cylinder'] # List of objects to choose from
        selected_object = random.choice(objects) # Choose a random object from the list
        
        if selected_object == 'Cone':
            bpy.ops.mesh.primitive_cone_add()
        elif selected_object == 'Sphere':
            bpy.ops.mesh.primitive_uv_sphere_add()
        elif selected_object == 'Cylinder':
            bpy.ops.mesh.primitive_cylinder_add()
        else:
            bpy.ops.mesh.primitive_cube_add()
        

            
        return {'FINISHED'}

def register():
    bpy.utils.register_class(AddRandomObjectButton)
    bpy.utils.register_class(OBJECT_OT_add_random_object)

def unregister():
    bpy.utils.unregister_class(AddRandomObjectButton)
    bpy.utils.unregister_class(OBJECT_OT_add_random_object)

if __name__ == "__main__":
    register()