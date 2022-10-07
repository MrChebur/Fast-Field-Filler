# Fast-Field-Filler
The plugin was created to quickly fill in the fields in the attribute table. It allows you to specify a layer, a field in its attribute table and fill all selected objects with a preset value.
 
For example, this plugin may be useful:
- If you check the results of the neural network by dividing selected objects into two classes: correctly selected objects (True), falsely selected objects (False).
- If you classify thermal spots detected by remote sensing data and divide all objects into: fires, anthropogenic heat sources, false alarms.


# Plugin features:
- Set from 1 to 10 preset class values.
- Save and load the values you need in a Json format file.
- Assign hotkeys (limited choice) to quickly fill the attribute table with the desired values.
- Set a limit on the maximum selection of objects ( to avoid accidentally overwriting everything).
- Buttons to save results and rollback changes.

# Example workflow:
![Example workflow](https://raw.githubusercontent.com/MrChebur/Fast-Field-Filler/cc74210b4dd34a49fceaaa0bade4d97984bb8540/examples/Plugin%20work%20example.gif)
