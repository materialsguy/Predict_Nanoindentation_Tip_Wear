s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(viewStyle=AXISYM)
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s1.FixedConstraint(entity=g[2])
s1.ArcByCenterEnds(center=(0.0, tip_r), point1=(0.0, 0.0), point2=(tip_r, tip_r), direction=COUNTERCLOCKWISE)
s1.Line(point1=(tip_r, tip_r), point2=(0.0, tip_r))
s1.Line(point1=(0.0, tip_r), point2=(0.0, 0.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-2']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#2 ]', ), )
p.Surface(side1Edges=side1Edges, name='Surf-tip')

p = mdb.models['Model-1'].parts['Part-2']
e = p.edges
edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(edges=edges, name='Set-tip')