#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <softPwm.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main (void)
{
int fd;
int adressMPU6050=0x69;
int dane[2]; /* tutaj zapisywane sa odczyty z rejestrow */

if(wiringPiSetup() == -1)
exit(1);

if((fd=wiringPiI2CSetup(adressMPU6050)) == -1){
printf("error initialize I2C");
exit(1);
}
printf("I2C modul MPU6050\r\n");

//Uruchamia pomiary
int regPWR=0x68; //<<---- podaæ adres rejestru PWR_MGMT_1
wiringPiI2CWriteReg16(fd, regPWR, 0);

//Odczytanie rejestru TEM_OUT_H
int regTEMP_OUT_H=0x41;//<<---- podac adres rejestru TEMP_OUT_H
int regTEMP_OUT_L=0x42; // adres rejestru TEMP_OUT_L

dane[0] = wiringPiI2CReadReg8(fd,regTEMP_OUT_H); /* Odczyt danych z rejestru TEMP_OUT_H */
dane[1] = wiringPiI2CReadReg8(fd,regTEMP_OUT_L); /* Odczyt danych z rejestru TEMP_OUT_L */

int16_t rawTemp = (dane[0]<<8)|dane[1]; /* zmienna przechowujaca 'surowy' pomiar temperatury */
/* na zmiennej dane[0] przeprowadzono operacje przesuniecia bitowego o 8 bitow w prawo oraz suma
 otrzymanej wartosci z odczytem danych pochadzacych z rejestru TEMP_OUT_L  */

float temperatura=((rawTemp/340)+36.53); /* przeliczenie odczytanego pomiaru na stopnie Celsjusza */

printf("Praca studentow: 244057 i 241675 - 9.04.2021 \n");
printf("\nTemperatura wynosi: %f\r\n",temperatura );

return 0;
}
