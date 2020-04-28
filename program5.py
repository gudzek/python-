"""
Program do analizy tekstów literackich
Copyright (C) 2020 by Damian Guzek and Kamil Sandak.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details,
available at <https://www.gnu.org/licenses/>.

Started on March 30, 2020. Last revision: March 31, 2020.
"""


title = "\
Program v. 1.00, 03/31/2020. Copyright (C) by Damian Guzek and Kamil Sandak.\n\
This is free software. No warranty. See GNU GPL for details.\n";
#

helpinfo = "\
Ten program generuje raport umożliwający analizę tekstu\n\
Program uruchomiamy podając dane w następujący sposób:\n\
python3 program.py analizowanyc_tekst.txt\n\
";

#==========================================================================
#Importowanie niezbędnych modułów
import sys
from nltk.tokenize import word_tokenize
import re
from nltk.probability import FreqDist
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words("english")

nazwa_pliku = sys.argv[1]



#==========================================================================
### Funkcja I
def pop_100(plik):
    '''Funkcja pop_100 oblicza jaki procent tekstu stnanowi 100 najczęściej
    występujących wyrazów w tekście'''

    words = re.findall(r'\w+', open(plik).read().lower())
    popularne = FreqDist(words).most_common(100)

    #zlicza najpopularniejsze wyrazy
    liczba_popularne = 0
    for i in range(len(popularne)):
        liczba_popularne +=popularne[i][1]

    procent = (liczba_popularne/len(words))*100
    return procent;



#==========================================================================
### Funkcja II
def pop_1000(plik):
    '''Funkcja pop_1000 oblicza jaki procent tekstu stnanowi 1000 najczęściej
    występujących wyrazów w tekście'''

    words = re.findall(r'\w+', open(plik).read().lower())
    popularne = FreqDist(words).most_common(1000)

    #zlicza najpopularniejsze wyrazy
    liczba_popularne = 0
    for i in range(len(popularne)):
        liczba_popularne +=popularne[i][1]


    procent = (liczba_popularne/len(words))*100
    return procent;



#==========================================================================
### Funkcja III
def slowa_stop(plik):
    """Funkcja slowa_stop zwraca jaki procent tekstu stanowią słowa niedeterminujące
    kontekstu tekstu"""
    words = re.findall(r'\w+', open(plik).read().lower())
    zliczenia =FreqDist(words)
    slowa_stop = stopwords.words("english")

    liczba_stop = 0
    for i in range(len(slowa_stop)):
        liczba_stop +=zliczenia[slowa_stop[i]]
    procent = (liczba_stop/len(words))*100
    return procent;



#==========================================================================
### Funkcja IV
def liczby(plik):
    """Funkcja liczy określa ile liczb znajduje się w tekscie"""
    numbers = re.findall(r'\d+', open(plik).read())
    ile_liczb=len(numbers)
    return ile_liczb;



#==========================================================================
### Funkcja V
def tresc(plik):
    """Funkcja tresc wyznacz 10 najpopularniejszych wyrazow charakterystycznych dla danego tekstu"""

    words = re.findall(r'\w+', open(plik).read().lower())
    zbior = {'stworz', 'zbior'}
    for i in range(len(words)):
        zbior.add(words[i])
    zbior.remove('stworz')
    zbior.remove('zbior')

    slowa_stop = stopwords.words("english")
    for i in range(len(slowa_stop)):
        zbior.add(slowa_stop[i])

    for i in range(len(slowa_stop)):
        zbior.remove(slowa_stop[i])

    popularne = FreqDist(words).most_common(100)
    top10 = {'stworz', 'zbior'}
    i=0
    while len(top10)<12:
        if popularne[i][0] in zbior:
            top10.add(popularne[i][0])
            i = i+1
        else:
            i = i+1

    top10.remove('stworz')
    top10.remove('zbior')

    return top10;



#==========================================================================
### Funkcja VI
def najdluzszy(plik):
    """Funkcja najdluzszy zwraca zbior sklada sie z wyrazow skladajacych sie z najwiekszej liczby liter"""
    words = re.findall(r'\w+', open(plik).read().lower())
    najdluzszy_wyraz = 0

    for i in range(len(words)):
        if len(words[i])>najdluzszy_wyraz:
            najdluzszy_wyraz = len(words[i])

    zbior = {'stworz', 'zbior'}
    for i in range(len(words)):
        if (len(words[i])==najdluzszy_wyraz):
            zbior.add(words[i])

    zbior.remove('stworz')
    zbior.remove('zbior')
    return zbior;



#==========================================================================
print("\n\n")
print("================================================ Raport================================================")
print("Nazwa załadowanego pliku:")
print(nazwa_pliku)
print("\n")


print("100 najpopularniejszych wyrazów stanowi",round(pop_100(nazwa_pliku),2),"% tekstu")
print("1000 najpopularniejszych wyrazów stanowi",round(pop_1000(nazwa_pliku),2),"% tekstu")
print("Słowa stop stanowią",round(slowa_stop(nazwa_pliku),2),"% tekstu")
print("Liczba liczb występujących w tekście: ",liczby(nazwa_pliku))
print("\n")
print("10 najpopularniejszych wyrazów charakterystycznych dla",nazwa_pliku,": " )
print(tresc(nazwa_pliku))
print("\n")
print("Najdłuższe wyrazy w", nazwa_pliku, ": ")
print(najdluzszy(nazwa_pliku))
print("================================================ Raport================================================")
print("\n")



#==========================================================================
