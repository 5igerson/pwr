#include <stdio.h>
//#include <pch.h>
#include <iostream>
#define _CRT_SECURE_NO_WARNINGS


float A[100][100];
float L[100][100];
float D[100][100];
float U[100][100];
float b[100];
float x[100];

int n, iter;
int i, j, k;

int main()
{

	printf("Rozwiązanie układu równań liniowych Metoda Gaussa-Seidela\n");
	printf("Rozwiazywanie ukladu n-rownan z n-niewiadomymi Ax=b\n");
	printf("Podaj n\n");
	scanf("%d", &n);
	if ((n < 1) && (n > 100)) {
		printf("Nieprawidlowa warosc parametru n\n");
		return 0;
	}


	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			printf("A[%d][%d] = ", (i + 1), (j + 1));
			scanf("%f", &A[i][j]);
			if ((i == j) && (A[i][j] == 0)) {
				printf("Wartosci na przekatnej musza byc rozne od 0\n");
				return 0;
			}
		}


	for (i = 0; i < n; i++) {
		printf("b[%d] = ", (i + 1));
		scanf("%f", &b[i]);
	}


	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			if (i < j) {
				U[i][j] = A[i][j];
			}
			else if (i > j) {
				L[i][j] = A[i][j];
			}
			else {
				D[i][j] = A[i][j];
			}
		}


	for (i = 0; i < n; i++)
		D[i][i] = 1 / D[i][i];


	for (i = 0; i < n; i++)
		b[i] *= D[i][i];


	for (i = 0; i < n; i++)
		for (j = 0; j < i; j++)
			L[i][j] *= D[i][i];

            


	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
			U[i][j] *= D[i][i];


	for (i = 0; i < n; i++)
		x[i] = 0;

	printf("Ile iteracji algorytmu wykonac?\n");
	scanf("%d", &iter);

	for (k = 0; k < iter; k++)
		for (i = 0; i < n; i++) {
			x[i] = b[i];
			for (j = 0; j < i; j++)
				x[i] -= L[i][j] * x[j];
			for (j = i + 1; j < n; j++)
				x[i] -= U[i][j] * x[j];

			printf("Wynik\n");
			for (i = 0; i < n; i++)
				printf("x[%d] = %f\n", (i + 1), x[i]);

			return 0;

		}
}