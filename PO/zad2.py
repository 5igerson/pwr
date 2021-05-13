import numpy as np
from scipy.misc import derivative
from math import sin
from math import log10
from timeit import default_timer

#definicja funkcji i wprowadzanie parametrow
def reg_falsi(f,a,b,tolerancja=1E-9,iteracje=100):
    start=default_timer()
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
        print("Brak rozwiazan (moze jest wiecej niz jedno rozwiazanie)")
        iter=0
        xi=0
    stop=default_timer()
    return xi,iter,stop-start

#wprowadzanie przedzialu 
print("Prosze wprowaadzic przedzial")
a=float(input("Wprowadz wartosc a: "))
b=float(input("Wprowadz wartosc b: "))

#pierwsza funkcja podana przez prowadzacego
funkcja=lambda x: -sin(x)**2+log10(x)

#druga funkcja podana przez prowadzacego
#funkcja=lambda x: x**2-sin(x)+log10(x)

#wykonaj zadeklarowana funkcje i zwroc wartosc rozwiazania i ilosc iteracji
rozwiazanie,iteracja,czas_wykonania=reg_falsi(funkcja,a,b)
print("Rozwiazanie wynosi: ",rozwiazanie)
print("Wykonano %d iteracji" %iteracja)
print("Czas wykonania operacji wynosi: %.7f s" %czas_wykonania)

