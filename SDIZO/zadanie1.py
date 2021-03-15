import numpy as np
import configparser
import pandas as pd
import random
import timeit
import os

clear = lambda: os.system('cls')
clear()

#----------------------------------------------
def calculate_menu(dane):

    print("1 - oblicz srednia arytmetyczna")
    print("2 - oblicz wartosc minimalna oraz maksymalna")
    print("3 - oblicz mediane")
    print("0 - jednak nic")

    opcja_liczenia=int(input())
    clear()

    if opcja_liczenia==1:
        start = timeit.timeit()
        print("srednia artymetyczna: ",np.mean(dane))
        end = timeit.timeit()
        print("czas srednia arytmetyczna",(end - start)*1000,"ms")
    elif opcja_liczenia==2:
        start = timeit.timeit()
        print("min: ",min(dane))
        end = timeit.timeit()
        print("czas min",(end - start)*1000,"ms")

        start = timeit.timeit()
        print("max: ",max(dane))
        end = timeit.timeit()
        print("czas max",(end - start)*1000,"ms")
    elif opcja_liczenia==3:
        start = timeit.timeit()
        print("mediana: ",np.median(dane))
        end = timeit.timeit()
        print("czas mediana: ",(end - start)*1000,"ms")
    elif opcja_liczenia==0:
        return

#----------------------------------------------
def read_data(wejscie):

    dane=pd.read_csv(wejscie)
    dane=pd.DataFrame.to_numpy(dane)
    print("Wczytano dane z pliku .csv")
    return dane
#----------------------------------------------
def generate_data(min,max,n):
    dane=np.zeros((n,1))
    for i in range(n):
        dane[i]=random.randint(min,max)

    print(dane)
    return dane
#----------------------------------------------
def save_data(dane,wejscie):

    dane=pd.DataFrame(dane)
    dane.to_csv(wejscie,index=False)
    print("zapisano dane do pliku: ",wejscie)

#----------------------------------------------
def initialize():
    config = configparser.ConfigParser()
    try:
        config.read(r'SDIZO\init.ini')
    except:
        print("cos nie dziala")
    else:
        pass

    print("sekcje w pliku init: ",config.sections())

    min1=config.getint('parameters','min')
    max1=config.getint('parameters','max')
    ilosc_liczb=config.getint('parameters','ilosc_liczb')
    wejscie=config.get('path','dane')
    wyjscie=config.get('path','wyjsciowe')

    return min1,max1,ilosc_liczb,wejscie,wyjscie

def menu():

    print("\n\n1 - wczytaj plik inicjujacy")
    print("2 - generuj dane")
    print("3 - zapisz dane")
    print("4 - wczytaj dane")
    print("5 - Przejdz do menu obliczen - obliczenia korzystajac z gotowych funkcji")
    print("6 - Przejdz do menu obliczen - obliczenia korzystajac z funkcji wlasnych")
    print("0 - wyjscie z programu")
    
    wybor=int(input())

    return wybor
#-----------------------------------------------

while(True):
    wybor=menu()
    clear()
    if wybor==1:
        [min1,max1,ilosc_liczb,wejscie,wyjscie]=initialize()
    elif wybor==2:
        dane=generate_data(min1,max1,ilosc_liczb)
    elif wybor==3:
        save_data(dane,wejscie)
    elif wybor==4:
        dane=read_data(wejscie)
    elif wybor==5:
        calculate_menu(dane)
    elif wybor==6:
        print("tu bedzie menu gotowych funkcji")
    elif wybor==0:
        break
    else:
        print("wybrano niepoprawna opcje!")



