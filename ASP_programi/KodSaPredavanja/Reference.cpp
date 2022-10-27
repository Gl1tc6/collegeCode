#include <iostream>

using namespace std;

int main(void){
    int a = 1;
    int &b = a;

    // slično kao int *b = &a;
    // ali bi kasnije trebalo eksplicitno dereferencirati

    b = 8;

    cout << a << " " << b;

    return 0;
}