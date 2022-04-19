import shutil


def change_input_file(path, name):
	to_write = ['1, EE11, EE11','2, EE22, EE22', '3, EE33, EE33', '4, EE12, EE12', '5, EE13, EE13', '6, EE23, EE23', '7, EP11, EP11', '8, EP22, EP22', '9, EP33, EP33', '10, EP12, EP12', '11, EP13, EP13','12, EP23, EP23','13, PEEQ, PEEQ']
	with open("{}{}.inp".format(path, name), "r") as f:
		lines = f.readlines()
	for i, line in enumerate(lines):
		if line == "*Depvar\n":
			for j, element in enumerate(to_write):
				lines.insert(i+j+2, "{}\n".format(element))
	f.close()
	file=open("{}{}.inp".format(path, name),"w")
	for line in lines:
		file.write(line)


if not os.path.exists('sc_1'):
	os.makedirs('sc_1')

job_name = 'Sim_ID_%d' % model_n
mdb.Job(name=job_name, model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='{}UMATPlasticity.f'.format(work_path), scratch=work_path + '/sc_1', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=n_CPU, numDomains=n_CPU, numGPUs=0)

mdb.jobs[job_name].writeInput()
del mdb.jobs[job_name]
change_input_file(work_path, job_name)
mdb.JobFromInputFile(inputFileName="{}{}.inp".format(work_path, job_name), name=job_name, type=ANALYSIS, userSubroutine='{}UMATPlasticity.f'.format(work_path), numCpus=12, numDomains=12)

mdb.jobs[job_name].submit(consistencyChecking=OFF)
mdb.jobs[job_name].waitForCompletion()

shutil.rmtree('sc_1', ignore_errors=True)


test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.sta')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.sta')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.log')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.log')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.sim')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.sim')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.msg')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.msg')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.prt')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.prt')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.com')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.com')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.inp')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.inp')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.dat')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.dat')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.mdl')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.mdl')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '.stt')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '.stt')

test_file = os.path.exists('Sim_3D_ID_%d' % model_n + '_RESTART.zip')
if test_file:
	os.remove('Sim_3D_ID_%d' % model_n + '_RESTART.zip')
