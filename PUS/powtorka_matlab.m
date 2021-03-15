%ogoline wprowadenie krotnie jest u niego na stronie


%zawsze chce zeby dawac na poczatku:
close all; 
clear all;
clc;
% i to poprosil zeby zawsze bylo na poczatku 

a=5;

%wektory powiedzial zeby dawac duzymi literami xD
Q=[1,2,3,4,5];
W=[8,9,7,5,4];

%transponowanie macierzy Q
Q';
%to umozliwi mnozenie
M=Q'*W;
K=Q*W';


%rozmiar macierzy
[wiersz,kolumna]=size(M);

%%%%RYSOWANIE WYKRESOW%%%%



plot(W,Q,'m*-','LineWidth',2);

%kilka wykresow na jednym oknie
hold on;
plot(Q,W,'r*-','LineWidth',2);

%siatka na wykresie
grid on;

xlabel('x');
ylabel('y');
title('Title');
legend('w1','w2');

%inny wykres niz 2d
%figure albo subplot
figure;
bar(Q,W);
xlabel('x');
ylabel('y');
title('Title');
grid on;