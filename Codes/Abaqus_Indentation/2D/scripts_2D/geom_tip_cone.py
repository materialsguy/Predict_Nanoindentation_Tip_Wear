s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.ArcByCenterEnds(center=(0.0, tip_r), point1=(0.0, 0.0), point2=(tip_r, 0.75*tip_r), direction=COUNTERCLOCKWISE)
s.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s.Line(point1=(tip_r+1, 0.75*tip_r+1), point2=(tip_r+2, 0.75*tip_r+2))
s.CoincidentConstraint(entity1=v[3], entity2=v[1])
s.TangentConstraint(entity1=g[4], entity2=g[3])
s.AngularDimension(line1=g[4], line2=g[2], textPoint=(3.87156867980957, 15.783878326416), value=cone_angle)

if 5*tip_r > 3*indent_depth:
	tip_length=5*tip_r
else:
	tip_length=3*indent_depth

s.Line(point1=(0.0, 0.0), point2=(0.0, tip_length))
s.VerticalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
s.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, tip_length), point2=(tip_r, tip_length))
s.HorizontalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.FixedConstraint(entity=v[5])
s.CoincidentConstraint(entity1=v[4], entity2=v[6])

p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-2']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#8 ]', ), )
p.Set(edges=edges, name='Set-tip')

p = mdb.models['Model-1'].parts['Part-2']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#6 ]', ), )
p.Surface(side1Edges=side1Edges, name='Surf-tip')


