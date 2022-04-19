s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, 0.0), point2=(35*indent_width, -t))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-1']
f, e, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=181.1, gridSpacing=4.52, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.rectangle(point1=(0.0, 0.0), point2=(3*indent_width, -4*indent_depth))# size of the fine area
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#60 ]', ), )
p.Surface(side1Edges=side1Edges, name='Surf-spec')

#p = mdb.models['Model-1'].parts['Part-1']
#s = p.edges
#side1Edges = s.getSequenceFromMask(mask=('[#1 ]', ), )
#p.Surface(side1Edges=side1Edges, name='Surf-spec')

#p = mdb.models['Model-1'].parts['Part-1']
#e = p.edges
#edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
#p.Set(edges=edges, name='Set-spec')
