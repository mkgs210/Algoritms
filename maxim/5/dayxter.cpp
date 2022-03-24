#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define SIZE 1000
int main()
{
    int a[SIZE][SIZE]; // матрица связей
    int d[SIZE]; // минимальное расстояние
    int v[SIZE]; // посещенные вершины
    int temp, minindex, min;
    int begin_index = 0;
    // Инициализация матрицы связей
    for (int i = 0; i < n; i++)
    {
        a[i][i] = 0;
        for (int j = i + 1; j < n; j++) {
            printf("Введите расстояние %d - %d: ", i + 1, j + 1);
            scanf("%d", &temp);
            a[i][j] = temp;
            a[j][i] = temp;
        }
    }
    // Вывод матрицы связей
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%5d ", a[i][j]);
        printf("\n");
    }
    //Инициализация вершин и расстояний
    for (int i = 0; i < n; i++)
    {
        d[i] = 10000;
        v[i] = 1;
    }
    d[begin_index] = 0;
    // Шаг алгоритма
    do {
        minindex = 10000;
        min = 10000;
        for (int i = 0; i < n; i++)
        { // Если вершину ещё не обошли и вес меньше min
            if ((v[i] == 1) && (d[i] < min))
            { // Переприсваиваем значения
                min = d[i];
                minindex = i;
            }
        }
        // Добавляем найденный минимальный вес
        // к текущему весу вершины
        // и сравниваем с текущим минимальным весом вершины
        if (minindex != 10000)
        {
            for (int i = 0; i < n; i++)
            {
                if (a[minindex][i] > 0)
                {
                    temp = min + a[minindex][i];
                    if (temp < d[i])
                    {
                        d[i] = temp;
                    }
                }
            }
            v[minindex] = 0;
        }
    } while (minindex < 10000);
    // Вывод кратчайших расстояний до вершин
    printf("\nКратчайшие расстояния до вершин: \n");
    for (int i = 0; i < n; i++)
        printf("%5d ", d[i]);

    // Восстановление пути
    int ver[SIZE]; // массив посещенных вершин
    int end = 4; // индекс конечной вершины = 5 - 1
    ver[0] = end + 1; // начальный элемент - конечная вершина
    int k = 1; // индекс предыдущей вершины
    int weight = d[end]; // вес конечной вершины

    while (end != begin_index) // пока не дошли до начальной вершины
    {
        for (int i = 0; i < n; i++) // просматриваем все вершины
            if (a[i][end] != 0)   // если связь есть
            {
                int temp = weight - a[i][end]; // определяем вес пути из предыдущей вершины
                if (temp == d[i]) // если вес совпал с рассчитанным
                {                 // значит из этой вершины и был переход
                    weight = temp; // сохраняем новый вес
                    end = i;       // сохраняем предыдущую вершину
                    ver[k] = i + 1; // и записываем ее в массив
                    k++;
                }
            }
    }
    // Вывод пути (начальная вершина оказалась в конце массива из k элементов)
    printf("\nВывод кратчайшего пути\n");
    for (int i = k - 1; i >= 0; i--)
        printf("%3d ", ver[i]);
    getchar(); getchar();
    return 0;
}