import numpy as np
import pprint
import matplotlib.pylab as plt

from config import *
from kinetics import *

def main():
    
    data_n = {}
    data_m = {}
    data_h = {}
    data_na = {}
    data_total = {}
    n = N_0
    m = M_0
    h = H_0
    v = VM_0

    for j in range(0, T_TOTAL*T_DEF, 1):
        
        time = j / T_DEF

        # driver for voltage clamp
        if time > T_CHANGE and time <= T_REVERT:
            v = VM_1
        elif time > T_REVERT: v = VM_0
    
        n = diff_inc(n, "n", v)
        m = diff_inc(m, "m", v)
        h = diff_inc(h, "h", v)

        data_n[time] = n**4
        data_m[time] = m**3
        data_h[time] = h        
        
        data_na[time] = h*m**3

        df_k = (v-EQ_K)
        df_na = (v-EQ_NA)
        df_l = (v-EQ_L)

        i_k = G_K*(n**4)*df_k
        i_na = G_NA*(h*m**3)*df_na
        i_l = G_L * df_l
        
        i = i_k + i_na + i_l

        data_total[time] = i
        #data_total[time] = G_NA*(h*m**3)*(v-EQ_NA) + G_K*(n**4)*(v-EQ_K) + G_L * (v-EQ_L) 
        

    list_n = sorted(data_n.items()) # sorted by key, return a list of tuples
    list_m = sorted(data_m.items())
    list_h = sorted(data_h.items())
    list_na = sorted(data_na.items())
    list_total = sorted(data_total.items())
    

    t, n_val = zip(*list_n) # unpack a list of pairs into two tuples
    t, m_val = zip(*list_m)
    t, h_val = zip(*list_h)
    t, na_val = zip(*list_na)
    t, total_val = zip(*list_total)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1)

    ax1.plot(t, n_val)
    ax1.set_title("n")
    
    ax2.plot(t, m_val, color = "r", label="m")
    ax2.plot(t, h_val, color = "g", label="h")
    ax2.set_title("m & h")

    ax3.plot(t, na_val)
    ax3.set_title("total sodium rate")

    ax4.plot(t, total_val)
    ax4.set_title("total")

    #plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()