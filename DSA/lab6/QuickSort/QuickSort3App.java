// QuickSort3App.java
// demonstrates quick sort; uses insertion sort for small partitions
////////////////////////////////////////////////////////////////
// Exercises:
// 1. Add counters for the number of comparisons, swaps, and recursive calls,
//    and display them after sorting
// 2. Compute the average number of comparisons, swaps, and recursive calls
//    over 100 runs
// 3. Analyze the complexity of the algortihm by varying the size of the 
//    array (e.g. 16, 32, 64, 128, 256) and examining the parameters from item 2.
// 4. Compare the performance with insertion sort.
// 5. Experiment with different cutoff value and find the best one for different
//    sizes of the array.

class QuickSort3App {
   public static void main(String[] args) {
      int maxSize = 16; // array size
      int totalComparision = 0;
      int totalSwap = 0;
      int totalRecursiveCalls = 0;
      int t = 0;
      while (t < 100) {
         System.out.println("The " + (t+1) + " run:");
         ArrayIns3 arr;
         arr = new ArrayIns3(maxSize); // create array
         for (int j = 0; j < maxSize; j++) // fill array with
         { // random numbers
            long n = (int) (java.lang.Math.random() * 99);
            arr.insert(n);
         }
         arr.display(); // display items
         arr.quickSort(); // quicksort them
         arr.display(); // display them again
         totalComparision += arr.getComparisions();
         totalSwap += arr.getSwaps();
         totalRecursiveCalls += arr.getRecursiveCalls();
         t++;
         System.out.println("The number of comparision: " + arr.getComparisions());
         System.out.println("The number of swap: " + arr.getSwaps());
         System.out.println("The number of recursive call: " + arr.getRecursiveCalls());
         System.out.println("//---------------------------------------------------------------//");
      }
      System.out.println("The average comparision over 100 runs is: " + (totalComparision / 100));
      System.out.println("The average swap over 100 runs is: " + (totalSwap / 100));
      System.out.println("The average recursive call over 100 runs is: " + (totalRecursiveCalls / 100));
   } // end main()
} // end class QuickSort3App
////////////////////////////////////////////////////////////////

class ArrayIns3 {
   private int comparisions;
   private int swaps;
   private int recursiveCalls;
   private long[] theArray; // ref to array theArray
   private int nElems; // number of data items
   // --------------------------------------------------------------

   public ArrayIns3(int max) // constructor
   {
      theArray = new long[max]; // create the array
      nElems = 0; // no items yet
      comparisions = 0;
      swaps = 0;
      recursiveCalls = 0;
   }

   // --------------------------------------------------------------
   public void insert(long value) // put element into array
   {
      theArray[nElems] = value; // insert it
      nElems++; // increment size
   }

   // --------------------------------------------------------------
   public void display() // displays array contents
   {
      System.out.print("A=");
      for (int j = 0; j < nElems; j++) // for each element,
         System.out.print(theArray[j] + " "); // display it
      System.out.println("");
   }

   // --------------------------------------------------------------
   public void quickSort() {
      recQuickSort(0, nElems - 1);
      // insertionSort(0, nElems-1); // the other option
   }

   // --------------------------------------------------------------
   public void recQuickSort(int left, int right) {
      recursiveCalls++;
      int size = right - left + 1;
      if (size < 10) // insertion sort if small
         insertionSort(left, right);
      else // quicksort if large
      {
         long median = medianOf3(left, right);
         int partition = partitionIt(left, right, median);
         recQuickSort(left, partition - 1);
         recQuickSort(partition + 1, right);
      }
   } // end recQuickSort()
   // --------------------------------------------------------------

   public long medianOf3(int left, int right) {
      int center = (left + right) / 2;
      // order left & center
      if (theArray[left] > theArray[center])
      {
         comparisions++;
         swap(left, center);
      }
      // order left & right
      if (theArray[left] > theArray[right])
      {
         comparisions++;
         swap(left, right);
      }
      // order center & right
      if (theArray[center] > theArray[right])
      {
         comparisions++;
         swap(center, right);
      }

      swap(center, right - 1); // put pivot on right
      return theArray[right - 1]; // return median value
   } // end medianOf3()
   // --------------------------------------------------------------

   public void swap(int dex1, int dex2) // swap two elements
   {
      long temp = theArray[dex1]; // A into temp
      theArray[dex1] = theArray[dex2]; // B into A
      theArray[dex2] = temp; // temp into B
      swaps++;
   } // end swap(
   // --------------------------------------------------------------

   public int partitionIt(int left, int right, long pivot) {
      int leftPtr = left; // right of first elem
      int rightPtr = right - 1; // left of pivot
      while (true) {
         while (theArray[++leftPtr] < pivot) // find bigger
         {
            comparisions++;
         }
            ; // (nop)
         while (theArray[--rightPtr] > pivot) // find smaller
         {
            comparisions++;
         }
            ; // (nop)
         if (leftPtr >= rightPtr) // if pointers cross,
            break; // partition done
         else // not crossed, so
            swap(leftPtr, rightPtr); // swap elements
      } // end while(true)
      swap(leftPtr, right - 1); // restore pivot
      return leftPtr; // return pivot location
   } // end partitionIt()
   // --------------------------------------------------------------
   // insertion sort

   public void insertionSort(int left, int right) {
      int in, out;
      // sorted on left of out
      for (out = left + 1; out <= right; out++) {
         long temp = theArray[out]; // remove marked item
         in = out; // start shifts at out
                   // until one is smaller,
         while (in > left && theArray[in - 1] >= temp) {
            comparisions++;
            theArray[in] = theArray[in - 1]; // shift item to right
            --in; // go left one position
         }
         theArray[in] = temp; // insert marked item
      } // end for
   } // end insertionSort()
   // --------------------------------------------------------------

   public int getComparisions() {
      return comparisions;
   }

   // --------------------------------------------------------------
   public int getSwaps() {
      return swaps;
   }

   // --------------------------------------------------------------
   public int getRecursiveCalls() {
      return recursiveCalls;
   }
} // end class ArrayIns
////////////////////////////////////////////////////////////////
