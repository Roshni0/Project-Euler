#include "pch.h"
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{

	int triangle[15][15];
	int a, b = 0;

	ifstream datafile;
	datafile.open("sheet.txt");


	for (a = 0; a < 15; a++)
	{
		for (b = 0; b - a < 1; b++)
		{
			datafile >> triangle[a][b];
		}
	}

	datafle.close();

	for (int c = 15; c >= 2; c--)
	{
		for (int d = 0; d < 14; d++)
		{
			triangle[c - 2][d] += max(triangle[c - 1][d], triangle[c - 1][d + 1]);
		}
	}

	return 0;
}
