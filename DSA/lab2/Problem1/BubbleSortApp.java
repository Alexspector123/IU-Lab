// bubbleSort.java
// demonstrates bubble sort
// to run this program: C>java BubbleSortApp
////////////////////////////////////////////////////////////////
package Problem1;

class ArrayBub {
   private long[] a; // ref to array a
   private int nElems; // number of data items
   private int nSwaps; // number of swaps
   private int numberOfCompare;
   private int totalCompare;
   // --------------------------------------------------------------

   public ArrayBub(int max) // constructor
   {
      a = new long[max]; // create the array
      nElems = 0; // no items yet
      nSwaps = 0; // no swaps yet
      numberOfCompare = 0;
      totalCompare = 0;
   }

   // --------------------------------------------------------------
   public void insert(long value) // put element into array
   {
      a[nElems] = value; // insert it
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
   public int getNumberCompare() // displays array contents
   {
      return numberOfCompare;
   }
   // --------------------------------------------------------------
   public int getTotalCompare() // displays array contents
   {
      return totalCompare;
   }
   // --------------------------------------------------------------
   public void bubbleSort() {
      int out, in;

      for (out = nElems - 1; out > 1; out--){ // outer loop (backward)
         
         System.out.println("During BubbleSort: ");
         numberOfCompare = 0;
         for (in = 0; in < out; in++){ // inner loop (forward)
            if (a[in] > a[in + 1]){ // out of order?
               swap(in, in + 1); // swap them
            }
            numberOfCompare++;
            display();
         }
         System.out.println("The number of Compare: " + numberOfCompare);
         System.out.println("//--------------------------------------------------------------");
         totalCompare += numberOfCompare;
      }
   } // end bubbleSort()
   // --------------------------------------------------------------

   private void swap(int one, int two) {
      long temp = a[one];
      a[one] = a[two];
      a[two] = temp;
      nSwaps++; // increase number of swap by 1
   }

   public int getSwapNumber() {
      return nSwaps;
   }
   // --------------------------------------------------------------
} // end class ArrayBub
  ////////////////////////////////////////////////////////////////

class BubbleSortApp {
   public static void main(String[] args) {
      int maxSize = 100; // array size
      ArrayBub arr; // reference to array
      arr = new ArrayBub(maxSize); // create the array

      arr.insert(77); // insert 10 items
      arr.insert(99);
      arr.insert(44);
      arr.insert(55);
      arr.insert(22);
      arr.insert(88);
      arr.insert(11);
      arr.insert(00);
      arr.insert(66);
      arr.insert(33);

      int n = arr.getNElems();

      System.out.println("Before BubbleSort: ");
      arr.display(); // display items

      arr.bubbleSort(); // bubble sort them

      System.out.println("After BubbleSort: ");
      arr.display(); // display them again

      // display the number of swaps
      System.out.println("The number of swaps = " + arr.getSwapNumber());

      System.out.println("The total number of comparision = " + arr.getTotalCompare());

      System.out.println("The algorithms'complexity = " + (n*(n-1)/2));
   } // end main()
} // end class BubbleSortApp
  ////////////////////////////////////////////////////////////////
