test_file = os.path.exists('F-u_ID_%d' % model_n + '.txt')

if test_file:
	f = open('F-u_ID_%d' % model_n + '.txt')
	lines = f.readlines()
	lines_n = len(lines)
	last_line = lines[lines_n-5]
	
	f = open("sims_check.txt", "a+")
	f.write('Sim ID: %d' % model_n + last_line)
	f.close()