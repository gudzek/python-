"""
Program obliczający numeryczne przybliżenie całki oznaczonej
wybranej funkcji na zadanym przedziale metoda prostokatow
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

Started on November 24, 2018. Last revision: November 25, 2018.
"""



title = "\
Program2_calki v. 1.00, 11/25/2018. Copyright (C) by Damian Guzek and Emilia Koniszewska.\n\
This is free software. No warranty. See GNU GPL for details.\n";


helpinfo = """\
Ten program obliczający numeryczne przybliżenie całki oznaczonej
wybranej funkcji na zadanym przedziale metoda prostokatow\n\
Program wykorzystuje dane podane przez użytkownika i oblicza calke dana wzorem x**2\n\
Program uruchamiamy podając dane w następujący sposób:\n\
poczatek_przedzialu
koniec_przedzialu
""";





#############=============================================================
#####import niezbędnych modułów - part_0
import math as m
import numpy as n





#############=============================================================
#####Oznaczenia - part_0

# linspace - funkcja zwracająca równo rozmieszczone liczby w określonym przedziale.
# Blad1 - lista zawierająca błędy bezwględne
# Blad2 - lista zawierająca błędy względne




#############=============================================================
##### program pyta uzytkownika o poczatek i koniec
##### przedzialu oraz sprawdza czy podane dane były prawidłowe - part_1
poczatek_przedzialu = int(input("Podaj poczatek przedzialu  "))
koniec_przedzialu = float(input("Podaj koniec przedzialu  "))

if (poczatek_przedzialu>koniec_przedzialu):
   print ("Wprowadzone dane sa nieprawidlowe, sprobuj jeszcze raz")
   quit ()





#############=============================================================
#####liczy numerycznie calki dla dla narastajacej
#####liczby przedziałów oraz za pomocą podstawowego twierdzenia całkowego - part_2
Blad1 = []
Blad2 = []
liczba_krokow = 1

for i in range(1, 4): #lub i in range (1,1000)


    #liczymy długość przedziałów - dx oraz wyliczamy ich środki
    print(liczba_krokow," to liczba kroków")
    punkty_w_przedziale = n.linspace(poczatek_przedzialu, koniec_przedzialu, liczba_krokow + 1)
    dx = (koniec_przedzialu-poczatek_przedzialu) / liczba_krokow


    #numerczynie wyliczamy naszą całkę
    suma_punktow = 0
    for i in range(0,len(punkty_w_przedziale)):
        suma_punktow += punkty_w_przedziale[i]**2
    suma_pol_prostokatow = dx * suma_punktow


    #obliczamy wynik całki z podstawowego twierdzenia całkowego
    #oraz błędy związana z obliczaniem całki w sposób numeryczny
    wynik_calki_numerycznej = suma_pol_prostokatow
    prawidlowy_wynik_calki = (1/3)*(koniec_przedzialu)**3 - (1/3)*(poczatek_przedzialu)**3
    blad_bezwgledny = abs(prawidlowy_wynik_calki - wynik_calki_numerycznej)
    blad_wzgledny = blad_bezwgledny*100/prawidlowy_wynik_calki

    #wyświetlamy wyniki dla każdej iteracji
    print("Wynik naszej calki to ",wynik_calki_numerycznej)
    print("Wynik dokładny to: ", prawidlowy_wynik_calki)
    print("Błąd bezwględny to: ", blad_bezwgledny)
    print("Błąd względny to: ", blad_wzgledny )
    print("\n\n")

    #towrzymy lsity składające się z błędów
    Blad1.append(blad_bezwgledny)
    Blad2.append(blad_wzgledny)
    liczba_krokow += 1






##### Linie kontrolne dla osoby piszącej program
#print("Blad1 to:", Blad1)
#print("Blad2 to:", Blad2)
