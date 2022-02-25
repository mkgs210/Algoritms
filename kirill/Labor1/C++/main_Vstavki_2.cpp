
#include <iostream>
#include <ctime>
#include <chrono>
#include <fstream>
using namespace std;


void SelectionSort(int *massiv, int size){
    int temp;
    int i,j;
    for (i = 0; i < size - 1; i++){
        temp=massiv[i];
        for (j = i-1; j>=0 && massiv[j]>temp; j--)
        {
            massiv[j+1] = massiv[j];
        }
        massiv[j+1] = temp;
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
        cout<<"Не отсортированный массив"<<endl;
        for (i=0; i<size; i++){
            cout<<massiv[i]<<" ";
        }
        cout<<endl;
        */

        //start_time =  getCPUTime( ); // начальное время
        //BubbleSort(massiv, size);
        //end_time = getCPUTime( ); // конечное время
        //search_time = end_time - start_time; // искомое время

        auto begin = std::chrono::steady_clock::now();
        SelectionSort(massiv, size);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
        y[j]=elapsed_ms.count()/1000000000.0;
        j++;

        /*
        cout<<"Отсортированный массив"<<endl;
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

    //Запись в файл
    fstream fs;
    fs.open("selection.txt", fstream::in | fstream::out| fstream::app);


    for(i=0; i<501; i++)    // или так
        fs << y[i] << " ";


    fs.close();

    return 0;
}

