#include <iostream>
using namespace std;
class CircularQueue
{
private:
    int *queue;
    int size;
    int front;
    int rear;

public:
    CircularQueue(int s)
    {
        size = s;
        queue = new int[size];
        front = -1;
        rear = -1;
    }
    ~CircularQueue()
    {
        delete[] queue;
    }
    bool isFull()
    {
        if ((rear + 1) % size == front)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool isEmpty()
    {
        if (front == rear)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    bool enqueue(int item)
    {
        if (isFull())
        {
            cout << "Stack overflow attempted";
        }
        if (isEmpty())
        {
            front = 0;
        }
    }
};

int main()
{
}