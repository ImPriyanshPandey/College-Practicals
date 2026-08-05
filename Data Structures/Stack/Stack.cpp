#include<iostream>

class Stack {
private:
    int* arr;
    int capacity;
    int top;

public:
    Stack(int size) {
        capacity=size;
        arr=new int(capacity);
        top=-1;
    }
    ~Stack() {
        delete[] arr;
    }

    bool isEmpty() {
        return top==-1;
    }

    bool isFull() {
        return top == capacity -1;
    }

    void push(int value) {
        if (isFull()) {
            std::cout<<"Stack Overflow! Can't push."<<value<<std::endl;
            return;
        }
        arr[++top]=value;
        std::cout<<"Pushed Element"<<value<<std::endl;
    }
    void pop() {
        if(isEmpty()) {
            std::cout<<"Stack Underflow! Can't pop."<<std::endl;
            return;
        }
        int poppedElement=arr[top--];
        std::cout<<"Popped Element"<<poppedElement<<std::endl;
        }
        int getTop() {
            if(isEmpty()) {
                std::cout<<"Stack is Empty."<<std::endl;
                return -1;
            }
            return arr[top];
        }
    };

int main() 
{
    Stack stack(5);

    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);
    stack.push(60);

    std::cout<<"Top Element: "<<stack.getTop()<<std::endl;

    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();

    return 0;
}