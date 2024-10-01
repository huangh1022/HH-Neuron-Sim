import tkinter as tk
import configparser as cp
import current_clamp
import voltage_clamp
import importlib

importlib.reload(current_clamp)
importlib.reload(voltage_clamp)

from voltage_clamp import *
from current_clamp import *

cfg = cp.ConfigParser()
cfg.read('config.ini')

i_main = tk.Tk()

def select_warning():
    top = tk.Toplevel(i_main)
    top.title('Error!')
    tk.Label(top, text = 'Choose a test type!').pack()

    tk.Button(top, text= "ok", command= top.destroy).pack(pady = 10)

def open_time_config():
    top = tk.Toplevel(i_main)
    top.title("Time Parameters")

    tk.Label(top, text="Total Time").grid(row=0)
    tk.Label(top, text="Updates Per Second").grid(row=1)
    tk.Label(top, text="Change").grid(row=2)
    tk.Label(top, text="Revert").grid(row=3)

    e1 = tk.Entry(top)
    e2 = tk.Entry(top)
    e3 = tk.Entry(top)
    e4 = tk.Entry(top)

    e1.insert(0, cfg['Time Params']['T_TOTAL'])
    e2.insert(0, cfg['Time Params']['T_DEF'])
    e3.insert(0, cfg['Time Params']['T_CHANGE'])
    e4.insert(0, cfg['Time Params']['T_REVERT'])

    e1.grid(row= 0, column= 1)
    e2.grid(row= 1, column= 1)
    e3.grid(row= 2, column= 1)
    e4.grid(row= 3, column= 1)

    def set_config():

        cfg.set('Time Params', 'T_TOTAL', e1.get())
        cfg.set('Time Params', 'T_DEF', e2.get())
        cfg.set('Time Params', 'T_CHANGE', e3.get())
        cfg.set('Time Params', 'T_REVERT', e4.get())

        with open('config.ini','w') as configfile:
            cfg.write(configfile)
        
        top.destroy()
        top.update()

    def toggle_rev():
        if e4['state'] == 'normal':
            e4.delete(0, tk.END)
            e4.insert(0, string=e1.get())
            e4['state'] = 'disabled'
        else:
            e4['state'] = 'normal'

    cb1 = tk.Checkbutton(top, text="Revert?", command = toggle_rev)

    cb1.grid(row=5)

    b2 = tk.Button(top, text= "Confirm", command = set_config)
    b2.grid(row=5, column=1)

def open_params(test_type):
    top = tk.Toplevel(i_main)
    top.title("Test Parameters")

    e1 = tk.Entry(top)
    e2 = tk.Entry(top)
    e3 = tk.Entry(top)
    e4 = tk.Entry(top)

    match test_type:
        case 'vc':
            tk.Label(top, text="Baseline Voltage").grid(row=0)
            tk.Label(top, text="Altered Voltage").grid(row=1)

            e1.insert(0, cfg['Voltage']['V_0'])
            e2.insert(0, cfg['Voltage']['V_1'])
        case 'cc':
            tk.Label(top, text="Baseline Current").grid(row=0)
            tk.Label(top, text="Altered Current").grid(row=1)
    
            e1.insert(0, cfg['Current']['I_0'])
            e2.insert(0, cfg['Current']['I_1'])
        case default:
            select_warning()
            

    tk.Label(top, text="Capacitance").grid(row=2)
    tk.Label(top, text="Resting Potential").grid(row=3)

    e3.insert(0, cfg['Circuit Params']['CAP'])
    e4.insert(0, cfg['Circuit Params']['V_R'])

    e1.grid(row= 0, column= 1)
    e2.grid(row= 1, column= 1)
    e3.grid(row= 2, column= 1)
    e4.grid(row= 3, column= 1)

    def set_config():

        match test_type:
            case 'vc':
                cfg.set('Voltage', 'V_0', e1.get())
                cfg.set('Voltage', 'V_1', e2.get())
            case 'cc':
                cfg.set('Current', 'I_0', e1.get())
                cfg.set('Current', 'I_1', e2.get())
            case default:
                select_warning()

        cfg.set('Circuit Params', 'CAP', e3.get())
        cfg.set('Circuit Params', 'V_R', e4.get())

        with open('config.ini','w') as configfile:
            cfg.write(configfile)
        
        top.destroy()
        top.update()

    b1 = tk.Button(top, text= "Confirm", command = set_config)
    b1.grid(row=5, column=1)

