#include <iostream>
using namespace std;

class queue
{

private:
    int front = -1;
    int rear = -1;
    int max = 100;
    int q[100];

public:
    void enqueue(int data)
    {
        if (rear == max - 1)
        {
            cout << "Q is full";
        }
        if (front == -1 && rear == -1)
        {
            front = 0;
            rear = 0;
            q[rear] = data;
        }
        else
        {
            rear = rear + 1;
            q[rear] = data;
        }
    }

    void dequeue()
    {
        if (front == -1 || front > rear)
        {
            cout << "empty";
            return;
        }
        else
        {
            cout << q[front];
            front++;
        }
    }

    void print()
    {
        if (front == -1 || front > rear)
        {
            cout << "Empty";
        }
        else
        {
            cout << q[front] << endl;
        }
    }
};

int main()
{
    queue q;
    q.enqueue(5);
    q.enqueue(10);
    q.enqueue(15);
    q.enqueue(20);

    q.dequeue();
    q.dequeue();
}