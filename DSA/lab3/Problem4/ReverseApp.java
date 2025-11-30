package Problem4;

import java.util.*;

class Stack{

    private int maxSize;
    private Person[] stackArray;
    private int top;

    public Stack(int max){
        maxSize = max;
        stackArray = new Person[maxSize];
        top = -1;
    }

    public void push(Person p){
        stackArray[++top] = p;
    }

    public Person pop(){
        System.out.println(stackArray[top].toString());
        return stackArray[top--];
    }

    public Person peek(){
        return stackArray[top];
    }
    
    public boolean isEmpty(){
        return (top == -1);
    }
    public int getTop(){
        return top;
    }
}

public class ReverseApp {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n;
        n = sc.nextInt();

        Person[] list = new Person[n];
        Stack stack = new Stack(n);

        for(int i=0; i<n; i++){
            list[i] = new Person(sc.next(), sc.next());
            stack.push(list[i]);
        }

        System.out.println("Reverse List: ");
        for(int i=0; i<n; i++){
            System.out.print((i+1) + ". ");
            list[i] = stack.pop();
        }
    }
}
