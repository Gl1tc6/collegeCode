#include <iostream>

using namespace std;

namespace s1 {
    float const pi = 3.14;
}

namespace s2 {
    double const pi = 3.141592654;
}

int main(void)
{
    //cout << s1::pi << endl;
    //cout << s2::pi << endl;
    // Sa posebno definiranim prostorom imena

    using namespace s2;

    cout << pi << endl;


    return 0;
}
