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
for QgN=15000:5000:25000
    %figure;
    
    i=1
    for TzewN=-40:0.1:40
   
        Tw1(i)=(QgN+Ks1*TzewN+(Ks0*Ks2*TzewN)/(Ks2+Ks0))/(Ks1+Ks0-(Ks0)^2/(Ks2+Ks0));
        i=i+1;
    end
    
    plot(-40:0.1:40,Tw1);
        xlabel('T zew');
    ylabel('Tw1');
    hold on
end

figure;
%Q jako zmienna
for TzewN=-30:10:10
    %figure;
    
    i=1
    for QgN=-40000:100:40000
   
        Tw1(i)=(QgN+Ks1*TzewN+(Ks0*Ks2*TzewN)/(Ks2+Ks0))/(Ks1+Ks0-(Ks0)^2/(Ks2+Ks0));
        i=i+1;
    end
    
    plot(-40:0.1:40,Tw1);
    xlabel('Qg');
    ylabel('Tw1');
    hold on
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     Tw2      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
%TzewN jako zmienna
for QgN=15000:5000:25000
    %figure;
    
    i=1
    for TzewN=-40:0.1:40
   
        Tw2(i)=(QgN*Ks0+Ks1*Ks2*TzewN+Ks1*Ks0*TzewN+Ks0*Ks2*TzewN)/(Ks1*Ks2+Ks1*Ks0+Ks0*Ks2);
        i=i+1;
    end
    
    plot(-40:0.1:40,Tw2);
    xlabel('T zew');
    ylabel('Tw2');
    hold on
end


figure;
%Q jako zmienna
for TzewN=-30:10:10
    
    
    i=1
    for QgN=-40000:100:40000
   
        Tw2(i)=(QgN*Ks0+Ks1*Ks2*TzewN+Ks1*Ks0*TzewN+Ks0*Ks2*TzewN)/(Ks1*Ks2+Ks1*Ks0+Ks0*Ks2);
        i=i+1;
    end
    
    plot(-40:0.1:40,Tw2);
    xlabel('Qg');
    ylabel('Tw2');
    hold on
end

