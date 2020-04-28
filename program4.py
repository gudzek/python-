"""
Program do rozwiązywania równań różniczkowych cząstkowych
Copyright (C) 2019 by Damian Guzek, Emilia Koniszewska and Dawid Drzymalski.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful and wonderful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details,
available at <https://www.gnu.org/licenses/>.

Started on January 20, 2019. Last revision: 2019.

Podczas pisana programu korzystalismy z zasobów:
* Książka D. Kincaid, W. Cheney: Analiza numeryczna, WNT, Warszawa 2006, ISBN 83-204-3078-X - Rozdział 9
"""





title = "\
Program3 v. 1.00, 20/01/2019. Copyright (C) by Damian Guzek, Emilia Koniszewska and Dawid Drzymalski.\n\
This is free software. No warranty. See GNU GPL for details.\n";
#

import matplotlib.pyplot as plt
import math
################################################################################################################
#Program oblicza metodą jawną przybliżenie funkcji będącej rozwiązaniem u_xx + u_tt=0, dla u(x,0)=g(x),
#u(0,t)=a(t) u(1,t)=b(t). Rozwiązanie opisane jest na [0,1]x[0,T], gdzie T = h*M
################################################################################################################

#Program został sprawdzony na kilku przykładach, aby sprawdzić wpływ zmiany wartości s na dokładność rozwiązania

#Aby sprawdzić konkretny przypadek, proszę odkomentować odpowiednia wartości k i M

#Dane do sprawdzenia z książki "Analiza numeryczna" - Zadanie 9.1
n = 9
k = 0.005125
M = 200

#k = 0.006
#M = 171

#Porównujemy, jak zmiana M wpływa na wynik
#k = 0.005
#M = 200
#M = 50

#Sprawdzamy wynik dla s = 0,549999
#k = 0.0055
#M = 200

#######################################################################
#Zmiana na n = 50
#n = 50

#k = 0.00015
#M = 200

#Pomimo s = 0.54621, wynik dokładny zwłaszcza dla x<0.5
#k = 0.00021
#M = 200

#Po raz kolejny po zwiększeniu M otrzymujemy wyniki odbiegające od wyniku rzeczywistego
#k = 0.00021
#M = 500

#Kiedy s < 0.5 i duże n, możemy przyjąć nawet M = 2000 (również sprawdzone na większych wartościach) i wynik pozostaje bardzo dokładny
#k = 0.0001
#M = 2000


#################################################################################################
#Określamy potrzebne tablice i
v = [0]*(n+2)
u = [0]*(n+2)
w = [0]*(n+2)
h = 1/(n+1)
s = k/(h**2)

#Warunek u(x,0)
for i in range(0, n+2):
    w[i] = float(math.sin(i*h*math.pi))

t = 0
#print(0,t,w)

#Algorytm do wyliczenia funkcji przybliżonej przy pomocy metody jawnej
for j in range(1, M+1):
    t = j*k
    v[0] = 0
    v[n+1] = 0
    for i in range(1, n+1):
        v[i] = float(s*w[i-1] + (1-2*s)*w[i] + s*w[i+1])
    #print(j,t,v)

    for i in range(0, n+2):
        w[i] = v[i]

#Pętla potrzebna do wyliczenia rozwiązania dokładnego
x = [0]*(n+2)
for i in range(0, n + 2):       #obliczenie wartości dokładnych znając rozwiązanie zagadnienia
    x[i] = i*h
    u[i] = float(math.exp(-(math.pi)*(math.pi)*M*k)*math.sin((math.pi)*x[i]))

#Pokazanie wyników - głównie potrzebne do analizy
print(w)
print(u)
print(s)

#Wizualna prezentacja otrzymanych wyników
plt.plot(x, u,'#32CD32', label="Wynik dokładny")        #rysowanie wykresu porównującego otrzymane wyniki
plt.plot(x, v,'#00ACEE', label="Metoda jawna")
plt.legend(loc='upper right')#Tworzenie legendy rysowanych wykresów
plt.grid(True)
plt.show()
