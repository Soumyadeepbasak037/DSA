#include <iostream>
using namespace std;

class stack
{
private:
    int top = -1;
    int stck[100];
    int max = 100;

public:
    void insert(int data)
    {
        if (top == -1)
        {
            top = 0;
            stck[top] = data;
        }
        else
        {
            top = top + 1;
            stck[top] = data;
        }
    }

    void pop()
    {
        if (top == -1)
        {
            cout << "Empty";
            return;
        }
        // cout << "Top at:" << top << endl;
        cout << "Element:" << stck[top];
        top = top - 1;
    }
    void print()
    {
        for (int i = 0; i <= top; i++)
        {
            cout << stck[i] << " ";
        }
        cout << endl;
    }
};

int main()
{
    stack stk;
    stk.insert(6);
    stk.insert(5);
    stk.insert(34);
    stk.insert(43);

    stk.print();
    stk.pop();
    stk.pop();
    stk.pop();
    stk.pop();
    stk.pop();

    cout << endl;
    stk.print();
}