#include <iostream>
using namespace std;

class Patient
{
private:
    int patientId;
    string patientName;
    float billAmount;
    string appointmentDate;

public:
    Patient()
    {
        patientId = 0;
        patientName = "Not Assigned";
        billAmount = 0.0;
        appointmentDate = "Not Fixed";
    }

    Patient(int id, string name, float bill, string date)
    {
        patientId = id;
        patientName = name;
        billAmount = bill;
        appointmentDate = date;
    }

    Patient(Patient &p)
    {
        patientId = p.patientId;
        patientName = p.patientName;
        billAmount = p.billAmount;
        appointmentDate = p.appointmentDate;
    }

    void display()
    {
        cout << "\nPatient ID : " << patientId;
        cout << "\nPatient Name : " << patientName;
        cout << "\nBilling Amount : Rs. " << billAmount;
        cout << "\nAppointment Date : " << appointmentDate;
        cout << endl;
    }
};

int main()
{
    Patient p1;
    cout << "\n--- Default Constructor ---";
    p1.display();

    Patient p2(101, "Rahul Patil", 3500.50, "15-02-2026");
    cout << "\n--- Parameterized Constructor ---";
    p2.display();

    Patient p3 = p2;
    cout << "\n--- Copy Constructor ---";
    p3.display();

    return 0;
}