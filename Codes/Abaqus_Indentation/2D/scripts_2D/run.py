def change_input_file(path, name):
	to_write = ['1, EE11, EE11','2, EE22, EE22', '3, EE33, EE33', '4, EE12, EE12', '5, EP11, EP11', '6, EP22, EP22', '7, EP33, EP33', '8, EP12, EP12', '9, PEEQ, PEEQ']
	with open("{}{}.inp".format(path, name), "r") as f:
		lines = f.readlines()
	for i, line in enumerate(lines):
		if line == "*Depvar\n":
			for j, element in enumerate(to_write):
				lines.insert(i+j+2, "{}\n".format(element))
	f.close()
	file = open("{}{}.inp".format(path, name), "w")
	for line in lines:
		file.write(line)


job_name = 'Sim_ID_%d' % model_n
mdb.Job(name='Sim_ID_%d' % model_n, model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='{}UMATPlasticity.f'.format(work_path), scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=n_CPU, numDomains=n_CPU, numGPUs=0)


mdb.jobs[job_name].writeInput()
del mdb.jobs['Sim_ID_%d' % model_n]
change_input_file(work_path, job_name)
mdb.JobFromInputFile(inputFileName="{}{}.inp".format(work_path, job_name), name=job_name, type=ANALYSIS,userSubroutine='{}UMATPlasticity.f'.format(work_path), numCpus=8, numDomains=8)

mdb.jobs['Sim_ID_%d' % model_n].submit(consistencyChecking=OFF)
mdb.jobs['Sim_ID_%d' % model_n].waitForCompletion()

test_file = os.path.exists('Sim_ID_%d' % model_n + '.sta')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.sta')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.log')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.log')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.sim')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.sim')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.msg')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.msg')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.prt')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.prt')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.com')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.com')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.inp')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.inp')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.dat')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.dat')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.mdl')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.mdl')

test_file = os.path.exists('Sim_ID_%d' % model_n + '.stt')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '.stt')

test_file = os.path.exists('Sim_ID_%d' % model_n + '_RESTART.zip')
if test_file:
	os.remove('Sim_ID_%d' % model_n + '_RESTART.zip')
