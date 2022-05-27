#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define SIZE 1000
int main()
{
    int a[SIZE][SIZE]; // ������� ������
    int d[SIZE]; // ����������� ����������
    int v[SIZE]; // ���������� �������
    int temp, minindex, min;
    int begin_index = 0;
    // ������������� ������� ������
    for (int i = 0; i < n; i++)
    {
        a[i][i] = 0;
        for (int j = i + 1; j < n; j++) {
            printf("������� ���������� %d - %d: ", i + 1, j + 1);
            scanf("%d", &temp);
            a[i][j] = temp;
            a[j][i] = temp;
        }
    }
    // ����� ������� ������
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%5d ", a[i][j]);
        printf("\n");
    }
    //������������� ������ � ����������
    for (int i = 0; i < n; i++)
    {
        d[i] = 10000;
        v[i] = 1;
    }
    d[begin_index] = 0;
    // ��� ���������
    do {
        minindex = 10000;
        min = 10000;
        for (int i = 0; i < n; i++)
        { // ���� ������� ��� �� ������ � ��� ������ min
            if ((v[i] == 1) && (d[i] < min))
            { // ��������������� ��������
                min = d[i];
                minindex = i;
            }
        }
        // ��������� ��������� ����������� ���
        // � �������� ���� �������
        // � ���������� � ������� ����������� ����� �������
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
    // ����� ���������� ���������� �� ������
    printf("\n���������� ���������� �� ������: \n");
    for (int i = 0; i < n; i++)
        printf("%5d ", d[i]);

    // �������������� ����
    int ver[SIZE]; // ������ ���������� ������
    int end = 4; // ������ �������� ������� = 5 - 1
    ver[0] = end + 1; // ��������� ������� - �������� �������
    int k = 1; // ������ ���������� �������
    int weight = d[end]; // ��� �������� �������

    while (end != begin_index) // ���� �� ����� �� ��������� �������
    {
        for (int i = 0; i < n; i++) // ������������� ��� �������
            if (a[i][end] != 0)   // ���� ����� ����
            {
                int temp = weight - a[i][end]; // ���������� ��� ���� �� ���������� �������
                if (temp == d[i]) // ���� ��� ������ � ������������
                {                 // ������ �� ���� ������� � ��� �������
                    weight = temp; // ��������� ����� ���
                    end = i;       // ��������� ���������� �������
                    ver[k] = i + 1; // � ���������� �� � ������
                    k++;
                }
            }
    }
    // ����� ���� (��������� ������� ��������� � ����� ������� �� k ���������)
    printf("\n����� ����������� ����\n");
    for (int i = k - 1; i >= 0; i--)
        printf("%3d ", ver[i]);
    getchar(); getchar();
    return 0;
}