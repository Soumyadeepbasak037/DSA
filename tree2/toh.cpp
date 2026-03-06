#include <iostream>
using namespace std;

void toh(int n, char s, char d, char a)
{
    if (n == 1)
    {
        cout << "Moving disk 1 from source to dest";
        return;
    }
    toh(n - 1, s, a, d);
    cout << endl;
    cout << "Moving disk " << n << " from source to dest" << endl;
    toh(n - 1, a, d, s);
}
int main()
{
    toh(5, 'A', 'C', 'B');
}

/*
sda
sad
ads
*/