from numpy import *;

from params import *

# kinetic equations based off of original HH paper
# V in calculating a and b is assumed to be written as negative driving force u, i.e. displacement of voltage 
# V=(-P+70)

user_a_n = "0.01*(10-u)/(exp(1-0.1*u)-1)"
user_a_m = "0.1*(25-u)/(exp(2.5-0.1*u)-1)"
user_a_h = ".07*exp(-u/20)"

user_b_n = ".125*exp(-u/80)"
user_b_m = "4*exp(-u/18)"
user_b_h = "1/(exp(3-0.1*u)+1)"

def get_diff(var, sub, v):
    inf = alt_inf(sub, v)
    tau = alt_tau(sub, v)

    return (inf - var) / tau
    
def diff_inc(var, sub, v):
    dt = (1/T_DEF)
    return var + (dt * (get_diff(var, sub, v)))

def alt_tau(sub, v):
    a = alt_a(sub, v)
    b = alt_b(sub, v)
    return (1)/(b+a)
    
def alt_inf(sub, v):
    a = alt_a(sub, v)
    b = alt_b(sub, v)
    return (a)/(b+a)

def set_a(const, user_expression): # set custom definition of a and b
    match const:
        case "n":
            user_a_n = user_expression
        case "m":
            user_a_n = user_expression
        case "h":
            user_a_n = user_expression
            
def set_b(const, user_expression):
    match const:
        case "n":
            user_a_n = user_expression
        case "m":
            user_a_m = user_expression
        case "h":
            user_a_h = user_expression

def default():
    user_a_n = "0.01*(10-u)/(exp(1-0.1*u)-1)"
    user_a_m = "0.1*(25-u)/(exp(2.5-0.1*u)-1)"
    user_a_h = ".07*exp(-u/20)"

    user_b_n = ".125*exp(-u/80)"
    user_b_m = "4*exp(-u/18)"
    user_b_h = "1/(exp(3-0.1*u)+1)"

def alt_a(sub, v):
    u = v-V_R
    match sub:
        case "n":
            a = eval(user_a_n)
        case "m":
            a = eval(user_a_m)
        case "h":
            a = eval(user_a_h)
        case _:
            a = None
    return a

def alt_b(sub, v):
    u = v-V_R
    match sub:
        case "n":
            b = eval(user_a_n)
        case "m":
            b = eval(user_a_m)
        case "h":
            b = eval(user_a_h)
        case _:
            b = None
    return b
