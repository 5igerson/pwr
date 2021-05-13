#include<stdio.h>
#include<wiringPi.h>
#include<wiringPiSPI.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

 int chan = 0;
  int speed = 1000000;
  int t_fine;
  
  enum {
  BMP280_REGISTER_DIG_T1 = 0x88,
  BMP280_REGISTER_DIG_T2 = 0x8A,
  BMP280_REGISTER_DIG_T3 = 0x8C,
  BMP280_REGISTER_DIG_P1 = 0x8E,
  BMP280_REGISTER_DIG_P2 = 0x90,
  BMP280_REGISTER_DIG_P3 = 0x92,
  BMP280_REGISTER_DIG_P4 = 0x94,
  BMP280_REGISTER_DIG_P5 = 0x96,
  BMP280_REGISTER_DIG_P6 = 0x98,
  BMP280_REGISTER_DIG_P7 = 0x9A,
  BMP280_REGISTER_DIG_P8 = 0x9C,
  BMP280_REGISTER_DIG_P9 = 0x9E,
  BMP280_REGISTER_CHIPID = 0xD0,
  BMP280_REGISTER_VERSION = 0xD1,
  BMP280_REGISTER_SOFTRESET = 0xE0,
  BMP280_REGISTER_CAL26 = 0xE1, /**< R calibration = 0xE1-0xF0 */
  BMP280_REGISTER_STATUS = 0xF3,
  BMP280_REGISTER_CONTROL = 0xF4,
  BMP280_REGISTER_CONFIG = 0xF5,
  BMP280_REGISTER_PRESSUREDATA = 0xF7,
  BMP280_REGISTER_TEMPDATA = 0xFA,
};


typedef struct {
  uint16_t dig_T1; /**< dig_T1 cal register. */
  int16_t dig_T2;  /**<  dig_T2 cal register. */
  int16_t dig_T3;  /**< dig_T3 cal register. */

  uint16_t dig_P1; /**< dig_P1 cal register. */
  int16_t dig_P2;  /**< dig_P2 cal register. */
  int16_t dig_P3;  /**< dig_P3 cal register. */
  int16_t dig_P4;  /**< dig_P4 cal register. */
  int16_t dig_P5;  /**< dig_P5 cal register. */
  int16_t dig_P6;  /**< dig_P6 cal register. */
  int16_t dig_P7;  /**< dig_P7 cal register. */
  int16_t dig_P8;  /**< dig_P8 cal register. */
  int16_t dig_P9;  /**< dig_P9 cal register. */
} bmp280_calib_data;

bmp280_calib_data calib_data;
  
  int writeRegister(int adress,int data) {
	 unsigned char buff[2];
	buff[0]=(adress& ~0x80);
	buff[1]=data;
	wiringPiSPIDataRW(chan, buff, 2);
	return 1;
}

int readRegister(int adress) {
	 unsigned char buff[2];
	buff[0]=(adress | 0x80);
	wiringPiSPIDataRW(chan, buff, 2);
	return buff[1];
}

void init() {
short unsigned wartosc=0;
wartosc=0xb6;

writeRegister(BMP280_REGISTER_SOFTRESET, wartosc);
delay(600);

writeRegister(BMP280_REGISTER_CONTROL, 0b00100111); //0x57 oversampling T=1 , oversampling P=1 , tryb:normal
delay(600);

writeRegister(BMP280_REGISTER_CONFIG, 0b01000000);// 125 ms , brak filtra , 4 wires
delay(600);

//kalibracaja temperatury
calib_data.dig_T1 = (readRegister(0x89) << 8) | (readRegister(0x88));
calib_data.dig_T2 = (readRegister(0x8B) << 8) | (readRegister(0x8A));
calib_data.dig_T3 = (readRegister(0x8D) << 8) | (readRegister(0x8C));

delay(1000);				   
}


//wzor z dokumentacji 
int32_t bmp280_compensate_T_int32(int32_t adc_T){ 
	int32_t var1, var2, T;

	var1 = ((((adc_T >> 3) - ((int32_t)calib_data.dig_T1 << 1))) * ((int32_t)calib_data.dig_T2)) >> 11;
	var2 = (((((adc_T >> 4) - ((int32_t)calib_data.dig_T1)) * ((adc_T >> 4) - ((int32_t)calib_data.dig_T1))) >> 12) * ((int32_t)calib_data.dig_T3)) >> 14;

	t_fine = var1 + var2 ;
	T = (t_fine * 5 + 128) >> 8;
	return T;
}

int main()
{
   
    if (wiringPiSPISetup(chan, speed) == -1)
    {
        printf("Could not initialise SPI\n");
        return 0;
    }
    
	init();
	delay(600);

	int id=readRegister(BMP280_REGISTER_CHIPID);
    int tempr=readRegister(0xFA)<<12|readRegister(0xFB)<<4|readRegister(0xFC)>>4;
    float temperature=bmp280_compensate_T_int32(tempr);
    temperature/=100;
		
    printf("Czujnik BMP280 - ChipID: %x\r\n",id);
    printf("Temperatura odczytana z czujnika BMP280: %f [C]\n",temperature);

	
	return 0;
}
