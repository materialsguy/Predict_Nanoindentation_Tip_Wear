from abaqus import *
from abaqus import *
from abaqus import *
from abaqusConstants import *
import __main__
import os
import os.path
import csv
import numpy as np
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

Mdb()

work_path = '/define/your/path/'  # path to the work directory, see readme_2D.txt

#######################################################################################################################

os.chdir(work_path)

a = np.loadtxt(open("input_data_2D.csv", "rb"), delimiter=",", skiprows=1)
input_data = np.asmatrix(a)
numrows = len(input_data)

############### Fine unloading parameters ###############

fine_portion = 0.15  # portion of the unloading step to have fine results, must be between 0 and 1
fine_substeps = 50  # number of substeps for results in fine unloading step
rough_substeps = 50  # number of substeps for results in the rest of unloading step

#########################################################

test_file = os.path.exists('sims_check.txt')
if test_file:
	os.remove('sims_check.txt')

for i in range(1, numrows+1):
	Mdb()
	model_n = input_data[i-1, 0]		# ID
	tip_type = input_data[i-1, 1]		# 1 for ball tip, 2 for cone tip
	tip_r = input_data[i-1, 2]			# tip radius in um
	cone_angle = input_data[i-1, 3]		# angle of cone tip
	t = input_data[i-1, 4]			# specimen thickness in um
	tip_E = input_data[i-1, 5]		# tip Youngs modulus in MPa
	tip_nu = input_data[i-1, 6]				# tip Poissons ratio
	specimen_E = input_data[i-1, 7] 	# specimen Youngs modulus in MPa
	specimen_nu = input_data[i-1, 8]		# specimen Poissons ratio
	specimen_Sy = input_data[i-1, 9]  # specimen yield stress in MPa
	n = input_data[i-1, 10] 	# specimen n (model from Dao)
	indent_depth = input_data[i-1, 11]  # indentation depth in um
	n_CPU = input_data[i-1, 12]		# number of CPU cores used for simulation
	save_odb = input_data[i-1, 13]

	if tip_type == 2:
		indent_width = indent_depth/(tan(np.deg2rad(90-cone_angle)))
	else:
		indent_width = tip_r

	# Define Meshing Parameters:

	'''original by Stanislav:
	# Define indenter Meshing Parameters
	indenter_mesh = tip_r
	indenter_rest_min = 0.03*tip_r
	indenter_rest_max = tip_r
	# Define fine part of indentet model
	horizontal_min = 0.01*tip_r
	horizontal_max = 0.04*3*indent_width
	vertical_min = 0.025*indent_depth
	vertical_max = 0.075*indent_depth
	# Rest of the model
	rest_mesh = 1.0
	'''
	horizontal_min = 0.075*tip_r
	horizontal_max = 0.5*indent_width
	indenter_mesh = tip_r*1.1

	# Define Indenter Meshing Parameters

	indenter_rest_min = 0.03*tip_r
	indenter_rest_max = tip_r*0.9

	# Define fine part of bulk model

	vertical_min = 0.025*indent_depth
	vertical_max = 0.075*indent_depth
	# Rest of the model
	rest_mesh = 1.5

	execfile(work_path + '/scripts_2D/geom_specimen.py', __main__.__dict__)

	if tip_type == 1:
		execfile(work_path + '/scripts_2D/geom_tip_ball.py', __main__.__dict__)
	elif tip_type == 2:
		execfile(work_path + '/scripts_2D/geom_tip_cone.py', __main__.__dict__)
	elif tip_type == 3:
		execfile(work_path + '/scripts_2D/geom_tip_flat.py', __main__.__dict__)

	execfile(work_path + '/scripts_2D/materials.py', __main__.__dict__)

	execfile(work_path + '/scripts_2D/contact_prop.py', __main__.__dict__)

	execfile(work_path + '/scripts_2D/load.py', __main__.__dict__)

	execfile(work_path + '/scripts_2D/msh.py', __main__.__dict__)

	execfile(work_path + '/scripts_2D/run.py', __main__.__dict__)

	try:
		execfile(work_path + '/scripts_2D/results.py', __main__.__dict__)

		execfile(work_path + '/scripts_2D/sim_check.py', __main__.__dict__)

	except:
		print('Simulation was not finished')