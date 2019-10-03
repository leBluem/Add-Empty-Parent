this is forked from: @chebhou https://github.com/chebhou/Add-Empty-Parent

## Blender Addon to Add empty(ies) as Parent

The script creates an empty object and sets it as a parent for the selected objects. After installing you can trigger it with pressing <kbd>P</kbd>, you can change this shortcut in the user preferences later.

***How to install :***
 - goto Blender -> Edit -> preferences -> addons, select downloaded zip and click install

***How to use :***

 - select the objects
 - press <kbd>P</kbd>
 - property panel "Add empty as parent" should appear
 - select the Empty ***type*** ( axis, arrow, cube ...)
 - select the empty ***position*** ( world center, median point, at cursor, active object )
 - select whether to add one empty per object or only one with ***one parent per object***
 - set option to first set objects-center ***set origin to object first***
 - check ***parent inverse*** if you want to set the inverse
 - you can set the scaling of the empty in ***scale*** field
 - you can set the name of the empty in ***name*** field
 - to use names of selected objects as base set ***use childname***

***example***
note: all three planes were selected before, "P" on keyboard shows this
![Imgur Image](https://i.imgur.com/Q0b5HiX.jpg)
