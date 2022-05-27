#include <iostream>
#include <fstream>
#include <chrono>
using namespace std;
const int maxV = 1000;
int i, j;
int GR[maxV][maxV];
//алгоритм Флойда-Уоршелла
void FU(int D[][maxV], int V)
{
	int k;
	for (i = 0; i < V; i++) D[i][i] = 0;

	for (k = 0; k < V; k++)
		for (i = 0; i < V; i++)
			for (j = 0; j < V; j++)
				if (D[i][k] && D[k][j] && i != j)
					if (D[i][k] + D[k][j] < D[i][j] || D[i][j] == 0)
						D[i][j] = D[i][k] + D[k][j];

	/*for (i = 0; i < V; i++)
	{
		for (j = 0; j < V; j++) cout << D[i][j] << "\t";
		cout << endl;
	}*/
}

int d[maxV]; // минимальное расстояние
int v[maxV]; // посещенные вершины
int temp, mini, minindex;
int begin_index = 0;

void dexter(int a[][maxV], int n) {
    

    for (int i = 0; i < n; i++)
    {
        d[i] = 10000;
        v[i] = 1;
    }
    d[begin_index] = 0;
    // Шаг алгоритма
    do {
        mini = 10000;
        minindex = 10000;
        for (int i = 0; i < n; i++){ // Если вершину ещё не обошли и вес меньше min
            if ((v[i] == 1) && (d[i] < mini)){ // Переприсваиваем значения
                mini = d[i];
                minindex = i;
            }
        }
        // Добавляем найденный минимальный вес
        // к текущему весу вершины
        // и сравниваем с текущим минимальным весом вершины
        if (minindex != 10000){
            for (int i = 0; i < n; i++){
                if (a[minindex][i] > 0){
                    temp = mini + a[minindex][i];
                    if (temp < d[i]){
                        d[i] = temp;
                    }
                }
            }
            v[minindex] = 0;
        }
    } 
    while (minindex < 10000);
    /*// Вывод кратчайших расстояний до вершин
    printf("\nКратчайшие расстояния до вершин: \n");
    for (int i = 0; i < n; i++)
        printf("%5d ", d[i]);*/
}
//главная функция
void main()
{
	setlocale(LC_ALL, "Rus");
    int m = 30000;

	ofstream fs; ofstream fs1;
	fs.open("Floid.txt", fstream::in | fstream::out | fstream::trunc);
    fs1.open("Dexter.txt", fstream::in | fstream::out | fstream::trunc);
	for (int n = 2; n < 52; n++) {
		cout << n << endl;
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
            {
                GR[i][j] = rand() % 100;
            }
        cout << "Floid" << endl;
		auto begin = chrono::steady_clock::now();
		/*for (int i = 0; i < m; i++) {
            FU(GR, n);
		}*/
		auto end = chrono::steady_clock::now();
		auto elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count() / m;
		//fs << elapsed_ms << '\n';//	//

        cout << "Dexter" << endl;
        begin = chrono::steady_clock::now();
        for (int i = 0; i < m; i++) {
            dexter(GR, n);
        }
        end = chrono::steady_clock::now();
        elapsed_ms = chrono::duration_cast<chrono::nanoseconds>(end - begin).count() / m;
        fs1 << elapsed_ms << '\n';//	//
	}
	fs.close();
    fs1.close();

}