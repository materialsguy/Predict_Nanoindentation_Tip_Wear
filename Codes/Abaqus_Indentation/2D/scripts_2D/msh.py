if tip_type == 1:
	a = mdb.models['Model-1'].rootAssembly
	partInstances =(a.instances['Part-2-1'], )
	a.seedPartInstance(regions=partInstances, size=0.01*tip_r, deviationFactor=0.1, minSizeFactor=0.1)
elif tip_type == 2:
	a = mdb.models['Model-1'].rootAssembly
	e1 = a.instances['Part-2-1'].edges
	pickedEdges = e1.getSequenceFromMask(mask=('[#2 ]', ), )
	a.seedEdgeBySize(edges=pickedEdges, size=0.01*tip_r, deviationFactor=indenter_mesh, constraint=FINER) # indnter tip
	a = mdb.models['Model-1'].rootAssembly
	e1 = a.instances['Part-2-1'].edges
	pickedEdges1 = e1.getSequenceFromMask(mask=('[#5 ]', ), )
	a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=indenter_rest_min, maxSize=indenter_rest_max, constraint=FINER) # other two lines
elif tip_type ==3:
	a = mdb.models['Model-1'].rootAssembly
	partInstances =(a.instances['Part-2-1'], )
	a.seedPartInstance(regions=partInstances, size=0.01*tip_r, deviationFactor=0.1, minSizeFactor=0.1)

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges2 = e1.getSequenceFromMask(mask=('[#42 ]', ), )
if 0.01*tip_r<0.04*3*indent_width:
	a.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=horizontal_min, maxSize=horizontal_max, constraint=FIXED) # horizontal fine
else:
	a.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=0.0025*3*indent_width, maxSize=0.035*3*indent_width, constraint=FINER)

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges1 = e1.getSequenceFromMask(mask=('[#81 ]', ), )
a.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=vertical_min, maxSize=vertical_max, constraint=FINER) #vertical fine

a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.seedPartInstance(regions=partInstances, size=rest_mesh, deviationFactor=0.1, minSizeFactor=0.1) # rest of the size

a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#2 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
pickedRegions = f1.getSequenceFromMask(mask=('[#1 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=TRI)
elemType1 = mesh.ElemType(elemCode=CAX4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CAX3, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-2-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
f2 = a.instances['Part-1-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#3 ]', ), )
pickedRegions =((faces1+faces2), )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances = (a.instances['Part-2-1'], )
a.generateMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)

elemType1 = mesh.ElemType(elemCode=CAX8, elemLibrary=STANDARD)	#R
elemType2 = mesh.ElemType(elemCode=CAX6, elemLibrary=STANDARD)	#M
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
pickedRegions = (faces1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
