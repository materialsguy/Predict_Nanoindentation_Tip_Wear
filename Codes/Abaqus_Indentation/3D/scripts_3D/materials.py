mdb.models['Model-1'].Material(name='tip_mat')
mdb.models['Model-1'].materials['tip_mat'].Elastic(table=((tip_E, tip_nu),))

mdb.models['Model-1'].Material(name='specimen_mat')
mdb.models['Model-1'].materials['specimen_mat'].UserMaterial(
    mechanicalConstants=(specimen_E, specimen_nu, specimen_Sy, n))
mdb.models['Model-1'].materials['specimen_mat'].Depvar(n=13)

mdb.models['Model-1'].HomogeneousSolidSection(name='tip_sec', material='tip_mat', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='spec_sec', material='specimen_mat', thickness=None)

p = mdb.models['Model-1'].parts['Part-2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]',), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-2']
p.SectionAssignment(region=region, sectionName='tip_sec', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1']
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]',), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='spec_sec', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
                    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=1000000, initialInc=0.001, minInc=1e-50,
                                 maxInc=0.01, nlgeom=ON)
mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1', maxNumInc=10000000, initialInc=initial_increment_2,
                                 minInc=1e-50, maxInc=0.01)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(timeInterval=0.01)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(timeInterval=0.01)

if quad_ele != 1:
    mdb.models['Model-1'].AdaptiveMeshControl(name='Ada-1', smoothingAlgorithm=GEOMETRY_ENHANCED)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['Part-1-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#2 ]',), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['Model-1'].steps['Step-1'].AdaptiveMeshDomain(region=region, controls='Ada-1', frequency=ALE_freq)
