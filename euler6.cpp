// euler6.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
using namespace std;

int main()
{
	int sum = 0;
	int squareSum;
	int enter = 100;
	int sumSquare = 0;
	for (int i = 0; i < (enter + 1); i++)
	{
		sum = sum + i;
		sumSquare = sumSquare + i * i;
	}
	squareSum = sum * sum;
	cout << "squareSum: " << squareSum << endl;
	cout << "SumSquare: " << sumSquare << endl;
	cout << "SumSqaure - sqaureSum = " << squareSum - sumSquare;
	return 0;
}
