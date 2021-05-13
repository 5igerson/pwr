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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Tw1     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Tzew jako zmienna
% for QgN=15000:5000:25000
%     %figure;
%     
%     i=1
%     for TzewN=-40:0.1:40
%    
%         Tw1(i)=(QgN+Ks1*TzewN+(Ks0*Ks2*TzewN)/(Ks2+Ks0))/(Ks1+Ks0-(Ks0)^2/(Ks2+Ks0));
%         i=i+1;
%     end
%     
%     plot(-40:0.1:40,Tw1);
%         xlabel('T zew');
%     ylabel('Tw1');
%     hold on
% end
% 
% figure;
% %Q jako zmienna
% for TzewN=-30:10:10
%     %figure;
%     
%     i=1
%     for QgN=-40000:100:40000
%    
%         Tw1(i)=(QgN+Ks1*TzewN+(Ks0*Ks2*TzewN)/(Ks2+Ks0))/(Ks1+Ks0-(Ks0)^2/(Ks2+Ks0));
%         i=i+1;
%     end
%     
%     plot(-40:0.1:40,Tw1);
%     xlabel('Qg');
%     ylabel('Tw1');
%     hold on
% end
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Tw2      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% figure;
% %TzewN jako zmienna
% for QgN=15000:5000:25000
%     %figure;
%     
%     i=1
%     for TzewN=-40:0.1:40
%    
%         Tw2(i)=(QgN*Ks0+Ks1*Ks2*TzewN+Ks1*Ks0*TzewN+Ks0*Ks2*TzewN)/(Ks1*Ks2+Ks1*Ks0+Ks0*Ks2);
%         i=i+1;
%     end
%     
%     plot(-40:0.1:40,Tw2);
%     xlabel('T zew');
%     ylabel('Tw2');
%     hold on
% end
% 
% 
% figure;
% %Q jako zmienna
% for TzewN=-30:10:10
%     
%     
%     i=1
%     for QgN=-40000:100:40000
%    
%         Tw2(i)=(QgN*Ks0+Ks1*Ks2*TzewN+Ks1*Ks0*TzewN+Ks0*Ks2*TzewN)/(Ks1*Ks2+Ks1*Ks0+Ks0*Ks2);
%         i=i+1;
%     end
%     
%     plot(-40:0.1:40,Tw2);
%     xlabel('Qg');
%     ylabel('Tw2');
%     hold on
% end

QgN=20000;
TzewN=-20;
T1N=20;
T2N=15;
dqg=1000;
dTzew=0;
ro=1.2;
cp=1005;
v1=90;
v2=30;
dT2N=5;
% 
% v1=60;
% v2=21;

Ks2=QgN/(3*(T1N-TzewN)+T2N-TzewN)
Ks1=3*Ks2
Ks0=(Ks2*(T2N-TzewN))/(T1N-T2N)

% Ks1 = QgN/((T1N-TzewN)+(1/3)*(T2N-TzewN));
% Ks2 = (1/3)*Ks1;
% Ks0 = (Ks2*(T2N-TzewN))/(T1N-T2N);

steptime=100;
Qfinalvalue=QgN+dqg;
Tzewfinalvalue=TzewN+dTzew;
tw1intinit=T1N;
tw2intinit=T2N;


cv1=ro*cp*v1;
cv2=ro*cp*v2;

%tw10=(Qfinalvalue*(cv2+Ks0+Ks2)+Tzewfinalvalue*(Ks1*cv2*s+Ks0*Ks1+Ks2*Ks1+Ks0*Ks2))/(cv1*s^2*cv2+cv1*s*Ks0+cv1*s*Ks2+Ks1*cv2*s+Ks0*Ks1+Ks0*cv2*s+Ks2*Ks0)
%tw20=(Ks0*Qfinalvalue+Tzewfinalvalue*(Ks0*Ks1+Ks2*cv1*s+Ks1*Ks2+Ks0*Ks2))/(cv2*s^2*cv1+cv2*s*Ks1+cv2*s*Ks0+cv1*s*Ks0+Ks0*Ks1+Ks2*cv1*s+Ks1*Ks2+Ks0*Ks2)

% tw10u=[Tzewfinalvalue*Ks1*cv2 Qfinalvalue*(cv2+Ks0+Ks2)+Tzewfinalvalue*(Ks0*Ks1+Ks2*Ks1+Ks0*Ks2)]

tw10d=[cv1*cv2 cv1*Ks0+cv1*Ks2+Ks1*cv2+Ks0*cv2 Ks0*Ks1+Ks2*Ks0+Ks1*Ks2]

% tw10d=[(cv1*cv2) ((cv1*(Ks0+Ks2))+(cv2*(Ks0+Ks1))) ((Ks0*Ks1)+(Ks1*Ks2)+(Ks0*Ks2))];

% tw20u=[Tzewfinalvalue*Ks2*cv1 Ks0*Qfinalvalue+Tzewfinalvalue*(Ks0*Ks1+Ks1*Ks2+Ks0*Ks2)]
% tw20d=[cv2*cv1 cv2*Ks1+cv2*Ks0+cv1*Ks0+Ks2*cv1 Ks0*Ks1+Ks0*Ks2]

%Tw10=((Ks2+Ks0)*(Qfinalvalue+(Ks1*Tzewfinalvalue))+(Ks0*Ks2*TzewN))/((Ks2+Ks0)*(Ks1+Ks0)-Ks0^2);
%Tw20=(((Ks0*Qfinalvalue)+(Ks0*Ks1*Tzewfinalvalue))+Ks2*Tzewfinalvalue*(Ks1+Ks0))/((Ks2+Ks0)*(Ks1+Ks0)-Ks0^2);
% 
%  G1=[(Ks1*cv2) (Ks0*Ks1+Ks2*Ks1+Ks0*Ks2)];
%  G2=[cv1 Ks0+Ks2]
%  G3=[(Ks2*cv1) (Ks1*Ks2+Ks0*Ks2+Ks0*Ks1)]
%  G4=[Ks0]



Tw20 = TzewN + (QgN*Ks0)/((Ks0*Ks1)+(Ks0*Ks2)+(Ks1*Ks2));
Tw10 = (QgN * (Ks0+Ks2)+TzewN*((Ks0*Ks1)+(Ks0+Ks2)+(Ks1*Ks2)))/((Ks0+Ks1)*(Ks0+Ks2)-Ks0^2);


%model kupfmullera
T=300;
T_0=10;
k=1.75/dqg;

Kp_nichols=(0.9*T)/(k*T_0)*1.5;
Kp_nichols=(0.9*T)/(k*T_0);
% Kp_nichols=100000
Ti_nichols=3.33*T_0;

% Kp_chien20=(0.6*T)/(k*T_0)*2.61;
Kp_chien20=(0.6*T)/(k*T_0);
Ti_chien20=T;

Kp_chien0=(0.35*T)/(k*T_0)*4.49;
Ti_chien0=1.2*T;

% figure;
% a=sim('zaj3simulink.slx',2000);
a=sim('zaj8simulink.slx',2000);
% a=sim('sprawko3simulink.slx',2000);
% plot(a.time_vektor,a.tw1out);
% 
% figure;
% plot(a.time_vektor,a.tw2out);

