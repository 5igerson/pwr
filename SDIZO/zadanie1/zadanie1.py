import numpy as np
import configparser
import pandas as pd
import random
from time import time
import timeit
import os
import math

clear = lambda: os.system('cls')
clear()


def data_sort(dane):
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

    return data_sort(mniejszy)+[pivot]+data_sort(wiekszy)
#----------------------------------------------
def calc_mean(dane):

    suma=0
    for i in range(len(dane)):
        suma+=dane[i]

    srednia=suma/len(dane)

    return srednia
#----------------------------------------------
def calc_min(dane):
    najmniejsza=dane[0]
    for i in range(len(dane)):
        
        if dane[i]<najmniejsza:
            najmniejsza=dane[i]

    return najmniejsza
#----------------------------------------------
def calc_max(dane):
    najwieksza=dane[0]
    for i in range(len(dane)):
        
        if dane[i]>najwieksza:
            najwieksza=dane[i]

    return najwieksza
#----------------------------------------------
def calc_median(dane):
    length=(len(dane)-1)/2
    if len(dane)%2==0:
        mediana=(dane[math.ceil(length)]+dane[int(length)])/2
    elif len(dane)%2==1:
        mediana=dane[int(length)]
    else:
        print("cos nie tak")


    return mediana
#----------------------------------------------
def calculate_menu(dane,wyjscie,czasy,wejscie1,n):

    print("Oblicz:")
    print("1-srednia arytmetyczna")
    print("2-wartosc min")
    print("3-wartosc max")
    print("4-mediana")
    operacja=int(input("Twoj wybor: "))
    clear()
    dfdict={}
    if operacja==1:

        #liczenie sredniej arytmetycznej
        start = time()
        srednia_arytm=float(calc_mean(dane))
        print("srednia artymetycznad: ",srednia_arytm)
        end = time()
        czas_srednia_arytm=(end - start)*1000
        print("czas srednia arytmetyczna: %.4f ms" %czas_srednia_arytm)
        dfdict["co liczone"]=["wartosc srednia arytmetyczna"]
        dfdict["wynik co liczone"]=[srednia_arytm]
        dfdict["napis ilosc instancji"]=["ilosc instancji"]
        dfdict["ilosc instancji"]=[n]
        dfdict["napis czas wykonania"]=["czas wykonania"]
        dfdict["czas wykonania"]=[czas_srednia_arytm]
        df=pd.DataFrame(dfdict)
        df.to_csv(wyjscie,sep=";",header=False,index=False,mode='a',decimal=",")
        print("zapisano dane do pliku: ",wyjscie)


    elif operacja==2:
        #liczenie wartosci min
        start = time()
        wartosc_min=float(calc_min(dane))
        print("min: ",wartosc_min)
        end = time()
        czas_min=(end - start)*1000
        print("czas min: %.4f ms" %czas_min)
        dfdict["co liczone"]=["wartosc min"]
        dfdict["wynik co liczone"]=[wartosc_min]
        dfdict["napis ilosc instancji"]=["ilosc instancji"]
        dfdict["ilosc instancji"]=[n]
        dfdict["napis czas wykonania"]=["czas wykonania"]
        dfdict["czas wykonania"]=[czas_min]
        df=pd.DataFrame(dfdict)
        df.to_csv(wyjscie,sep=";",header=False,index=False,mode='a',decimal=",")
        print("zapisano dane do pliku: ",wyjscie)

    elif operacja==3:
        #liczenie wartosci max
        start = time()
        wartosc_max=float(calc_max(dane))
        print("max: ",wartosc_max)
        end = time()
        czas_max=(end - start)*1000
        print("czas max: %.4f ms" %czas_max)
        dfdict["co liczone"]=["wartosc max"]
        dfdict["wynik co liczone"]=[wartosc_max]
        dfdict["napis ilosc instancji"]=["ilosc instancji"]
        dfdict["ilosc instancji"]=[n]
        dfdict["napis czas wykonania"]=["czas wykonania"]
        dfdict["czas wykonania"]=[czas_max]
        df=pd.DataFrame(dfdict)
        df.to_csv(wyjscie,sep=";",header=False,index=False,mode='a',decimal=",")
        print("zapisano dane do pliku: ",wyjscie)

    elif operacja==4:
        #liczenie mediany
        start = time()
        dane_posortowane=data_sort(dane.tolist())
        wartosc_mediana=float(calc_median(np.array(dane_posortowane)))
        print("mediana: ",wartosc_mediana)
        end = time()
        czas_mediana=(end - start)*1000
        print("czas mediany: %.4f ms" %czas_mediana)
        dfdict["co liczone"]=["wartosc mediana"]
        dfdict["wynik co liczone"]=[wartosc_mediana]
        dfdict["napis ilosc instancji"]=["ilosc instancji"]
        dfdict["ilosc instancji"]=[str(n)]
        dfdict["napis czas wykonania"]=["czas wykonania"]
        dfdict["czas wykonania"]=[str(czas_mediana)]
        df=pd.DataFrame(dfdict)
        df.to_csv(wyjscie,sep=";",header=False,index=False,mode='a',decimal=",")
        print("zapisano dane do pliku: ",wyjscie)
        dane=np.append(dane,wartosc_mediana)
        dane_posortowane=sorted(dane.tolist())
        dane_posortowane=pd.DataFrame(dane_posortowane)
        dane_posortowane.to_csv(wejscie1,index=False)
        print("dodano mediane do pliku: ",wejscie1)

    wybor=9
    return wybor
