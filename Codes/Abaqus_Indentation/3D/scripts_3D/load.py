a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['Part-2-1'].vertices
a.DatumCsysByThreePoints(origin=v11[1], point1=v11[4], point2=v11[0], name='Datum csys-2', coordSysType=CYLINDRICAL)
mdb.models['Model-1'].constraints['Constraint-1'].setValues(terms=((1.0, 'Part-2-1.Set-tip', 3, 9), (-1.0, 'point', 3, 9)))
mdb.models['Model-1'].constraints['Constraint-2'].setValues(terms=((1.0, 'Part-1-1.Set-spec', 1, 9), (-1.0, 'point', 1, 9)))

a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#400 ]', ), )
region = regionToolset.Region(faces=faces1)
datum = mdb.models['Model-1'].rootAssembly.datums[9]
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=datum)

a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#314a ]', ), )
f2 = a.instances['Part-2-1'].faces
faces2 = f2.getSequenceFromMask(mask=('[#11 ]', ), )
region = regionToolset.Region(faces=faces1+faces2)
datum = mdb.models['Model-1'].rootAssembly.datums[9]
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', region=region, u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=datum)

a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
region = regionToolset.Region(referencePoints=refPoints1)
datum = mdb.models['Model-1'].rootAssembly.datums[9]
mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', region=region, u1=UNSET, u2=UNSET, u3=indent_depth, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=datum)
mdb.models['Model-1'].boundaryConditions['BC-3'].setValuesInStep(stepName='Step-2', u3=(1-fine_portion)*indent_depth)
mdb.models['Model-1'].boundaryConditions['BC-3'].setValuesInStep(stepName='Step-3', u3=0.0)

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-2-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
e2 = a.instances['Part-1-1'].edges
edges2 = e2.getSequenceFromMask(mask=('[#120008 ]', ), )
region = regionToolset.Region(edges=edges1+edges2)
datum = mdb.models['Model-1'].rootAssembly.datums[9]
mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Initial', region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=datum)