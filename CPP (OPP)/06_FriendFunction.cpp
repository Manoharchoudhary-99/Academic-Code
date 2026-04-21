#include <iostream>
using namespace std;

class Sample
{
private:
    int a, b;

public:
    Sample(int x, int y)
    {
        a = x;
        b = y;
    }

    friend void showData(Sample s);
};

void showData(Sample s)
{
    cout << "Value of a = " << s.a << endl;
    cout << "Value of b = " << s.b << endl;
    cout << "Sum = " << (s.a + s.b) << endl;
}

int main()
{
    Sample obj(10, 20);
    showData(obj);
    return 0;
}