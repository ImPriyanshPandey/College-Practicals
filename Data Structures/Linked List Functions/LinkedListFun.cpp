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
class LinkedList {
    private:
        Node* head;
    public:
        LinkedList() {
            head=nullptr;
        }

        void insertatstart(int value) {
            Node* newNode=new Node(value);
            newNode->next=head;
            head=newNode;
        }

        void insertatend(int value) {
            Node* newNode=new Node(value);

            if(head==nullptr) {
                head=newNode;
                return;
            }
            Node*temp=head;
            while(temp->next!=nullptr) {
                temp=temp->next;
            }
            temp->next=newNode;
        }
        void display() {
            Node*temp=head;
            while(temp!=nullptr) {
                std::cout<<temp->data<<" ";
                temp=temp->next;
            }
            std::cout<<std::endl;
        }
};

int main() 
{
    LinkedList myList;

    myList.insertatend(5);
    myList.insertatend(11);
    myList.insertatstart(2);
    myList.insertatend(19);

    myList.display();
return 0;
}