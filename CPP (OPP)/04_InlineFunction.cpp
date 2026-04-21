#include <iostream>
using namespace std;

class Calculator
{
private:
    float a, b;

public:
    void getData(float x, float y)
    {
        a = x;
        b = y;
    }

    inline float add() { return a + b; }
    inline float subtract() { return a - b; }
    inline float multiply() { return a * b; }
    inline float divide() { return a / b; }
};

int main()
{
    Calculator calc;
    float x, y;

    cout << "Enter two numbers: ";
    cin >> x >> y;

    calc.getData(x, y);

    cout << "\nAddition = " << calc.add();
    cout << "\nSubtraction  = " << calc.subtract();
    cout << "\nMultiplication = " << calc.multiply();
    cout << "\nDivision = " << calc.divide();

    return 0;
}