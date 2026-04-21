#include <iostream>
#include <iomanip>
using namespace std;

class HotelBill
{
private:
    int tableNo, items;
    string customerName;
    long long contact;
    float total, discount, payable;

public:
    void getCustomerDetails()
    {
        cout << "Enter Table Number: ";
        cin >> tableNo;

        cin.ignore();

        cout << "Enter Customer Name: ";
        getline(cin, customerName);

        cout << "Enter Customer Contact Number: ";
        cin >> contact;
    }

    void getOrderDetails()
    {
        int qty;
        float price;
        total = 0;

        cout << "\nEnter Number of Items Ordered: ";
        cin >> items;

        for (int i = 1; i <= items; i++)
        {
            cout << "\nItem " << i << " Quantity: ";
            cin >> qty;

            cout << "Item " << i << " Price: ";
            cin >> price;

            total += qty * price;
        }
    }

    void calculateBill()
    {
        if (total >= 2000)
            discount = total * 0.20;
        else if (total >= 1000)
            discount = total * 0.10;
        else
            discount = 0;

        payable = total - discount;
    }

    void displayBill()
    {
        cout << "\n---------- HOTEL BILL ---------- \n";
        cout << "Table No : " << tableNo << endl;
        cout << "Customer Name : " << customerName << endl;
        cout << "Contact Number : " << contact << endl;

        cout << fixed << setprecision(2);
        cout << "Total Amount : Rs. " << total << endl;
        cout << "Discount : Rs. " << discount << endl;
        cout << "Payable Amount : Rs. " << payable << endl;
    }
};

int main()
{
    HotelBill bill;
    bill.getCustomerDetails();
    bill.getOrderDetails();
    bill.calculateBill();
    bill.displayBill();

    return 0;
}