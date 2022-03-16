
#include <iostream>
#include <ctime>
#include <chrono>
#include <fstream>
using namespace std;


void BubbleSort(int *massiv, int size)
{
  int temp;
  for (int i = 1; i < size; i++)
  {
    for (int j = 0; j < size-1; j++)
    {
      if (massiv[j] > massiv[j+1])
      {
        temp = massiv[j];
        massiv[j] = massiv[j+1];
        massiv[j+1] = temp;
      }
    }
  }
}

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
    int size, i, j, colvo;
    int *massiv;
    int x[500];
    double y1[20],y2[20],y3[20];



    for (i=0;i<20;i++){
        y1[i]=0;
        y2[i]=0;
        y3[i]=0;

    }
    j=0;
    for (i=100;i<2001;i+=100){
        srand(time(NULL));
        size=i;
        massiv=new int [size];


        /*
        cout<<"Не отсортированный массив"<<endl;
        for (i=0; i<size; i++){
            cout<<massiv[i]<<" ";
        }
        cout<<endl;


        for (i=0; i<size; i++){
            massiv[i]=rand()%201;
        }
        */

        cout<<i<<endl;

        for (colvo=0;colvo<10000;colvo++){

            srand(time(NULL));

            for (i=0; i<size; i++){
                massiv[i]=rand()%201;
            }

            auto begin = std::chrono::steady_clock::now();
            BubbleSort(massiv, size);
            auto end = std::chrono::steady_clock::now();
            auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
            y1[j]+=(elapsed_ms.count()/1000000000.0)/10000.0;


            for (i=0; i<size; i++){
                massiv[i]=rand()%201;
            }

            begin = std::chrono::steady_clock::now();
            SelectionSort(massiv, size);
            end = std::chrono::steady_clock::now();
            elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
            y2[j]+=(elapsed_ms.count()/1000000000.0)/10000.0;


            for (i=0; i<size; i++){
                massiv[i]=rand()%201;
            }

            begin = std::chrono::steady_clock::now();
            DirectSelectionSort(massiv, size);
            end = std::chrono::steady_clock::now();
            elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
            y3[j]+=(elapsed_ms.count()/1000000000.0)/10000.0;

        }

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

    /*
    for (i=0;i<501;i++){
        x[i]=i;
        cout<<x[i]<<" ";

    }
    */

    cout<<endl<<endl;

    /*
    for (i=0;i<501;i++){
        cout<<y[i]<<" ";

    }
    */

    //Запись в файл
    fstream fs1;
    fstream fs2;
    fstream fs3;

    fs1.open("puzir.txt", fstream::in | fstream::out| fstream::app);
    fs2.open("selection.txt", fstream::in | fstream::out| fstream::app);
    fs3.open("direct.txt", fstream::in | fstream::out| fstream::app);


    for(i=0; i<20; i++){
        fs1 << y1[i] << " ";
        fs2 << y2[i] << " ";
        fs3 << y3[i] << " ";
    }



    fs1.close();
    fs2.close();
    fs3.close();

    return 0;
}

