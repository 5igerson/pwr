 
import numpy as np


def gaus_seidl(A,B,n):

    print("Metoda Gausa-Seidla\n")

    L=np.tril(A,-1)
    U=np.triu(A,1)
    D=A-U-L
    revD = np.linalg.inv(D)

    print("D: \n",D)
    print("U: \n",U)
    print("L: \n",L)

    Db=np.diag(revD*B)
    DL=revD@L
    DU=revD@U
    

    print("reverse: \n",revD)
    print("Db: \n",Db)
    print("DL: \n",DL)
    print("DU: \n",DU)

    x=np.zeros((n,1))
    xy=np.zeros((n,1))
    iterations=100


    tol=1e-6


    for k in range(iterations):
        convergance=False
        for i in range(n):
            sum=0
            for j in range(n):
                if not(j==i): 
                    sum=sum+A[i,j]*x[j]               
            xy[i]=-1/A[i,i]*(sum-B[i])
            if abs(xy[i]-x[i])>tol:
                print("iterations\n\n",k)

                convergance=True
            if convergance:
                break
        x=xy


    print("iterations\n\n",k)
    print("solution: \n",x)

    print("sprawdzenie: \n\n",A@x)
    P=1
    return P

    
    


""" A=([2,1,1,-3],
   [1,1,-1,1],
   [1,1,1,1],
   [-1,2,-1,1])

B=([3,4,10,4]) """



n=int(input("Ile ma byc niewiadomych: "))

A=np.zeros((n,n))
B=np.zeros((n,1))

for i in range(n):
    for j in range(n):
        print("A[",i,"][",j,"]: ")
        A[i][j]=int(input())


for i in range(n):
    print("B[",i,"]: ")
    B[i]=int(input())

print("A: \n",A)
print("B: \n",B)
gaus_seidl(A,B,n)
