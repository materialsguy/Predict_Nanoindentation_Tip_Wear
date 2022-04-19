s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, 0.0), point2=(5*indent_width, -t))# radus of the whole model
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidRevolve(sketch=s, angle=60.0, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[3], sketchUpEdge=e[0], sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=316.22, gridSpacing=7.9, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
#s1.rectangle(point1=(0.0,0.0), point2=(indent_width, -1.25*indent_depth))#radius/dpth of the fine volume
s1.rectangle(point1=(0.0,0.0), point2=(indent_width, -2*indent_depth))#radius/dpth of the fine volume 14
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#8 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[0], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], e[1])
p.PartitionCellBySweepEdge(sweepPath=e[8], cells=pickedCells, edges=pickedEdges)
p = mdb.models['Model-1'].parts['Part-1']
v1 = p.vertices
p.DatumPlaneByThreePoints(point1=v1[0], point2=v1[2], point3=v1[1])
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
d1 = p.datums
#p.PartitionCellByDatumPlane(datumPlane=d1[4], cells=pickedCells)

p = mdb.models['Model-1'].parts['Part-1']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#80 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-spec')

p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#20 ]', ), )
p.Set(faces=faces, name='Set-spec')

p = mdb.models['Model-1'].parts['Part-1']
d = p.datums
p.DatumPlaneByOffset(plane=d[4], flip=SIDE2, offset=2.0)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
d1 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d1[7], cells=pickedCells)
