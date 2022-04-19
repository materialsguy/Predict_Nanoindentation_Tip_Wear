a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#8 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[6], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', region=region, u1=UNSET, u2=-indent_depth, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)

mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-2', u2=(1-fine_portion)*(-indent_depth))
mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-3', u2=0.0)

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#84 ]', ), )
e2 = a.instances['Part-2-1'].edges
edges2 = e2.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(edges=edges1+edges2)
mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Initial', region=region, u1=SET, u2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)