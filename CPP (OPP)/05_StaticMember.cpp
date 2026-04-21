#include <iostream>
using namespace std;

class Student
{
private:
    static int count;

public:
    Student()
    {
        count++;
    }

    static void showCount()
    {
        cout << "Total number of students: " << count << endl;
    }
};

int Student::count = 0;

int main()
{
    Student s1, s2, s3;
    Student::showCount();
    return 0;
}