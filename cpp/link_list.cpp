#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* address;
};

class LinkedList {
public:
    Node* top;

    LinkedList() {
        top = NULL;
    }

    void push(int val) {
        Node* newNode = new Node();
        newNode->data = val;
        newNode->address = top;
        top = newNode;
    }

    int pop() {
        if (top == NULL) {
            cout << "List is empty" << endl;
            return -9999999;
        }
        int val = top->data;
        Node* temp = top;
        top = top->address;
        delete temp;
        return val;
    }

    void printList() {
        Node* temp = top;
        while (temp != NULL) {
            cout << temp->data << endl;
            temp = temp->address;
        }
        cout << endl;
    }
};

int main() {
    LinkedList myList;
    
    while (true)
    {
        cout << "------------------\n";
        cout << "Options:\n1. Push item \n2. Pop item \n3. Show list \n\n";
        cout << "------------------\n";
        int user_in;
        cout << "Enter option: \n";
        cin >> user_in;
        cout << endl;

        switch (user_in)
        {
        case 1:{
            cout << "Enter data to push:  \n";
            cin >> user_in;
            myList.push(user_in);
            cout << endl;
            }
            break;
        case 2:{
            int popitem = myList.pop();
            if (popitem == -9999999)
                cout << "Error: Empty linked list. Nothing to pop.\n";
            else
                cout << "Popped value: " << popitem << endl;
            }
            break;
        case 3:
            myList.printList();
            break;
        
        default:
            cout << "Error: Enter a valid integer!" << endl;
            break;
        }
    }

    return 0;
}
