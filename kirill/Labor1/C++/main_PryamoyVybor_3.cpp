#include <iostream>
#include <ctime>
#include <chrono>
#include <fstream>
using namespace std;


void DirectSelectionSort(int *massiv, int size){
    int min, temp;
    for (int i = 0; i < size - 1; i++){
        min = i;
        for (int j = i + 1; j < size; j++){
            if (massiv[j] < massiv[min])
            min = j;
        }
        temp = massiv[i];
        massiv[i] = massiv[min];
        massiv[min] = temp;
    }
}


int main()
{

    setlocale(LC_ALL,"Rus");
    double start_time, end_time, search_time;
    int size, i, j;
    int *massiv;
    int x[500];
    double y[500];
    srand(time(NULL));


    j=0;
    for (i=10;i<5001;i+=10){
        size=i;
        massiv=new int [size];

        for (i=0; i<size; i++){
            massiv[i]=rand()%201;
        }
        /*
        cout<<"�� ��������������� ������"<<endl;
        for (i=0; i<size; i++){
            cout<<massiv[i]<<" ";
        }
        cout<<endl;
        */

        //start_time =  getCPUTime( ); // ��������� �����
        //BubbleSort(massiv, size);
        //end_time = getCPUTime( ); // �������� �����
        //search_time = end_time - start_time; // ������� �����

        auto begin = std::chrono::steady_clock::now();
        DirectSelectionSort(massiv, size);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
        y[j]=elapsed_ms.count()/1000000000.0;
        j++;

        /*
        cout<<"��������������� ������"<<endl;
        for (i=0; i<size; i++){
            cout<<massiv[i]<<" ";
        }
        cout<<endl;
        */

        delete[] massiv;
        //cout<<endl;
    }


    for (i=0;i<501;i++){
        x[i]=i;
        cout<<x[i]<<" ";

    }

    cout<<endl<<endl;

    for (i=0;i<501;i++){
        cout<<y[i]<<" ";

    }

    //������ � ����
    fstream fs;
    fs.open("direct.txt", fstream::in | fstream::out| fstream::app);


    for(i=0; i<501; i++)    // ��� ���
        fs << y[i] << " ";


    fs.close();

    return 0;
}

