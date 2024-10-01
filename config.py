# voltage clamp settings 
VM_0 = -70
VM_1 = -10


# current clamp settings
I_0 = 0
I_1 = 10

CAP = 1

T_CHANGE = 50 # time until V_cmd is changed
T_REVERT = 250 # if pulse, time to revert to original
T_TOTAL = 300
T_DEF = 20 # updates/s

N_0 = 0.00
M_0 = 0.00
H_0 = 0.00



V_R = -60

#Original HH paper was unclear about resting potential E; everything written in difference from resting potential
V_K = 12
V_NA = -115
V_L = -10.387

EQ_K = - V_K + V_R
EQ_NA = - V_NA + V_R
EQ_L = - V_L + V_R

G_K = 36
G_NA = 120
G_L = 0.3