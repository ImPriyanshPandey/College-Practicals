#include<iostream>

#define MAX_SIZE 100

class Queue {
private:
    int arr[MAX_SIZE];
    int front;
    int rear;

public:
    Queue() {
        front=-1;
        rear=-1;
    }
    bool isEmpty() {
        return front==-1 && rear==-1;
    }
    bool isFull() {
        return rear==MAX_SIZE-1;
    }

    void enqueue(int item) {
        if(isFull()) {
            std::cout<<"Queue is Full. Can't enqueue."<<std::endl;
            return;
        }
        else if(isEmpty()) {
            front=rear=0;
        }
        else {
            rear++;
        }
        arr[rear]=item;
    }
    int dequeue() {
        if(isEmpty()) {
                std::cout<<"Queue is empty. Can't dequeue."<<std::endl;
                return -1;
        }
        int item=arr[front];
        if(front==rear) {
            front=rear=-1;
        }
        else {
            front++;
        }
        return item;
    }
    int getFront() {
        if(isEmpty()) {
                std::cout<<"Queue is empty."<<std::endl;
                return -1;
        }
        return arr[front];
    }
    int getSize() {
        if(isEmpty()) {
            return 0;
        }
        return rear-front+1;
    }
};

int main() 
{
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    std::cout<<"Size: "<<q.getSize()<<std::endl;
    std::cout<<"Front: "<<q.getFront()<<std::endl;

    std::cout<<q.dequeue()<<std::endl;
    std::cout<<q.dequeue()<<std::endl;

    std::cout<<"Size: "<<q.getSize()<<std::endl;

    return 0;
}