#include <iostream>
using namespace std;

void bblSort1(int arr[], int size){
    int temp = 0;
    for(int i = 0; i<size; i++){
        for(int j = 0; j < size - i; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main(void){
    int a[] = {5,23,4,1,15,2,13,8,19,11};
    int arrSize = sizeof(a)/sizeof(int);
    //int *pa = a;

    //cout << sizeof(int) << endl;

    for(int i = 0; i < arrSize; ++i){
        cout << a[i] << " ";
    }
    cout<< endl;

    bblSort1(a, arrSize);

    cout<< "\n\n\n" << endl;

    for(int i = 0; i < sizeof(a)/sizeof(int); ++i){
       cout << a[i] << " ";
    }
    cout<< endl;
    
    return 0;
}