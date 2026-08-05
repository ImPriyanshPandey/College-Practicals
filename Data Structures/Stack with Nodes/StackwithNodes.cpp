#include<iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int value) {
        data=value;
        next=nullptr;
    }
};
class Stack {
private:
    Node* top;
public:
    Stack() {
        top=nullptr;
    }

    ~Stack() {
        while(top!=nullptr) {
            Node*temp=top;
            top=top->next;
            delete temp;
        }
    }
    bool isEmpty() {
        return top==nullptr;
    }

    void push(int value) {
        Node* newNode=new Node(value);
        newNode->next=top;
        top=newNode;
        std::cout<<"Pushed Element: "<<value<<std::endl;
    }
    void pop() {
        if(isEmpty()) {
            std::cout<<"Stack Underflow! Can't Pop elements"<<std::endl;
            return;
        }
        int poppedElement=top->data;
        Node* temp=top;
        top=top->next;
        delete temp;
        std::cout<<"Popped Element"<<poppedElement<<std::endl;
    }

    int getTop() {
        if(isEmpty()) {
                std::cout<<"Stack is Empty."<<std::endl;
                return -1;
        }
        return top->data;
    }
};

int main() 
{
    Stack stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);

    std::cout<<"Top Element: "<<stack.getTop()<<std::endl;

    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();

    return 0;
}