#----------------------------------------------
def read_data(wejscie,n):
    n=int(n)
    dane=pd.read_csv(wejscie)
    dane=pd.DataFrame.to_numpy(dane)
    print("Wczytano dane z pliku .csv")
    return dane[0:n]
#----------------------------------------------
def generate_data(min,max,n):
    dane=np.zeros((n,1))
    for i in range(n):
        dane[i]=random.randint(min,max)

    print("wygenerowano dane")
    return dane
#----------------------------------------------
def save_data(dane,wejscie):

    dane=pd.DataFrame(dane)
    dane.to_csv(wejscie,index=False)
    print("zapisano dane do pliku: ",wejscie)
#----------------------------------------------
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

    min1=-1000000
    max1=1000000
    ilosc_liczb=10000000
    wejscie=config.get('path','dane')
    wejscie1=config.get('path','dane1')
    wyjscie=config.get('path','wyjsciowe')
    n=config.get('variables','n')

    return min1,max1,ilosc_liczb,wejscie,wyjscie,n,wejscie1
#----------------------------------------------
def menu():

    print("\n\n1 - wczytaj plik inicjujacy")
    print("2 - generuj dane")
    print("3 - zapisz dane")
    print("4 - wczytaj dane")
    print("5 - Przejdz do menu obliczen")
    print("0 - wyjscie z programu")
    
    wybor=int(input("Twoj wybor: "))

    return wybor
#-----------------------------------------------

while(True):
    wybor=9
    wybor=menu()
    clear()
    if wybor==1:
        min1,max1,ilosc_liczb,wejscie,wyjscie,n,wejscie1=initialize()
        
    elif wybor==2:
        dane=generate_data(min1,max1,ilosc_liczb)
    elif wybor==3:
        save_data(dane,wejscie)
    elif wybor==4:
        dane=read_data(wejscie,n)
    elif wybor==5:
        wybor=calculate_menu(dane,wyjscie,n,wejscie1,n)
    elif wybor==0:
        break






            start = time()
            insert_sort(new_data.tolist())
            end = time()
            print("czas sortowania przez wstawianie wynosi: ",(end-start)*1000)
            save_out("insert sort",(end-start)*1000,data_out,n[i])
            save_data(cs_data, "dane1.csv")


            def insert_sort(data):

    for i in range(len(data)):
        pomocnicza=data[i]
        j=i-1
        while j>=0 and data[j]>pomocnicza:
            data[j+1] = data[j]
            j=j-1
            data[j+1]=pomocnicza

    return data