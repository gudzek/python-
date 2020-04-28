import math

"""
Program do rozwiązywania układów nieliniowych
Copyright (C) 2018 by Damian Guzek, Emilia Koniszewska and Dawid Drzymalski.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful and wonderful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details,
available at <https://www.gnu.org/licenses/>.

Started on December 27, 2018. Last revision: December 28, 2018.

Podczas pisana programu korzystalismy z zasobów poniższej strony
https://www.math.ubc.ca/~pwalls/
"""





title = "\
Program3 v. 1.00, 28/12/2018. Copyright (C) by Damian Guzek, Emilia Koniszewska and Dawid Drzymalski.\n\
This is free software. No warranty. See GNU GPL for details.\n";
#

#######################################################################
### Definicje funkcji - part 0
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Metoda bisekcji
def bisection(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Metoda siecznych
def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Metoda netwona
def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(1,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
        print(xn)
    print('Exceeded maximum iterations. No solution found.')
    return None

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
### Wzory funckcji - part 0.5
f = lambda x: x**3 - x**2 - 1
Df = lambda x: 3*x**2 - 2*x

w = lambda x: x**2 - x - 1
Dw = lambda x: 2*x -1

g = lambda x: math.sin(x - 1.4)
Dg = lambda x: math.cos(x - 1.4)




#######################################################################
### Wykonywanie kilkudziesięciu iteracji - part 1
print("funkcja f")
print("Metoda bisekcji")
for i in range(1,50):
    approx_fb = bisection(f,1,2,i)
    print(approx_fb)

print("\n\n")
print("funkcja f")
print("Metoda siecznych")
for i in range(1,50):
    approx_fs = secant(f,1,2,i)
    print(approx_fs)

print("\n\n")
print("funkcja f")
print("Metoda Netwona")
approx_fn = newton(f,Df,1,1e-17,50)
print(approx_fn)

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("funkcja w")
print("Metoda bisekcji")
for i in range(1,50):
    approx_wb = bisection(w,1,2,i)
    print(approx_wb)

print("\n\n")
print("funkcja w")
print("Metoda siecznych")
for i in range(1,50):
    approx_ws = secant(w,1,2,i)
    print(approx_ws)

print("\n\n")
print("funkcja w")
print("Metoda Netwona")
approx_wn = newton(w,Dw,1,1e-17,50)
print(approx_wn)

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("funkcja g")
print("Metoda bisekcji")
for i in range(1,50):
    approx_gb = bisection(g,1,2,i)
    print(approx_gb)

print("\n\n")
print("funkcja g")
print("Metoda siecznych")
for i in range(1,50):
    approx_gs = secant(g,1,2,i)
    print(approx_gs)

print("\n\n")
print("funkcja g")
print("Metoda Netwona")
approx_gn = newton(g,Dg,1,1e-17,50)
print(approx_gn)
