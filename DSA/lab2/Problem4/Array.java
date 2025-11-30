package Problem4;

import java.util.Random;

public class Array {
    private long[] a; // ref to array a
    private long[] a1; // copy of array a
    private int nElems; // number of data items
    private int totalCompare;
    private int totalSwap;
    private int totalCopy;
    // --------------------------------------------------------------
 
    public Array(int max) // constructor
    {
       a = new long[max]; // create the array
       a1 = new long[max];
       nElems = 0; // no items yet
       totalCompare = 0;
       totalSwap = 0;
       totalCopy = 0;
    }
 
    // --------------------------------------------------------------
    public void insert(long value) // put element into array
    {
       a[nElems] = value; // insert it
       a1[nElems] = value;
       nElems++; // increment size
    }
    // --------------------------------------------------------------
    public void display() // displays array contents
    {
       for (int j = 0; j < nElems; j++) // for each element,
          System.out.print(a[j] + " "); // display it
       System.out.println("");
    }
    // --------------------------------------------------------------
    public int getNElems() // displays array contents
    {
       return nElems;
    }
    // --------------------------------------------------------------
    public int getTotalCompare() // displays array contents
    {
       return totalCompare;
    }
    // --------------------------------------------------------------
    public int getTotalSwap() // displays array contents
    {
       return totalSwap;
    }
    // --------------------------------------------------------------
    public int getTotalCopy() // displays array contents
    {
       return totalCopy;
    }
    // --------------------------------------------------------------
    public void bubbleSort() {
       int out, in;
       int numberOfCompare;
       for(out = 0; out<nElems-1; out++){
         numberOfCompare = 0;
         for(in = out+1; in<nElems; in++){
            if(a[out] > a[in]){
               swap(out,in);
            }
            numberOfCompare++;
         }
         totalCompare += numberOfCompare;
       }
    } // end bubbleSort()
    // --------------------------------------------------------------
 
    private void swap(int one, int two) {
       long temp = a[one];
       a[one] = a[two];
       a[two] = temp;
       totalSwap++; // increase number of swap by 1
    }
    // --------------------------------------------------------------
    public void selectionSort()
      {
      int out, in, min;
      int numberOfCompare;
      for(out=0; out<nElems-1; out++)   // outer loop
         {
            numberOfCompare = 0;
            min = out;                     // minimum
            for(in=out+1; in<nElems; in++){ // inner loop
               if(a[in] < a[min] )         // if min greater,
                  min = in;               // we have a new min
               numberOfCompare++;

            }
            totalCompare += numberOfCompare;
            swap(out, min);
         }  // end for(out)
      }  // end selectionSort()
//--------------------------------------------------------------
public void insertionSort()
      {
      int in, out;
      int numberOfPass;
      for(out=1; out<nElems; out++)     // out is dividing line
         {
         numberOfPass = 0;
         long temp = a[out];            // remove marked item
         in = out;                      // start shifts at out
         while(in>0 && a[in-1] >= temp) // until one is smaller,
            {
            a[in] = a[in-1];            // shift item to right
            --in;                       // go left one position
            numberOfPass++;
            }
         a[in] = temp;                  // insert marked items
         totalCopy+=numberOfPass;
         }  // end for
      }  // end insertionSort()
//--------------------------------------------------------------
      public void resetArr(){
         for(int i=0; i<nElems; i++){
            a[i] = a1[i];
         }
         totalCompare = 0;
         totalSwap = 0;
         totalCopy = 0;
      }
}

class SortApp {
    public static void main(String[] args) {
       int[] maxSizes = {10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000};
       Array arr; // reference to array
       int size = 0;
       while(size<maxSizes.length){
         int maxSize = maxSizes[size];
         arr = new Array(maxSize); // create the array
         Random rand = new Random();
         for(int i=0; i<maxSize; i++){
            arr.insert(rand.nextInt(maxSize));
         }

         System.out.println("Array Size: " + maxSize);
         System.out.printf("%-15s %-15s %-15s %-15s%n", "Algorithm", "Comparision", "Swap", "Copy");
         System.out.println("//--------------------------------------------------------------");

         arr.bubbleSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Bubble Sort", arr.getTotalCompare(), arr.getTotalSwap(), arr.getTotalCopy());
         arr.resetArr();

         arr.selectionSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Selection Sort", arr.getTotalCompare(), arr.getTotalSwap(), arr.getTotalCopy());
         arr.resetArr();

         arr.insertionSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Insertion Sort", arr.getTotalCompare(), arr.getTotalSwap(), arr.getTotalCopy());
         arr.resetArr();

         size++;
         System.out.println("//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
       }
    }
 }
 