#include <iostream>

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

int main()
{
    int n = 5;
    std::cout << iterativeFact(n) << std::endl;
    std::cout << recursiveFact(n) << std::endl;
    std::cout << iterativeFib(n) << std::endl;
    std::cout << recursiveFib(n) << std::endl;
}