def open_hh():
    top = tk.Toplevel(i_main)
    top.title("Test Parameters")

    e1 = tk.Entry(top)
    e2 = tk.Entry(top)
    e3 = tk.Entry(top)
    e4 = tk.Entry(top)
    e5 = tk.Entry(top)
    e6 = tk.Entry(top)

    e1.insert(0, cfg['HH Params']['V_K'])
    e2.insert(0, cfg['HH Params']['V_NA'])
    e3.insert(0, cfg['HH Params']['V_L'])
    e4.insert(0, cfg['HH Params']['G_K'])
    e5.insert(0, cfg['HH Params']['G_NA'])
    e6.insert(0, cfg['HH Params']['G_L'])

    e1.grid(row= 0, column= 1)
    e2.grid(row= 1, column= 1)
    e3.grid(row= 2, column= 1)
    e4.grid(row= 3, column= 1)
    e5.grid(row= 4, column= 1)
    e6.grid(row= 5, column= 1)

    tk.Label(top, text="V_K").grid(row=0)
    tk.Label(top, text="V_Na").grid(row=1)
    tk.Label(top, text="V_L").grid(row=2)
    tk.Label(top, text="G_K").grid(row=3)
    tk.Label(top, text="G_Na").grid(row=4)
    tk.Label(top, text="G_L").grid(row=5)

    def reset_params():

        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e5.delete(0, tk.END)
        e6.delete(0, tk.END)
        
        e1.insert(0, '12')
        e2.insert(0, '-115')
        e3.insert(0, '-10.387')
        e4.insert(0, '36')
        e5.insert(0, '120')
        e6.insert(0, '0.3')

    def set_config():

        cfg.set('HH Params', 'V_K', e1.get())
        cfg.set('HH Params', 'V_NA', e2.get())
        cfg.set('HH Params', 'V_L', e3.get())
        cfg.set('HH Params', 'G_K', e4.get())
        cfg.set('HH Params', 'G_NA', e5.get())
        cfg.set('HH Params', 'G_L', e6.get())

        with open('config.ini','w') as configfile:
            cfg.write(configfile)
        
        top.destroy()
        top.update()

    b1 = tk.Button(top, text= "HH Default", command = reset_params)
    b1.grid(row=7)

    b2 = tk.Button(top, text= "Confirm", command = set_config)
    b2.grid(row=7, column=1)

def run_sim(test_type):
    
    if test_type == "vc":
        voltage_clamp()
    elif test_type == "cc":
        current_clamp()
    else:
        select_warning()
        
def inter_main():

    test_type = "vc"

    i_main.geometry("320x440")

    i_main.title("Single Neuron Simulation")

    tk.Label(i_main, text = "Select the simulation to perform:").pack(pady=20)

    test_type = tk.StringVar()
    
    tk.Radiobutton(i_main, text="Voltage Clamp", variable= test_type, value = 'vc', indicator = 0).pack(anchor='center')
    tk.Radiobutton(i_main, text="Current Clamp", variable= test_type, value = 'cc', indicator = 0).pack(anchor='center')

    tk.Label(i_main, text = "Change Parameters:").pack(pady=20)

    b_time = tk.Button(i_main, text = 'Change Time Parameters', width=25, command = open_time_config)
    b_param = tk.Button(i_main, text = 'Change Test Parameters', width=25, command = lambda: open_params(test_type.get()))
    b_hh = tk.Button(i_main, text = 'Change Kinetics Parameters', width=25, command = open_hh)

    b_time.pack()
    b_param.pack()
    b_hh.pack()

    tk.Label(i_main, text = "Edits to parameters require restart to take effect.").pack(pady=20)

    tk.Button(i_main, text = 'Run Simulation', width=25, command = lambda: run_sim(test_type.get())).pack(pady=20)

    i_main.mainloop()

def main():
    inter_main()

if __name__ == "__main__":
    main()