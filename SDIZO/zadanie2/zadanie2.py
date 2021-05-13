import random
import configparser
import os
import numpy as np
import pandas as pd
from time import time
import json

clear = lambda: os.system('cls')

def initialize():
    config = configparser.ConfigParser()
    clear()
    inicjujacy=input("Podaj nazwe pliku inicjujacego: ")
    try:
        config.read(inicjujacy.lower()+".ini")
    except:
        print("nie otworzono pliku ini")
    else:
        pass

    print("sekcje w pliku init: ",config.sections())

    min1=int(config.get('variables','min'))
    max1=int(config.get('variables','max'))
    ilosc_liczb=json.loads(config.get('variables','n'))
    dane_wejsciowe=config.get('path','dane')
    dane_wyjsciowe=config.get('path','daneposortowane')
    czasy=config.get('path','czasy')

    return min1,max1,ilosc_liczb,dane_wejsciowe,dane_wyjsciowe,czasy

def generate_data(min1,max1,ilosc_liczb):
    print("trwa generowanie danych")
    dane=np.zeros((ilosc_liczb,1))
    for i in range(ilosc_liczb):
        dane[i]=int(random.randint(min1,max1))

    print("wygenerowano dane")
    return dane

def menu():

    print("\n\n1 - wczytaj plik inicjujacy")
    print("2 - generuj dane")
    print("3 - zapisz dane")
    print("4 - wczytaj dane")
    print("5 - porownaj zlozonosc czasowa algorytmow")
    print("0 - wyjscie z programu")
    
    choice=int(input("Twoj wybor: "))

    return choice

def save_data(data,data_in):
    data=pd.DataFrame(data)
    data.to_csv(data_in,index=False)
    print("zapisano dane do pliku: ",data_in)

def save_out(alg,data,data_out,n):
    dfdict={}
    dfdict["alg"]=["algorytm"]
    dfdict["algorytm"]=[alg]
    dfdict["napis ilosc instancji"]=["ilosc instancji"]
    dfdict["ilosc instancji"]=[str(n)]
    dfdict["napis czas wykonania"]=["czas wykonania"]
    dfdict["czas wykonania"]=[str(data)]
    df=pd.DataFrame(dfdict)
    df.to_csv(data_out,sep=";",header=False,index=False,mode='a',decimal=",")
    print("zapisano dane do pliku: ",data_out)


    return 0

def read_data(data_in,nofnumbers):

    data=pd.read_csv(data_in)
    nofnumbers=max(nofnumbers)
    print("max to : ",nofnumbers)
    data=pd.DataFrame.to_numpy(data)
    print("Wczytano dane z pliku .csv")
    return data[0:nofnumbers]

def counting_sort(L,n):

    

    ilosc_unikalnych=1000*2+1
    tab_pom=np.zeros(ilosc_unikalnych)
    tab_wyjsciowa=np.zeros(len(L))

    

    for i in range(len(L)):
        val=int(L[i]+1000)
        tab_pom[val]+=1

    k=1
    while(k<ilosc_unikalnych):
        tab_pom[k]+=tab_pom[k-1]
        k+=1



    k=len(L)-1
    while(k>=0):
        val=int(L[k])+1000
        for i in range(int(tab_pom[val]-tab_pom[val-1])):
     
            tab_wyjsciowa[int(tab_pom[val-(1)]+i)]=int(val-1000)
            i=i+1

        
        k=k-1
    
    tab_wyjsciowa=tab_wyjsciowa.tolist()
    return tab_wyjsciowa

def bubblesort(data):

    
    for i in range(0,len(data)):
        #pivot=data[0]
        for j in range(0,len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
            
    return data

def quick_sort(dane):
    dlugosc=len(dane)
    if dlugosc <= 1:
        return dane
    else:
        pivot=dane.pop()

    wiekszy=[]
    mniejszy=[]
    for i in dane:
        if i >pivot:
            wiekszy.append(i)
        else:
            mniejszy.append(i)

    return quick_sort(mniejszy)+[pivot]+quick_sort(wiekszy)

def sort_data(data,data_out,n):


    print("1-zestaw E\n2-zestaw A\n")
    wybrano_zestaw=int(input("wybierz zestaw: "))
    for i in range(len(n)):
        print("wielkosc instancji: ",n[i])
        new_data=data[0:n[i]]


    
    
        start = time()
        qsort_data=quick_sort(new_data.tolist())
        end = time()
        print("czas quicksort wynosi: ",(end-start)*1000)
        save_out("quicksort",(end-start)*1000,data_out,n[i])


    return data

while(True):
    choice=9
    choice=menu()
    clear()
    
    if choice==1:
        min1,max1,nofnumbers,data_in,data_out,times=initialize()
        print("\n",nofnumbers)
    elif choice==2:
        data=generate_data(min1,max1,1000000)
    elif choice==3:
        save_data(data,data_in)
    elif choice==4:
        data=read_data(data_in,nofnumbers)
    elif choice==5:
        choice=sort_data(data,times,nofnumbers)
    elif choice==0:
        break
