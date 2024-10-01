import numpy as np

from config import *

# kinetic equations based off of original HH paper
# V in calculating a and b is assumed to be written as negative driving force, i.e. displacement of voltage 
# V=(-P+70)

def get_diff(var, sub, V):
    inf = get_inf(sub, V)
    tau = get_tau(sub, V)

    return (inf - var) / tau
    
def diff_inc(var, sub, V):
    dt = (1/T_DEF)
    return var + (dt * (get_diff(var, sub, V)))

def get_tau(sub, V):
    a = get_a(sub, V)
    b = get_b(sub, V)
    return (1)/(b+a)
    
def get_inf(sub, V):
    a = get_a(sub, V)
    b = get_b(sub, V)
    return (a)/(b+a)

def get_a(sub, V):
    u = V-V_R;
    match sub:
        case "n":
            a = 0.01*(10-u)/(np.exp(1-0.1*u)-1)
        case "m": 
            a = 0.1*(25-u)/(np.exp(2.5-0.1*u)-1)
        case "h":
            a = .07 * np.exp(-u/20)
        case _:        
            a = None
    return a

def get_b(sub, V):
    u = V-V_R;
    match sub:
        case "n":
            b = .125 * np.exp(-u/80)
        case "m":
            b = 4 * np.exp(-u/18)
        case "h":
            b = 1/(np.exp(3-0.1*u)+1)
        case _:        
            b = None
    return b

def main():
    print(get_tau("n",-70))

if __name__ == "__main__":
    main()