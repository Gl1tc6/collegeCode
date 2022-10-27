#include <iostream>

using namespace std;

class Point {
    public:
        double x;
        double y;

        void mirrorX(double xValue) { x = 2*xValue - x ;}
        void mirrorY(double yValue) { y = 2*yValue - y ;}

    Point(int _x, int _y) : x(_x), y(_y) {};
    Point() { Point(0,0); };



};

int main(void){
    Point p;

    cout << sizeof(p) << endl;
    cout << p.x << " " << p.y << endl;
    Point p2 {10, 20};
    p2.mirrorX(-1);

    cout << p2.x << " " << p2.y << endl;

    return 0;
}