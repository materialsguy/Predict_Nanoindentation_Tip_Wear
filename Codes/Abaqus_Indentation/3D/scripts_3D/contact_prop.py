mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON, contactStiffness=DEFAULT, contactStiffnessScaleFactor=1.0, clearanceAtZeroContactPressure=0.0, stiffnessBehavior=LINEAR, constraintEnforcementMethod=PENALTY)
a = mdb.models['Model-1'].rootAssembly
region1=a.instances['Part-1-1'].surfaces['Surf-spec']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['Part-2-1'].surfaces['Surf-tip']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', createStepName='Step-1', master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(11*indent_width, 1.0, 0.0))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
a.Set(referencePoints=refPoints1, name='point')
mdb.models['Model-1'].Equation(name='Constraint-1', terms=((1.0, 'Part-2-1.Set-tip', 3), (-1.0, 'point', 3)))
mdb.models['Model-1'].Equation(name='Constraint-2', terms=((1.0, 'Part-1-1.Set-spec', 1), (-1.0, 'point', 1)))
