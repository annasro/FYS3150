import  numpy as np


x = np.sqrt(2)

def f(x):
    return np.arctan(x)

def df(x):
    return 1/(1+x**2)

def feil(h,x):
    return np.abs(df(x) - (f(x+h) - f(x))/h)

h = np.logspace(-12,-1, 10000)

values = feil(h,x)
min_value_index = np.argmin(values)
s = values[min_value_index]

print(min_value_index)
print(s)
h1 = h[s]


def f2(x,h1):
    return (f(x+h1) -f(x)) / h1

def f3(x,h1):
    return (f(x+h1) - f(x-h1)) / (2*h1)

print(f2(x,s))
print(f3(x,s))
print(1/3.0)
