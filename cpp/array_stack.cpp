#include<iostream>
#define maxsize 20
using namespace std;

class Stack
{
    int top;
    int a[maxsize];
public:
    Stack();
    bool isfull();
    bool isempty();
    void push(int x);
    void pop();
    void Top();
    void Size();
};

Stack::Stack()   
    {
        top=0;
    }

bool Stack::isfull()    
    {
        if(top==maxsize)
            return true;
        else
            return false;
    }

bool Stack::isempty()   
    {
        if(top==0)
            return true;
        else
            return false;
    }

void Stack::Size()   
{
    cout<<"Stack size = "<<top<<endl;
}

void Stack::push(int x)
{
    if(isfull())
    {
        cout<<"Stack is full"<<endl;
        return;
    }
    else
    a[top]=x;   
    top++;
}

void Stack::pop()
{
    if(isempty())
    {
        cout<<"Empty list!"<<endl;
        return;
    }
    else
        top--;   
        cout<<"pops "<<a[top]<<endl;
}

void Stack::Top()   // Displays the element on top
{
    cout<<"top is "<<a[top-1]<<endl;
}

int main()
{
    Stack s;
    int ch,element,result;
    cout<<"Enter an element (integer)"<<endl;
    cin>>element;
    s.push(element);
    s.pop();
    if(s.isfull())
            cout<<"Stack is full"<<endl;
        else
            cout<<"Stack is not full"<<endl;
    if(s.isempty())
            cout<<"Stack is empty"<<endl;
        else
            cout<<"Stack is not empty"<<endl;
    return 0;
}