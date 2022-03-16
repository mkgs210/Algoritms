#include <iostream>
#include <ctime>
#include <chrono>
#include <fstream>

int iterativeFact(int n) {
    int r = 1;
    int k = n;
    for(int i = 0; i <n; i++){
        r = r * k;
        k=k-1;
    }
    return r;
}

int recursiveFact(int n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * recursiveFact(n - 1);
    }
    
}

int iterativeFib(int n){
    if (n == 0) {
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    int r = 1;
    int k = 1;
    for (int i = 2; i < n; i++) {
        int p = r + k;
        r = k;
        k = p;
    }
    return k;
}

int recursiveFib(int n) {
    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else{
        return recursiveFib(n - 2) + recursiveFib(n - 1);
    }
}

int iterativeTrib(int n) {
    if (n == 0) {
        return 0;
    }
    else if (n == 1 or n ==2) {
        return 1;
    }
    int k0 = 0;
    int k1 = 1;
    int k2 = 1;
    for (int i = 2; i < n; i++) {
        int p = k0 + k1 + k2;
        k0 = k1;
        k1 = k2;
        k2 = p;
    }
    return k2;
}

int recursiveTrib(int n) {
    if (n == 0) {
        return 0;
    }
    else if ((n == 1) or (n==2)) {
        return 1;
    }
    else {
        return recursiveTrib(n - 1) + recursiveTrib(n - 2) + recursiveTrib(n - 3);
    }
}

int main()
{
    setlocale(LC_ALL, "Rus");
    double start_time, end_time, search_time;
    int n;
    int m = 100;
    
    std::fstream fs;
    /*fs.open("iterativeFact.txt", std::fstream::in | std::fstream::out | std::fstream::app);

    std::cout << "iterativeFact" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        iterativeFact(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count()/ 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
    fs.open("recursiveFact.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    std::cout << "recursiveFact" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        recursiveFact(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
    fs.open("iterativeFib.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    std::cout << "iterativeFib" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        iterativeFib(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
    fs.open("iterativeTrib.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    std::cout << "iterativeTrib" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        iterativeTrib(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
    */



    fs.open("recursiveFib.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    std::cout << "recursiveFib" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        recursiveFib(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
    fs.open("recursiveTrib.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    std::cout << "recursiveTrib" << std::endl;
    for (n = 0; n < m; n += 1) {
        auto begin = std::chrono::steady_clock::now();
        recursiveTrib(n);
        auto end = std::chrono::steady_clock::now();
        auto elapsed_ms = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0;;
        fs << elapsed_ms << ' ';
        std::cout << n << std::endl;
    }
    fs.close();
}