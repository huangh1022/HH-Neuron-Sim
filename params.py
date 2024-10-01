import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

V_0 = float(cfg['Voltage']['V_0'])
V_1 = float(cfg['Voltage']['V_1'])

I_0 = float(cfg['Current']['I_0'])
I_1 = float(cfg['Current']['I_1'])

CAP = float(cfg['Circuit Params']['CAP'])
V_R = float(cfg['Circuit Params']['V_R'])

T_TOTAL = int(cfg['Time Params']['T_TOTAL'])
T_DEF = int(cfg['Time Params']['T_DEF'])
T_CHANGE = int(cfg['Time Params']['T_CHANGE'])
T_REVERT = int(cfg['Time Params']['T_REVERT'])

N_0 = float(cfg['Conductances']['N_0'])
M_0 = float(cfg['Conductances']['M_0'])
H_0 = float(cfg['Conductances']['H_0'])

V_K = float(cfg['HH Params']['V_K'])
V_NA = float(cfg['HH Params']['V_NA'])
V_L = float(cfg['HH Params']['V_L'])

G_K = float(cfg['HH Params']['G_K'])
G_NA = float(cfg['HH Params']['G_NA'])
G_L = float(cfg['HH Params']['G_L'])

EQ_K = - V_K + V_R
EQ_NA = - V_NA + V_R
EQ_L = - V_L + V_R
