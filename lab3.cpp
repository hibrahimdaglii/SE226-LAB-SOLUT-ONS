#include <iostream>
#define MAX 1000

using namespace std;
class Node{
public:
    int data;
    Node *next;
    Node(int x, Node *n){
    data=x;
    next=n;

    }
};
class Stack{
Node* top;
int count;
int size;

Stack(int size){
    top=nullptr;
    count=0;
    this->size=size;
 }
 void push(int data){
     if(size=MAX){
        cout<<"stack is full"<<endl;
     }
 else{
        if(top==nullptr){
            top=new Node(data, nullptr);
 size++

 }
 else{
    Node* temp= new Node(data,top);
    top=temp;
    size++;
 }

 }
 Node* pop(){
 if(top== nullptr){

    cout<<"no elements!"<<endl;
    return nullptr;
 }
 else{
    Node* temp = top;
    top->next = top;
    size--;
    return temp;
 }
 }
 int topOfStack(){
 if(top==nullptr){
    cout<<"no elements!"<<endl;
    return -1;

 }
 else{
    return top->data;
 }
 }
 bool isEmpty(){
 if(top==nullptr){
    return true;
 }
 else return false;
 }
 int sizeOfStack(){
 if(top== nullptr){
    cout<<"No element!"<<endl;
    return -1;

 }
 else{
    return size;
 }
 }
};

int main()
{
    Stack *s = new Stack(5);
    s->push(2);
    cout<< s->topOfStack();

    return 0;
};