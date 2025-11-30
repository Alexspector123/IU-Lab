package Problem2;

import java.util.*;

public class SpecialArray {

    private final int maxSize = 10;
    private int[] arr;
    private Stack<int[]> undo;
    private Stack<int[]> redo;

    public SpecialArray(){
        arr = new int[maxSize];
        undo = new Stack<int[]>();
        redo = new Stack<int[]>();

        Random rand = new Random();
        for(int i=0; i<maxSize; i++){
            arr[i] = rand.nextInt(20);
        }
    }

    public void update(int value, int index){

        undo.push(arr.clone());
        redo.clear();

        if(index < 0 || index > arr.length){
            System.out.println("Index out of bounds!");
        }
        else{
            arr[index] = value;
        }
    }

    public void undo(){

        if(!undo.isEmpty()){
            redo.push(arr.clone());
            arr = undo.pop();
            System.out.println("Undo successfully!");
        }
        else{
            System.out.println("Cannot undo!");
        }
    }

    public void redo(){

        if(!redo.isEmpty()){
            undo.push(arr.clone());
            arr = redo.pop();System.out.println("Redo successfully!");
        }
        else{
            System.out.println("Cannot redo!");
        }
    }

    public void display(){
        for(int i=0; i<maxSize; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        System.out.println("//------------------");
    }
    public static void main(String[] args) {

        SpecialArray sa = new SpecialArray();

        System.out.print("Initial array: ");
        sa.display();

        sa.update(0, 3);
        sa.update(0, 5);
        sa.update(0, 7);
        
        sa.display();

        sa.undo();
        sa.display();
        sa.undo();
        sa.display();
        sa.undo();
        sa.display();

        sa.redo();
        sa.display();
        sa.redo();
        sa.display();
        sa.redo();
        sa.display();
    }
}
