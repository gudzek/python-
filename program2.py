"""
Program do rysowania wykresow interpolowanych wielomianów
przy podanych przez użytkownika węzłach
Copyright (C) 2018 by Damian Guzek and Emilia Koniszewska.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details,
available at <https://www.gnu.org/licenses/>.

Started on October 26, 2018. Last revision: October 29, 2018.
"""





title = "\
Program2 v. 1.00, 10/29/2018. Copyright (C) by Damian Guzek and Emilia Koniszewska.\n\
This is free software. No warranty. See GNU GPL for details.\n";
#

helpinfo = "\
Ten program rysuje wielomiany, wyliczone na podstawie interpolacji metodą Newtona\n\
Do znalezienia odpowiadającego wielomianu program wykorzystuje węzły podane przez użytkownika\n\
Program uruchomiamy podając dane w następujący sposób:\n\
x_0 f(x_0) x_1 f(x_1) x_2 f(x_2)...\n\
";





#=============================================================
##############Oznaczenia - part_0
# X - [x_0, x_1, x_2, ...] - argumenty
# Y - [f(x_0), f(x_1), f(x_2), ...] - wartości
# Z - [[x_0, x_1, x_2], [f(x_0), f(x_1), f(x_2)], [f[x_0 x_1],f[x_1 x_2]]]
    #Z jest listą w której przetrzymujemy wszystkie wyliczone lub wprowadzone wartości

# P - [f(x_0), f[x_0 x_1], f[x_0 x_1 x_2]] - zawiera wszystkie wartości niezbędne do obliczenia wielomianu
# Lista - np. [[-2, 1], [0, 1], [-3, 2]] - lista dwumianów wykorzystywanych przy wyliczaniu wielomianu
    #Precyzując [-2, 1] oznacza dwumian (x-2)
    #           [ 0, 1] oznacza dwumian (x-0)

# Lista2 - np. [a_0 , [b_0 , b_1], [c_0, c_1, c_2], [d_0, d_1, d_2, d_3]]
    #Lista sum częściowych, które po zsumowaniu dają nam wielomian, który chcemy narysować

# Wynik - współczynniki wielomianu wynikowego podane według szablonu [a_0, a_1, a_2, ...]
    #       F(x) = a_0 + a_1*x + a_2*x^2 + a_3*x^3 + ...




#Import niezbędnych modułów
import sys
import matplotlib.pyplot as plt





#=============================================================
##############Funkcje - part_1
#Fukcja mnożąca dwumiany
def multi(a,b):
    prod = []

    for i in range(0,len(a)+len(b)-1):
        prod.append(0)

    for i in range(0,len(a)):
        for j in range(0,len(b)):
            prod[i+j] += a[i] * b[j]

    print(prod)
    return(prod)





#=============================================================
##############Sprawdzamy, czy można uruchomić pozostałą część kodu - part_2
#sprawdzamy poprawność wprowadzonych danych
if len(sys.argv)%2 == 0:
    print("Podano złą liczbę argumentów. Spróbuj jeszcze raz.")
    quit()





#=============================================================
##############Segregujemy wprowadzone dane - part_3
#Dzielimy wprowadzone węzły na dwie listy
#X - argumenty
#Y - wartości
X = []
Y = []
for i in range(1,int((len(sys.argv)+1)/2)):
    X.append(int(sys.argv[2*i-1]))
    Y.append(int(sys.argv[2*i]))





#=============================================================
###############Informacja zwrotna dla użytkownika - part_4
#Informujemy użytkownika o podanych argumentach i wartościach
print("\nJako argumenty węzłów podano: ", X)
print("\nJako wartości węzłów podano: ", Y, "\n")





#=============================================================
##############Wyliczanie f[x_0,x_1,x_2,...] - part_5
#Korzystamy z algorytmu Newtona
#Lista Z jest nam potrzebna do zachowywania obliczanych wyrażeń
Z = []
Z.append(X)
Z.append(Y)

#Obliczamy Divided differences i umieszczamy je w listach
for j in range(0,len(X)-1):
    Y_new = []

    for i in range(1, len(X)-j):
        Y_new.append((Z[j+1][i]-Z[j+1][i-1])/(Z[0][i+j] - Z[0][i-1]))
    Z.append(Y_new)

#Wyciągamy z listy tylko elemetny niezbędne do utworzenia wielomianu
P = []
for i in range(1,len(X)+1):
    P.append(Z[i][0])





#=============================================================
##############Tworzenie dwumianów - part_6
#towrzymy dwumiany - (x - x_i) - wzór newtona
#będą potrzebne do późniejszego wymnożenia
X_new = []
for i in range(0,len(X)):
    X_new.append(i)

for i in range(0,len(X)):
    X_new[i] = (-1)*X[i]

New_stuff = []
for i in range(0,len(X)):
    New_stuff.append(1)

Lista = []
for i in range(0,len(X)):
    Lista.append(i)

for i in range(0,len(X)):
    Lista[i] = [X_new[i], New_stuff[i]]





#=============================================================
##############Wymnażamy wcześniej utworzone dwumiany - part_7
Lista2 = []
Lista2.append(P[0])
Lista2.append(Lista[0])

Polyn = multi(Lista[0],Lista[1])
Lista2.append(Polyn)

for i in range(2, len(X)-1):
    Polyn = multi(Polyn,Lista[i])
    Lista2.append(Polyn)

##############Wymnażamy wcześniej utworzone dwumiany przez wartość z P - part_7.5
for j in range(1, len(Lista2)):
    for i in range(1, len(Lista2[j])+1):
        Lista2[j][i-1] = Lista2[j][i-1] * P[j]





#=============================================================
##############Dodawanie odpowiednich wyrazów - part_8
Wynik = []
for i in range(0,len(Lista2)):
    Wynik.append(0)

Wynik[0] = Lista2[0]

for j in range(1,len(Lista2)):
    for i in range(0,len(Lista2[j])):
        Wynik[i] += Lista2[j][i]

print("\n\n\nNasz wielomian to [a_0,a_1,a_2, ...]:  ",Wynik)





#=============================================================
##############Wyliczanie wartości funkcji - part_9
X_wyk = []
Y_wyk = []

p = -100
while p<=100:
    X_wyk.append(p)

    U = 0
    for i in range(0,len(Wynik)):
        U += Wynik[i]*p**i
    Y_wyk.append(U)
    p = p + 1

#Rysuję wykres i podane węzły
plt.plot(X_wyk,Y_wyk)
plt.plot(X, Y, 'o', color='black')
plt.show()
