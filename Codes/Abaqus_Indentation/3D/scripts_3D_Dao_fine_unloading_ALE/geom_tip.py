s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s1.FixedConstraint(entity=g[2])
s1.ArcByCenterEnds(center=(0.0, tip_r), point1=(0.0, 0.0), point2=(tip_r/2, tip_r/2), direction=COUNTERCLOCKWISE)
s1.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s1.FixedConstraint(entity=v[0])
s1.Line(point1=(tip_r,tip_r), point2=(2*tip_r,2*tip_r))
s1.Line(point1=(2*tip_r,2*tip_r), point2=(0.0, 2*tip_r))
s1.HorizontalConstraint(entity=g[5], addUndoState=False)
s1.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
s1.Line(point1=(0.0, 2*tip_r), point2=(0.0, 0.0))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.CoincidentConstraint(entity1=v[3], entity2=v[1])
s1.TangentConstraint(entity1=g[3], entity2=g[4])
s1.AngularDimension(line1=g[4], line2=g[2], textPoint=(10.0180740356445, 13.1899108886719), value=90-12.5)

test_d=tip_r-(tip_r*cos(numpy.deg2rad(12.95)))
if indent_depth > test_d:
	tip_height=1.5*indent_depth
else:
	tip_height=1.5*test_d

s1.DistanceDimension(entity1=g[5], entity2=v[0], textPoint=(-17.4926872253418, 12.8783416748047), value=tip_height)
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
#p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidRevolve(sketch=s1, angle=120.0, flipRevolveDirection=OFF)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-2']
v2 = p.vertices
p.DatumPlaneByThreePoints(point1=v2[1], point2=v2[2], point3=v2[3])
p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d2 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d2[2], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-2']
f1 = p.faces
p.RemoveFaces(faceList = f1[2:3]+f1[4:6], deleteCells=False)
p = mdb.models['Model-1'].parts['Part-2']
f, d1 = p.faces, p.datums
p.DatumPlaneByRotation(plane=f[3], axis=d1[1], angle=-60.0)

p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
d2 = p.datums
p.PartitionCellByDatumPlane(datumPlane=d2[5], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-2']
f1 = p.faces
p.RemoveFaces(faceList = f1[2:3]+f1[4:5]+f1[6:8], deleteCells=False)
p = mdb.models['Model-1'].parts['Part-2']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#c ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-tip')
p = mdb.models['Model-1'].parts['Part-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(faces=faces, name='Set-tip')
