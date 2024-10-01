import matplotlib.pylab as plt
import params
import kinetics
import importlib

importlib.reload(params)
importlib.reload(kinetics)

from kinetics import *
from params import *

def current_clamp():

    data_k = {}
    data_na = {}
    data_l = {}
    data_total = {}

    n = N_0
    m = M_0
    h = H_0

    v = V_0
    i = I_0

    for j in range(0, T_TOTAL*T_DEF, 1):

        time = j / T_DEF

        # driver for current clamp

        if time > T_CHANGE and time <= T_REVERT:
            i = I_1
        elif time > T_REVERT: i = I_0

        df_k = (v-EQ_K)
        df_na = (v-EQ_NA)
        df_l = (v-EQ_L)

        i_k = G_K*(n**4)*df_k
        i_na = G_NA*(h*m**3)*df_na
        i_l = G_L * df_l

        dv = (i - i_k - i_na - i_l) / CAP

        n = diff_inc(n, "n", v)
        m = diff_inc(m, "m", v)
        h = diff_inc(h, "h", v)

        v = v + (dv / T_DEF)

        data_total[time] = v

        data_k[time] = i_k
        data_na[time] = i_na
        data_l[time] = i_l
        
        #data_total[time] = G_NA*(h*m**3)*(v-EQ_NA) + G_K*(n**4)*(v-EQ_K) + G_L * (v-EQ_L)

    list_k = sorted(data_k.items()) # sorted by key, return a list of tuples
    list_na = sorted(data_na.items())
    list_l = sorted(data_l.items())
    list_total = sorted(data_total.items())
    

    t, k_val = zip(*list_k) # unpack a list of pairs into two tuples
    t, na_val = zip(*list_na)
    t, l_val = zip(*list_l)
    t, total_val = zip(*list_total)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1)

    ax1.plot(t, k_val)
    ax1.set_title("Potassium Current")
    
    ax2.plot(t, na_val)
    ax2.set_title("Sodium Current")

    ax3.plot(t, l_val)
    ax3.set_title("Leak Current")

    ax4.plot(t, total_val)
    ax4.set_title("Membrane Potential")

    #plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    current_clamp()

if __name__ == "__main__":
    main()