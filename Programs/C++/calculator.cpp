#include <iostream> 
using namespace std; 

int main() {
	float first;
	float second;
	string operation;
	
	cout << "Enter first number: ";
	cin >> first;
	cout << "Enter second number: ";
	cin >> second;
	cout << "Enter operation(+,-,*,/): ";
	cin >> operation;

	if (operation == "+") {
		cout << "Result: " << first + second;
	}

	else if (operation == "-") {
		cout << "Result: " << first - second;
	}

	else if (operation == "*") {
		cout << "Result: " << first * second;
	}

	else if (operation == "/") {
		cout << "Result: " << first / second;
	}

	else {
		cout << "Unknown operation!";
	}
}
