bl_info = {
    "name": "Add an empty as parent",
    "author": "Chebhou, leBluem",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "description": "Adds a parent for the selected objects",
    "category": "Object"
}

import bpy
import sys
from bpy.props import BoolProperty, EnumProperty, StringProperty, FloatProperty

def add_parent(self, context):
    selected_obj = bpy.context.selected_objects.copy()
    if len(selected_obj)>0:

        if self.originFirst==1:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')

        if self.position != 'None' :
            exec("bpy.ops.view3d.snap_cursor_to_%s()"%self.position)

        if self.individuell==0:
            bpy.ops.object.empty_add(type = self.type)
            bpy.ops.transform.resize(value=(self.scaling, self.scaling, self.scaling))
            if self.usechildname==1:
                bpy.context.object.name = selected_obj[0].name + self.name
            else:
                bpy.context.object.name = self.name
            # bpy.ops.transform.resize(value=(self.scaling, self.scaling, self.scaling))
            # bpy.ops.transform.resize(value=(self.scaling, self.scaling, self.scaling))
            inv_mat = bpy.context.object.matrix_world.inverted()
            for obj in selected_obj :
                obj.parent = bpy.context.object
                if self.inverse :
                    obj.matrix_parent_inverse = inv_mat
        else:
            cnt=0
            for obj in selected_obj :
                bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
                bpy.ops.object.empty_add(type = self.type, location=obj.location)
                bpy.ops.transform.resize(value=(self.scaling, self.scaling, self.scaling))
                if self.usechildname==1:
                    bpy.context.object.name = selected_obj[0].name + self.name
                else:
                    bpy.context.object.name = self.name + str(cnt)
                inv_mat = bpy.context.object.matrix_world.inverted()
                obj.parent = bpy.context.object
                if self.inverse :
                    obj.matrix_parent_inverse = inv_mat
                cnt=cnt+1
    else:
        print('Nothing selected!')

class AddEmptyAsParent(bpy.types.Operator):
    """Create a new parent"""
    bl_idname = "object.add_parent"
    bl_label = "Add empty as parent"
    bl_options = {'REGISTER', 'UNDO'}

    type  = EnumProperty(
        name="empty type",
        description="choose the empty type",
        items=(('PLAIN_AXES', "Axis", "Axis"),
                ('ARROWS', "Arrows", "Arrows"),
                ('SINGLE_ARROW', "Single arrow", "Single arrow"),
                ('CIRCLE', "Circle", "Circle"),
                ('CUBE', "Cube", "Cube"),
               ('SPHERE', "Sphere", "Sphere"),
               ('CONE', "Cone", "Cone")),
        default='PLAIN_AXES'
        )

    position  = EnumProperty(
        name="parent position",
        description="where to create the parent",
        items=(('center', "World center", "World center"),
                ('None', "Cursor position", "Cursor position"),
                ('selected', "Median point", "Median position"),
                ('active', "Active object position", "Active position"),),
        default='active'
        )

    individuell = BoolProperty(
        name = "one parent per object",
        default = 1,
        description = "uncheck to set one parent for all selected"
        )

    originFirst = BoolProperty(
        name = "set origin to object first",
        default = 1,
        description = "uncheck to keep object origins"
        )

    inverse = BoolProperty(
        name = "parent inverse",
        default = 1,
        description = "uncheck to set to center"
        )

    scaling     = FloatProperty(
        name="Scaling",
        description="Scaling of Empty",
        min=0.0,
        max=100.0,
        # unit='SIZE',
        default=0.01
        )

    name      = StringProperty(
        name ="name",
        default ="AC_POBJECT_")

    usechildname = BoolProperty(
        name = "use childname",
        default = 0,
        description = "check to use objectname + string above as empty name"
        )

    def execute(self, context):
        add_parent(self, context)
        return {'FINISHED'}


addon_keymaps = []

# Register
classes = [
    AddEmptyAsParent
]

def register():
    bpy.utils.register_class(AddEmptyAsParent)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        # you can chnge the shortcut later
        kmi = km.keymap_items.new(AddEmptyAsParent.bl_idname, 'P', 'PRESS')
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(AddEmptyAsParent)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
