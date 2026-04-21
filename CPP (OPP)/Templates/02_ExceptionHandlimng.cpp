#include <iostream>
using namespace std;

int main()
{
    int a, b;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    try
    {
        if (b == 0)
            throw b;

        cout << "Division = " << a / b;
    }
    catch (int x)
    {
        cout << "Error: Division by zero not allowed";
    }

    return 0;
}