import numpy as np
mdb.models['Model-1'].Material(name='tip_mat')
mdb.models['Model-1'].materials['tip_mat'].Elastic(table=((tip_E, tip_nu), ))

mdb.models['Model-1'].Material(name='specimen_mat')
mdb.models['Model-1'].materials['specimen_mat'].UserMaterial(
    mechanicalConstants=(specimen_E, specimen_nu, specimen_Sy, n))
mdb.models['Model-1'].materials['specimen_mat'].Depvar(n=9)


mdb.models['Model-1'].HomogeneousSolidSection(name='tip_sec', material='tip_mat', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='spec_sec', material='specimen_mat', thickness=None)

p = mdb.models['Model-1'].parts['Part-2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(faces=faces)
p.SectionAssignment(region=region, sectionName='tip_sec', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3 ]', ), )
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='spec_sec', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0), point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)

mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=1000000000, initialInc=0.001, minInc=1e-27, maxInc=0.01, nlgeom=ON)

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(timeInterval=0.01)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=('IRF1', 'IRF2', 'IRF3', 'IRM1', 'IRM2', 'IRM3', 'ALLAE', 'ALLCD', 'ALLDMD', 'ALLEE', 'ALLFD', 'ALLIE', 'ALLJD', 'ALLKE', 'ALLKL', 'ALLPD', 'ALLQB', 'ALLSE', 'ALLSD', 'ALLVD', 'ALLWK', 'ETOTAL'), timeInterval=0.01)

mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1', maxNumInc=1000000000, initialInc=0.001, minInc=1e-27, maxInc=0.01, nlgeom=ON)
