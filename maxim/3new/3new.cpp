//f(x)=2x^3-6*x+3, a=0, b=2,5

#include <iostream>
#include <cmath>
#include <ctime>
#include <chrono>
#include <fstream>

using namespace std;

const double goldenRatio = (1 + sqrt(5)) / 2; // "Золотое" число

double f(double x) {
	return pow(x, 4)-pow(x, 3)+pow(x, 2)-5*x+3;
}

double fib(double(*func)(double), double a, double b, double eps) {
	const double g = (sqrt(5) - 1.0) / 2;
	double a1, b1;
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
	return (a + b) / 2;
}
double gold(double(*func)(double), double a, double b, double accuracy) {
	double x1, x2; // Точки, делящие текущий отрезок в отношении золотого сечения
	while (fabs(b - a) > accuracy) {
		x1 = b - (b - a) / goldenRatio;
		x2 = a + (b - a) / goldenRatio;
		if (f(x1) <= f(x2)) // Условие для поиска максимума
			a = x1;
		else
			b = x2;
	} // Выполняем, пока не достигнем заданной точности
	return (a + b) / 2;
}
int main() {
	double a = 0.1, b = 1.5;
	int m = 20000;

	setlocale(LC_ALL, "Rus");
	ofstream fs;
	ofstream fs1;

	fs.open("method_Fib.txt", fstream::in | fstream::out | fstream::trunc);
	fs1.open("method_gold.txt", fstream::in | fstream::out | fstream::trunc);
	double x;
	double eps = 2;
	for (int  n = 0; n<53; n++) {
		eps = eps / 2;
		cout << "method_Fib" << endl;
		auto begin = chrono::steady_clock::now();

		for (int i = 1; i < m; i++) {
			x = fib(f, a, b, eps);
			//cout << x << endl;
		}

		auto end = chrono::steady_clock::now();
		auto elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count()/ m;
		fs << elapsed_ms << '\n';//	//
		cout << n << ' ' << endl;
		cout << "method_gold" << endl;
		begin = chrono::steady_clock::now();

		for (int i = 1; i < m; i++) {
			x = gold(f, a, b, eps);
			//cout << x << endl;
		}

		end = chrono::steady_clock::now();
		elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count()/ 10000;
		fs1 << elapsed_ms << '\n';//	//

		//cout.precision(7);
		//cout << n << ' ' << eps <<"\nx=" << fixed << x << ", f(x)=" << f(x) << "\n" <<endl;
		cout << n << ' ' << endl;
	}
	fs.close();
	fs1.close();

	return 0;
}