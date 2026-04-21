#include <iostream>
using namespace std;

class A
{
public:
    int x;

    A(int i)
    {
        x = i;
    }

    A operator+(A obj)
    {
        return A(x + obj.x);
    }

    void show()
    {
        cout << "Value = " << x;
    }
};

int main()
{
    A a1(5), a2(10);
    A a3 = a1 + a2;

    a3.show();

    return 0;
}