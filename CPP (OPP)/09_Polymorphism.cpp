#include <iostream>
using namespace std;

class Base
{
public:
    void show()
    {
        cout << "This is Base class function\n";
    }
};

class Derived : public Base
{
public:
    void show()
    {
        cout << "This is Derived class function\n";
    }
};

int main()
{
    Base *b;
    Derived d;

    b = &d;

    b->show();   // Compile time binding
    d.show();    // Derived function

    return 0;
}