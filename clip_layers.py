import processing

# Load the clipping mask
mainLayerFolder = "//TP-Share/G/Documents/GIS/Danderyd/Surveying/18276"
mask = mainLayerFolder + "/mask.shp"

# Output folder
clipFolder = mainLayerFolder + "/clip/"
styleFolder = clipFolder + "/styles/"

# Create a group to store the results
root = QgsProject.instance().layerTreeRoot()
shapeGroup = root.addGroup("clippedGroup")

# Group to clip
groupName = "Topografi 10"
groupToClip = root.findGroup(groupName)
layers = [child.layer() for child in groupToClip.children()]

# Clip each layer according to the mask, and keep their styles
# They are read in reverse order as they are processed in a FILO manner.
for layer in layers[::-1]:
    print("Clipping " + layer.name())
    # Save the styles onto a new folder
    layerStylePath = styleFolder + layer.name() + ".qml"
    layer.saveNamedStyle(layerStylePath)
    
    # Clip and save the result onto a new folder
    clipName = layer.name() + "_clip"
    clipPath = clipFolder + clipName
    processing.run("native:clip", {"INPUT": layer, "OVERLAY": mask, "OUTPUT": clipPath})
    
    # Open the clipped file and apply the saved style to it
    vlayer = QgsVectorLayer(clipPath+".gpkg", clipName, "ogr")
    vlayer.loadNamedStyle(layerStylePath)
    QgsProject.instance().addMapLayer(vlayer)
    
    # Copy the clipped file to the clipedGroup
    layer = root.findLayer(vlayer.id())
    clone = layer.clone()
    shapeGroup.insertChildNode(0, clone)
    
    # Delete the previously imported clipped file from it original group
    topo_group = root.findGroup(groupName)
    group = topo_group.findGroup(clipName)
    if group is not None:
        topo_group.removeChildNode(group)
    
    topo_group.removeChildNode(layer)

