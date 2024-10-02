import matplotlib.pylab as plt
import params
import kinetics
import importlib

importlib.reload(params)
importlib.reload(kinetics)

from kinetics import *
from params import *

def curves():

    inf_n = {}
    inf_m = {}
    inf_h = {}
    
    tau_n = {}
    tau_m = {}
    tau_h = {}

    for i in range(V_LOWER*V_DEF, V_UPPER*V_DEF, 1):

        voltage = i / V_DEF
        
        inf_n[voltage] = get_inf('n', voltage)
        inf_m[voltage] = get_inf('m', voltage)
        inf_h[voltage] = get_inf('h', voltage)
        
        tau_n[voltage] = get_tau('n', voltage)
        tau_m[voltage] = get_tau('m', voltage)
        tau_h[voltage] = get_tau('h', voltage)

    ls_inf_n = sorted(inf_n.items()) # sorted by key, return a list of tuples
    ls_inf_m = sorted(inf_m.items())
    ls_inf_h = sorted(inf_h.items())

    ls_tau_n = sorted(tau_n.items())
    ls_tau_m = sorted(tau_m.items())
    ls_tau_h = sorted(tau_h.items())
    
    v1, inf_n_val = zip(*ls_inf_n) # unpack a list of pairs into two tuples
    v2, inf_m_val = zip(*ls_inf_m)
    v3, inf_h_val = zip(*ls_inf_h)

    v4, tau_n_val = zip(*ls_tau_n)
    v5, tau_m_val = zip(*ls_tau_m)
    v6, tau_h_val = zip(*ls_tau_h)

    plt.subplot(2, 3, 1)
    plt.plot(v1, inf_n_val)
    plt.title("n_inf Values")
    
    plt.subplot(2, 3, 2)
    plt.plot(v2, inf_m_val)
    plt.title("m_inf Values")

    plt.subplot(2, 3, 3)
    plt.plot(v3, inf_h_val)
    plt.title("h_inf Values")

    plt.subplot(2, 3, 4)
    plt.plot(v4, tau_n_val)
    plt.title("tau_n Values")

    plt.subplot(2, 3, 5)
    plt.plot(v5, tau_m_val)
    plt.title("tau_m Values")

    plt.subplot(2, 3, 6)
    plt.plot(v6, tau_h_val)
    plt.title("tau_h Values")

    #plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    curves()

if __name__ == "__main__":
    main()