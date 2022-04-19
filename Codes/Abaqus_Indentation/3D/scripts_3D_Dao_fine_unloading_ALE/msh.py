a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-2-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-2-1'].cells
cells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#144 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=indenter_fine, deviationFactor=0.1, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#88 ]', ), )
pickedEdges2 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, end2Edges=pickedEdges2, minSize=indenter_fine, maxSize=60*indenter_fine, constraint=FINER)

elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)

a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-2-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-2-1'], )
a.generateMesh(regions=partInstances)

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#18000 ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=num_round, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#22020 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=fine_depth, deviationFactor=0.1, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#800010 ]', ), )
pickedEdges2 = e1.getSequenceFromMask(mask=('[#44000 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, end2Edges=pickedEdges2, minSize=fine_min, maxSize=fine_max, constraint=FINER)

a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#2 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=HEX_DOMINATED, technique=SWEEP, algorithm=MEDIAL_AXIS)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#2 ]', ), )
a.generateMesh(regions=pickedRegions)

# rest
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#100100 ]', ), )
pickedEdges2 = e1.getSequenceFromMask(mask=('[#400 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, end2Edges=pickedEdges2, minSize=rest_depth_min, maxSize=rest_depth_max, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#7 ]', ), )
a.seedEdgeBySize(edges=pickedEdges, size=rest_mesh, deviationFactor=0.1, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#4 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=HEX_DOMINATED, technique=SWEEP, algorithm=MEDIAL_AXIS)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#4 ]', ), )
a.generateMesh(regions=pickedRegions)

a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
a.generateMesh(regions=pickedRegions)

elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#7 ]', ), )
c2 = a.instances['Part-2-1'].cells
cells2 = c2.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =((cells1+cells2), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))

if quad_ele==1:
	elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
	a = mdb.models['Model-1'].rootAssembly
	c1 = a.instances['Part-1-1'].cells
	cells1 = c1.getSequenceFromMask(mask=('[#2 ]', ), )
	pickedRegions =(cells1, )
	a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))
else:
	elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
	elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
	elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)
	a = mdb.models['Model-1'].rootAssembly
	c1 = a.instances['Part-1-1'].cells
	cells1 = c1.getSequenceFromMask(mask=('[#2 ]', ), )
	pickedRegions =(cells1, )
	a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))

# workaround by Claus
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(mesh.ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=ENHANCED,
    distortionControl=DEFAULT), mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD,
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), mesh.ElemType(
    elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
    distortionControl=DEFAULT)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].cells.getSequenceFromMask(
    ('[#4 ]', ), ), ))
