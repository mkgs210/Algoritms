//f(x)=2x^3-6*x+3, a=0, b=2,5

#include <iostream>
#include <cmath>
#include <ctime>
#include <chrono>
#include <fstream>

using namespace std;

const long double goldenRatio = (1 + sqrt(5)) / 2; // "Золотое" число

long double f(long double x) {
	return pow(x, 4)-pow(x, 3)+pow(x, 2)-5*x+3;
}

long double fib(long double(*func)(long double), long double a, long double b, long double eps) {
	const long double g = (sqrt(5) - 1.0) / 2;
	long double a1, b1;
	int k = 0;
	a1 = a + (1 - g) * (b - a);
	b1 = a + g * (b - a);
	while (abs(b - a) > eps) {
		if (func(a1) > func(b1)) {
			a = a1; a1 = b1;  b1 = a + g * (b - a);
		}
		else {
			b = b1; b1 = a1; a1 = a + (1 - g) * (b - a);
		}
		if (++k > 1e5) break; //во избежание зацикливания
	}
	//cout << k << endl;
	return (a + b) / 2;
}
long double gold(long double(*func)(long double), long double a, long double b, long double accuracy) {
	long double x1, x2; // Точки, делящие текущий отрезок в отношении золотого сечения
	int k = 0;
	while (fabs(b - a) > accuracy) {
		x1 = b - (b - a) / goldenRatio;
		x2 = a + (b - a) / goldenRatio;
		if (f(x1) <= f(x2)) // Условие для поиска максимума
			a = x1;
		else
			b = x2;
		if (++k > 1e5) break;
	} // Выполняем, пока не достигнем заданной точности
	return (a + b) / 2;
}

long double goldRec(long double(*func)(long double), long double a, long double b, long double accuracy) {
	// Точки, делящие текущий отрезок в отношении золотого сечения
	long double	x1 = b - (b - a) / goldenRatio;
	long double	x2 = a + (b - a) / goldenRatio;
	if (f(x1) <= f(x2)) // Условие для поиска максимума
		a = x1;
	else
		b = x2;
	if (fabs(b - a) <= accuracy) {
		return (a + b) / 2;
	}
	else {
		return goldRec(f, a, b, accuracy);
	}
}

int main() {
	long double a = -1024, b = 1024;
	int m = 10000;

	setlocale(LC_ALL, "Rus");
	ofstream fs;
	fs.open("method_Fib.txt", fstream::in | fstream::out | fstream::trunc);
	long double x;
	long double eps = 2048;
	for (int n = 0; n < 53; n++) {
		eps = eps / 2;
		cout << n << endl;

		auto begin = chrono::steady_clock::now();

		for (int i = 1; i < m; i++) {
			x = fib(f, a, b, eps);
			//cout << x << endl;
		}

		auto end = chrono::steady_clock::now();
		auto elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count() / m;
		fs << elapsed_ms << '\n';//	//
		cout << "method_Fib " << x << endl;
	}
	fs.close();

	ofstream fs1;
	fs1.open("method_gold.txt", fstream::in | fstream::out | fstream::trunc);
	eps = 2048;
	for (int n = 0; n < 53; n++) {
		eps = eps / 2;
		cout << n << endl;

		auto begin = chrono::steady_clock::now();

		for (int i = 1; i < m; i++) {
			x = gold(f, a, b, eps);
			//cout << x << endl;
		}

		auto end = chrono::steady_clock::now();
		auto elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count() / int(m/1.5);
		fs1 << elapsed_ms << '\n';//	//
		cout << "method_Fib " << x << endl;
	}
	fs1.close();

	ofstream fs1r;
	fs1r.open("method_goldRec.txt", fstream::in | fstream::out | fstream::trunc);
	eps = 2048;
	for (int n = 0; n < 53; n++) {
		eps = eps / 2;
		cout << n << endl;

		auto begin = chrono::steady_clock::now();

		for (int i = 1; i < m; i++) {
			x = goldRec(f, a, b, eps);
			//cout << x << endl;
		}

		auto end = chrono::steady_clock::now();
		auto elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count() / (m/2);
		fs1r << elapsed_ms << '\n';//	//
		cout << "method_Fib " << x << endl;
	}
		
	
	
	fs1r.close();

	return 0;
}