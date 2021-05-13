#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <softPwm.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/* Zadanie 2.1 */
int main (void)
{
int fd;

int adressMPU6050=0x69;


int dane[2]; /* tablica przechowujaca dane odczytane z podanych rejestrow */

if(wiringPiSetup() == -1)
exit(1);

/* inicjalizacja interfejsu I2C */
if((fd=wiringPiI2CSetup(adressMPU6050)) == -1){
printf("error initialize I2C");
exit(1);
}
printf("I2C modul MPU6050\r\n");

//Uruchamia pomiary
int regPWR=0x68; //<<---- podaæ adres rejestru PWR_MGMT_1
wiringPiI2CWriteReg8(fd, regPWR, 0);

//Odczytanie rejestru WHO_AM_I
int regWho=0x75;//<<---- podac adres rejestru Who Am I

dane[0] = wiringPiI2CReadReg8(fd,regWho); /*odczyt z rejestru Who Am I */

printf("Praca studentow: 244057 i 241675 - 9.04.2021 \n");
printf("I am: %d\r\n",dane[0]);

return 0;
}
