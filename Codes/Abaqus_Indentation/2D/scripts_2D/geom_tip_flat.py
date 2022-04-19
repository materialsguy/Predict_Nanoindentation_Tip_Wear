s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, 0.0), point2=(tip_r, 2*indent_depth))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-2']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#3 ]', ), )
p.Surface(side1Edges=side1Edges, name='Surf-tip')

p = mdb.models['Model-1'].parts['Part-2']
e = p.edges
edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
p.Set(edges=edges, name='Set-tip')