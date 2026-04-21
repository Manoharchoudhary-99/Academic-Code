#include <iostream>
using namespace std;

class Base
{
public:
    virtual void display()
    {
        cout << "Base class display\n";
    }
};

class Derived : public Base
{
public:
    void display()
    {
        cout << "Derived class display\n";
    }
};

int main()
{
    Base *b;
    Derived d;

    b = &d;
    b->display();

    return 0;
}