import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

odb_name='/Sim_ID_%d' % model_n + '.odb'
session.mdbData.summary()
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o1 = session.openOdb(name=work_path + odb_name)
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
odb = session.odbs[work_path + odb_name]
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), nodeSets=('POINT', ))

xy1 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
xy2 = 6*xy1
xy2.setValues(sourceDescription='6 * "RF:RF2 PI: ASSEMBLY N: 1"')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'RF:RF2 PI: ASSEMBLY N: 6')

x0 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 6']
x1 = session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
session.writeXYReport(fileName='F-u_3D_ID_%d' % model_n + '.txt', appendMode=OFF, xyData=(x0, x1))
del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 6']
del session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
session.odbs[work_path + odb_name].close()
if save_odb==1:
	print("ODB saved")
else:
	pass
	#os.remove('Sim_3D_ID_%d' % model_n + '.odb')
