#include <iostream>
using namespace std;

class Shape
{
public:
    virtual void area() = 0;
    virtual void perimeter() = 0;
};

class Rectangle : public Shape
{
    float length, width;

public:
    void getData()
    {
        cin >> length >> width;
    }

    void area()
    {
        cout << length * width;
    }

    void perimeter()
    {
        cout << 2 * (length + width);
    }
};