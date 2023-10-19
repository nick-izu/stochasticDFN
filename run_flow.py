from pydfnworks import *

DFN = create_dfn()

##dfnGen
DFN.make_working_directory()
DFN.check_input()
DFN.create_network()
DFN.mesh_network(visual_mode=False)

# First we define values for the stochastic families

variable = "transmissivity"
function = "correlated"
params = {"alpha":2.2*10**-9, "beta":0.8}
b1,perm1,T1 = DFN.generate_hydraulic_values(variable,function,params,family_id=1)

T = T1 
b = b1
perm = perm1  

DFN.dump_hydraulic_values(b,perm,T)

# Add transmissivity values to the mesh for visualization
DFN.add_variable_to_mesh("trans,", "transmissivity.dat", "full_mesh.inp")

## JDH I added an exit here for you to look at the files before you run the simulation.
#exit()

#dfnFlow
#DFN.dfn_flow()


#dfntrans
#DFN.dfn_trans()

