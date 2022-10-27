#include <iostream>

using namespace std;

int kvadrat(int a){
    cout << "int ";
    return a*a;
}

double kvadrat(double a){
    cout << "double ";
    return a*a;
}

int main(void){
    cout << kvadrat(2) << " "
      << kvadrat(2.) << " " << kvadrat('A') << endl;

    return 0;
}