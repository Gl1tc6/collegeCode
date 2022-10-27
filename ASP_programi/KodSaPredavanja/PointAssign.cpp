#include <iostream>
using namespace std;

class Point {
    public:
        double x;
        double y;

        void mirrorX(double xValue) { x = 2*xValue - x ;}
        void mirrorY(double yValue) { y = 2*yValue - y ;}

    //Point(int _x, int _y) : x(_x), y(_y) {};

};

int main(void){
    Point p, r, s;
    cout << p.x << " " << p.y << endl;
    p.x = 10; p.y = 20;
    r = p;
    cout << r.x << " " << r.y << endl;
    memcpy(&s, &p, sizeof(p));
    cout << s.x << " " << s.y << endl;
    
    return 0;
}