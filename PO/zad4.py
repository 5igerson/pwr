import numpy as np
import scipy
from scipy import linalg

#podana macierz
A=[[3,1,2],[1,8,1],[2,1,1]]
A=[[2,5,9],[5,4,3],[9,3,1]]
#funkcja zwraca wartosci wlasne macierzy i wektory wlasne macierzy
wartosci,wektory=np.linalg.eig(A)

#wyswietlanie wartosci wlasnych
print("wartosci wlasne macierzy: ")
print(wartosci)
print("wektory wlasne macierzy: ")
print(wektory.T)

#-----normalizacja wynikow otrzymanych z wolframalpha------

#wprowadzanie wektorow wlasnych otrzymanych z wolframalpha
matrix3=[1.13254,0.880783,1]
matrix2=[-1.02431,0.181739,1]
matrix1=[0.630895,-1.94658,1]




#normalizacja wektorow
matrix1 = matrix1/np.linalg.norm(matrix1)
matrix2 = matrix2/np.linalg.norm(matrix2)
matrix3 = matrix3/np.linalg.norm(matrix3)

#budowanie macierzy ze znormalizowanych wektorow
matrix=np.asarray([np.asarray(matrix3),np.asarray(matrix2),np.asarray(matrix1)])*-1
print("znormalizowane wartosci wektorow z Wolframalpha: ")

print(matrix)
