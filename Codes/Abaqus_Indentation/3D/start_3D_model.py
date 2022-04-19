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
work_path = 'define/your/path'		# path to the work directory
##################################################################################
os.chdir(work_path)
a = np.loadtxt(open("input_data_3D.csv", "rb"), delimiter=",", skiprows=1)
input_data = np.asmatrix(a)
numrows = len(input_data)
############### Fine unloading parameters ###############
fine_portion = 0.15	 # portion of the unloading step to have fine results, must be between 0 and 1
fine_substeps = 50	 # number of substeps for results in fine unloading step
rough_substeps = 50	 # number of substeps for results in the rest of unloading step
#########################################################
test_file = os.path.exists('sims_check_3D.txt')
if test_file:
	os.remove('sims_check_3D.txt')

for i in range(1, numrows+1):
	Mdb()
	model_n = input_data[i-1, 0]		# ID
	tip_r = input_data[i-1, 1]			# tip radius in um
	t = input_data[i-1, 2]			# specimen thickness in um
	tip_E = input_data[i-1, 3] 		# tip Youngs modulus in MPa
	tip_nu = input_data[i-1, 4] 				# tip Poissons ratio
	specimen_E = input_data[i-1, 5] 	# specimen Youngs modulus in MPa
	specimen_nu = input_data[i-1, 6]		# specimen Poissons ratio
	specimen_Sy = input_data[i-1, 7]  # specimen yield stress in MPa
	n = input_data[i-1, 8]  # specimen n
	indent_depth = input_data[i-1, 9]  # indentation depth in um
	n_CPU = int(input_data[i-1, 10])		# number of CPU cores used for simulation
	save_odb = input_data[i-1, 11]

	#  MESHING PARAMETERS

	mesh_variable = 0.1

	num_round = 10  # number of elements "around" the model (60 degrees arc around the indentation place is divided into this number, like a pizza slices)
	fine_depth = 0.0425*indent_depth

	fine_min = 0.05*mesh_variable
	fine_max = 0.75*mesh_variable
	rest_depth_min = 10*mesh_variable  # minimal element size in the rest of the model in the thickness direction
	rest_depth_max = 70*mesh_variable  # maximal element size in the rest of the model in the thickness direction
	rest_mesh = 10*mesh_variable
	indenter_fine = 0.01*mesh_variable
	initial_increment_2 = 0.005		# element size - the indenter tip

	quad_ele = 0  # if ==1 then quadratic elements will be used under the tip, else only linear ones
	ALE_freq = 1  # frequency of ALE adaptive meshing, 1 means each time step will undergo remeshing, 2 means each other undergoes it etc.
	indent_width = indent_depth/(tan(np.deg2rad(12.95)))

	execfile(work_path + '/scripts_3D/geom_specimen.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/geom_tip.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/materials.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/contact_prop.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/load.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/msh.py', __main__.__dict__)
	execfile(work_path + '/scripts_3D/run.py', __main__.__dict__)
	try:
		execfile(work_path + '/scripts_3D/results.py', __main__.__dict__)
		execfile(work_path + '/scripts_3D/sim_check.py', __main__.__dict__)
	except:
		print('Simulation was not finished')
