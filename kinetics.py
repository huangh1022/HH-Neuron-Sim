from numpy import *;

from params import *

# kinetic equations based off of original HH paper
# V in calculating a and b is assumed to be written as negative driving force u, i.e. displacement of voltage 
# V=(-P+70)

def get_diff(var, sub, v):
    inf = get_inf(sub, v)
    tau = get_tau(sub, v)

    return (inf - var) / tau
    
def diff_inc(var, sub, v):
    dt = (1/T_DEF)
    return var + (dt * (get_diff(var, sub, v)))

def get_tau(sub, v):
    a = get_a(sub, v)
    b = get_b(sub, v)
    return (1)/(b+a)
    
def get_inf(sub, v):
    a = get_a(sub, v)
    b = get_b(sub, v)
    return (a)/(b+a)

def get_a(sub, v):
    u = v-V_R;
    match sub:
        case "n":
            a = 0.01*(10-u)/(exp(1-0.1*u)-1)
        case "m": 
            a = 0.1*(25-u)/(exp(2.5-0.1*u)-1)
        case "h":
            a = .07*exp(-u/20)
        case _:        
            a = None
    return a

def get_b(sub, v):
    u = v-V_R;
    match sub:
        case "n":
            b = .125*exp(-u/80)
        case "m":
            b = 4*exp(-u/18)
        case "h":
            b = 1/(exp(3-0.1*u)+1)
        case _:        
            b = None
    return b

def main():
    print(get_tau("n",-70))

if __name__ == "__main__":
    main()