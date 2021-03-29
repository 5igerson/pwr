import numpy as np
from scipy.misc import derivative
from math import sin
from math import log10

#definicja funkcji i wprowadzanie parametrow
def reg_falsi(f,a,b,tolerancja=1E-9,iteracje=100):

    #sprawdzamy czy wartosci przecinaja os OX
    if f(a)*f(b)<0:
        #petla wykonuje sie tyle razy ile ustalono iteracji
        for iter in range(1,iteracje+1):
            #implementacja wzoru podanego w instrukcji
            xi=(a*f(b)-b*f(a))/(f(b)-f(a))
            #sprawdzamy czy osiagnieto tolerancje - jesli tak to wychodzimy z funkcji
            if abs(f(xi))<tolerancja:
                break
            #jesli nie osiagnieto tolerancji to sprawdzamy ktora rzedna ma znak przeciwny
            elif f(a)*f(xi)<0:
                #jesli rzedna ma znak przeciwny do f(xi) to za b podstawiamy wartosc xi
                b=xi
            else:
                #jesli rzedna ma znak przeciwny do f(xi) to za a podstawiamy wartosc xi
                a=xi
    else:
        print("brak rozwiazan (moze jest wiecej niz jedno rozwiazanie)")
        iter=0
        xi=0

    return xi,iter

#wprowadzanie przedzialu 
print("Prosze wprowadzic przedzial")
a=float(input("wprowadz wartosc a: "))
b=float(input("wprowadz wartosc b: "))

#pierwsza funkcja podana przez prowadzacego
funkcja=lambda x: -sin(x)**2+log10(x)

#druga funkcja podana przez prowadzacego
#funkcja=lambda x: x**2-sin(x)+log10(x)

#wykonaj zadeklarowana funkcje i zwroc wartosc rozwiazania i ilosc iteracji
rozwiazanie,iteracja=reg_falsi(funkcja,a,b)
print("rozwiazanie wynosi: ",rozwiazanie)
print("wykonano %d iteracji" %iteracja)

