import tkinter as tk
import configparser as cp

from voltage_clamp import *
from current_clamp import *

cfg = cp.ConfigParser()
cfg.read('config.ini')

i_main = tk.Tk()

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

    match test_type:
        case 'vc':
            tk.Label(top, text="Starting Voltage").grid(row=0)
            tk.Label(top, text="Altered Voltage").grid(row=1)
            tk.Label(top, text="Change").grid(row=2)
            tk.Label(top, text="Revert").grid(row=3)
        case 'cc':
            tk.Label(top, text="Total Time").grid(row=0)
            tk.Label(top, text="Updates Per Second").grid(row=1)
            tk.Label(top, text="Change").grid(row=2)
            tk.Label(top, text="Revert").grid(row=3)
        case default:
            top = tk.Toplevel(i_main)
            top.title('Error!')
            tk.Label(top, text = 'Choose a test type!').pack

    

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

def run_sim(test_type):
    if test_type == "vc":
        voltage_clamp()
    elif test_type == "cc":
        current_clamp()
    else:
        top = tk.Toplevel(i_main)
        top.title('Error!')
        tk.Label(top, text = 'Choose a test type!').pack
        

def inter_main():

    test_type = "vc"

    i_main.geometry("270x720")

    i_main.title("Single Neuron Simulation")

    tk.Label(i_main, text = "Single Neuron Simulation").pack()

    test_type = tk.StringVar()
    
    tk.Radiobutton(i_main, text="Voltage Clamp", variable= test_type, value = 'vc', indicator = 0).pack(anchor='center')
    tk.Radiobutton(i_main, text="Current Clamp", variable= test_type, value = 'cc', indicator = 0).pack(anchor='center')

    b_time = tk.Button(i_main, text = 'Change Time Parameters', width=25, command = open_time_config)
    b_param = tk.Button(i_main, text = 'Change Test Parameters', width=25, command = lambda: open_params(test_type.get()))
    b_hh = tk.Button(i_main, text = 'Change Kinetics Parameters', width=25, command = open_time_config)

    b_time.pack(pady=20)
    b_param.pack()
    b_hh.pack()

    tk.Button(i_main, text = 'Run Simulation', width=25, command = lambda: run_sim(test_type.get())).pack(pady=20)

    i_main.mainloop()

def main():
    inter_main()

if __name__ == "__main__":
    main()