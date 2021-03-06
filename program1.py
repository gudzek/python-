
import matplotlib.pyplot as plt                                             #importuję bilbiotekę która będzie mi potrzeba w dalszych etapach programu

print("Program rysuje wielomiany stopnia co najwyżej 4 o współczynnikach z przedziału (-10;10)")
                                                                            #informuję użytkownika co może zrobić

a_4 = int(input("Podaj współczynik przy x^4 >  "))                          #program pyta użytkownika o kolejne współczynniki
a_3 = int(input("Podaj współczynik przy x^3 >  "))
a_2 = int(input("Podaj współczynik przy x^2 >  "))
a_1 = int(input("Podaj współczynik przy x >  "))
a_0 = int(input("Podaj wyraz wolny >  "))


if abs(a_4)>10 or abs(a_3)>10 or abs(a_2)>10 or abs(a_1)>10 or abs(a_0)>10:
	print("Podałeś złe współczynniki, spróbuj jeszcze raz ")				#sprawdzam czy podane współczynniki są z przedziału
	quit()																	# (-10;10) - jeżeli nie - to zamykam Program

print(f"Podałeś wielomian f(x)={a_4}x^4+{a_3}x^3+{a_2}x^2+{a_1}x+{a_0}")    #program informuje jaki wielomian podał użytkownik


X = []                                                                      #tworzę pusty wektor dla X i Y
Y = []

i = -100                                                                    #zaczynam iterację od -100 i kończę na 100 aby otrzymać
j = -100                                                                    #symetryczne odcinki po dodatniej i ujemnej osi X
while i<=100:
    X.append(i)                                                             #dodaję "i" do wektora "X"
    i = i + 1

while j<=100:
    Y.append(a_4*j*j*j*j + a_3*j*j*j + a_2*j*j + a_1*j +a_0)                #dodaje wartość wielomianu w punkie "i" do wektora Y
    j = j + 1

plt.plot(X,Y)                                                               #rysuję wykres
plt.show()                                                                  #pokazuję wykres
