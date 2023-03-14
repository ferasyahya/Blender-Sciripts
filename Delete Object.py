import bpy

class DeleteObjectButton(bpy.types.Panel):
    bl_label = "Delete Object"
    bl_idname = "OBJECT_PT_delete"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.delete", text="Delete Selected Object")

def register():
    bpy.utils.register_class(DeleteObjectButton)

def unregister():
    bpy.utils.unregister_class(DeleteObjectButton)

if __name__ == "__main__":
    register()