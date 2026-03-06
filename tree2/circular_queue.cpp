#include <iostream>
using namespace std;

class circularqueue
{
private:
    int front = -1;
    int rear = -1;
    int q[100];
    int max = 100;

public:
    void enqueue(int data)
    {
        if (isfull())
        {
            return;
        }

        if (front == -1 && rear == -1)
        {
            front = 0;
            rear = 0;

            q[rear] = data;
        }
        else
        {
            rear = (rear + 1) % max;
            q[rear] = data;
        }
    }
    int isfull()
    {
        if ((rear + 1) % max == front)
        {
            return 1;
        }
        return 0;
    }
    int isempty()
    {
        if (front == -1)
        {
            return 1;
        }
        return 0;
    }
    void deque()
    {
        if (isempty())
        {
            return;
        }
        cout << q[front] << endl;

        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {

            front = (front + 1) % max;
        }
    }
};