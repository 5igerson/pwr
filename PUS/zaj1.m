close all; 
clear all;
clc;

QgN=20000;
TzewN=-20;
T1N=20;
T2N=15;

Ks2=QgN/(3*(T1N-TzewN)+T2N-TzewN)
Ks1=3*Ks2
Ks0=(Ks2*(T2N-TzewN))/(T1N-T2N)

Tw2=(Ks0*T1N+Ks2*Tzew)/(Ks0+Ks2)
Tw1=