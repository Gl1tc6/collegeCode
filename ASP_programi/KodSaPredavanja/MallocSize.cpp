#include <iostream>
using namespace std;

//int main(void){
    //int p[2000000] = {0};
    //int *p;
    //p = (int *)malloc(500000 * sizeof(int));

    //if(p){
       // p[0] = 5;
       //cout<<p[0]<<endl;
      // free(p);
    
    //}else{
      //  cout<<"Err. Mem. allocation!";
    //}

  //  return 0;
//}

int main(void){
    //int p[2000000] = {0};
    //int *p = new (nothrow) int[260000];
    //delete[] p;
    //p = (int *)malloc(500000 * sizeof(int));

    try
        {
            int *p = new int[2500000000];
            if(p){
                    p[0] = 0;
                    cout<<"p[0] = "<< p[0] <<endl;
                    delete[] p;
                
                }else{
                    cout<<"Err. Mem. allocation!";
                }
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
    

    return 0;
}