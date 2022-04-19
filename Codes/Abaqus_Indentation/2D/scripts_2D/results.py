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

session.mdbData.summary()
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o1 = session.openOdb(name=work_path + '/Sim_ID_%d' % model_n + '.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
odb = session.odbs[work_path + '/Sim_ID_%d' % model_n + '.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', NODAL, ((COMPONENT, 'RF2'), )), ('U', NODAL, ((COMPONENT, 'U2'), )), ), nodeSets=('POINT', ))
x0 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
x1 = session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
session.writeXYReport(fileName='F-u_ID_%d' % model_n + '.txt', appendMode=OFF, xyData=(x0, x1))
del session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: 1']
del session.xyDataObjects['U:U2 PI: ASSEMBLY N: 1']
session.odbs[work_path + '/Sim_ID_%d' % model_n + '.odb'].close()
if save_odb == 1:
	print("ODB saved")
else:
	os.remove('Sim_ID_%d' % model_n + '.odb')