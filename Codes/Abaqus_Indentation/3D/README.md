# IMPORTANT

Model uses following unit system:
<ul>
	<li>force: micro-Newtons (µN)</li>
	<li>displacement or dimension: micro-meters (µm)</li>
	<li>stress: megapascals (MPa)</li>
</ul>

These applies for both input and output data

**RUNNING THE SIMULATIONS**


(1) Change input parameters in the "input_data_2D.csv" file (each row in the file specifies one simulation)

	ID - identification number of the simulation, must be unique for each simulation
	tip_R - tip radius
	specimen_thickness - thickness of the indented specimen
	tip_E - Young's modulus of the tip material model (purely elastic)
	tip_nu - Poisson's ration of the tip material model (purely elastic)
	specimen_E - Young's modulus of the specimen material model (Ramberg-Osgood material model)
	specimen_nu - Poisson's ration of the specimen material model (Ramberg-Osgood material model)
	yield_stress -yielding stress of the specimen used in Ramberg-Osgood material model
	specmen_n - the slope of the specimen plastic part of the stress-strain curve
	indentation_depth - depth of the indentation procedure
	number_of_used_CPUs - specifies how many cores of Your CPU will be used
	Save_ODB - specifies whether the ODB results database will be saved, if 1, ODB will be saved, if 0, only Force-displacement curves data will be saved

*** RESULTING FILES ***

After each simulation is done, two files with respective ID will be saved:

a) ODB results database (can be set to delete via parameter "save ODB") named "Sim_ID_..." with all resulting data

b) Resulting force-displacement indentation curve in file "F-u_ID...txt". This file has structured columns - 1st is for "simulation time", 2nd one is the resulting force in each step related to the tip displacement in the 3rd column.

Whole simulation run is then summarized in file "sims_check.txt" where for each simulation ID (1st column) the end-time is shown (2nd column), if it equals 2, simulation ended correctly, if it is less than 2 or ID is missing, simulation crashed during the evaluation.
Keep in mind that "sims_check.txt" file is ALWAYS deleted, when a new set of simulation is started in the same folder!
