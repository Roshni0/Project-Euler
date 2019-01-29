#include "pch.h"
#include < iostream >
#include < string >
#include < math.h >

using namespace std;

int main() {
	double powerValue = pow(2, 1000);
	string powerString = to_string(powerValue);
	int digitSum = 0, currentDigit = 0;
	while (powerString[currentDigit] != '.') {
		digitSum += powerString[currentDigit] - '0';
		currentDigit++;
	}
	cout << digitSum;
}