# Keys for connection type
DOPA_ex = 0
DOPA_in = 1
NORA_ex = 2
SERO_in = 3
SERO_ex = 4

# Keys for synapse models
model = 0
basic_weight = 1

# Quality of graphics
dpi_n = 120

# Keys for parts dictionary
k_IDs   = 'IDs'
k_name  = 'Name'
k_NN    = 'NN'
k_model = 'Model'

# T - simulation time | dt - simulation pause step
T = 1000.
dt = 10.

# Neurons number for spike detector
N_detect = 100

# Neurons number for multimeter
N_volt = 3

# Generator delay
pg_delay = 10.

# Synapse weights
w_DA_ex = 13.
w_DA_in = -w_DA_ex
w_NA_ex = 13.
w_SERO_ex = 10.
w_SERO_in = -w_SERO_ex

# Minimal number of neurons
NN_minimal = 10

# Synapse models
dopa_synapse_ex  = 'dopa_synapse_ex'
dopa_synapse_in  = 'dopa_synapse_in'
nora_synapse_ex  = 'nora_synapse_ex'
sero_synapse_ex  = 'sero_synapse_ex'
sero_synapse_in  = 'sero_synapse_in'
gen_static_syn   = 'noise_conn'

# Additional setings
dopamine_flag = True     # dopamine modulation flag
generator_flag = True
status_gui = True        # True - GUI is on | False - is off
flag_5HT =True