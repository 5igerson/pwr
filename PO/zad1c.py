import numpy as np

def jacobi(A,B,n):

    print("\n\nMetoda Jacobiego\n")

    x=np.zeros((n,1))
    xy=np.zeros((n,1))
    iterations=100

    for k in range(iterations):
        #print("iteration ",k,"\n")
        for i in range(n):
            sum=0
            for j in range(n):
                if not(j==i):
                    sum=sum+A[i,j]*x[j]
            xy[i]=-1/A[i,i]*(sum-B[i])
        x=xy
    

    print("rozwiazanie: \n",x)

    print("sprawdzenie (iloczynem): \n\n",A@x)
  


n=int(input("Ile ma byc niewiadomych: "))

A=np.zeros((n,n))
B=np.zeros((n,1))

for i in range(n):
    for j in range(n):
        print("A[",i,"][",j,"]: ")
        A[i][j]=float(input())


for i in range(n):
    print("B[",i,"]: ")
    B[i]=float(input())

print("A: \n",A)
print("B: \n",B)
jacobi(A,B,n)
