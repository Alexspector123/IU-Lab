// PartitionApp.java
// demonstrates partitioning an array
////////////////////////////////////////////////////////////////
// Exercises:
// 1. Add counters for the number of comparisons and swaps and display
//    them after partitioning
// 2. Investigate the relationship between the index of partitioning,
//    the number of comparison, and the number of swaps.
// 3. Do Exercise 2 with different pivots: 
//    - beginning, end, or middle of the interval; 
//    - selected at random from the interval or from a larger interval;
//    - last item in the array.
// 4. Compute the average number of comparisons and swaps over 100 runs.

class PartitionApp
   {
   public static void main(String[] args)
      {
      int totalSwap = 0;
      int totalComparision = 0;
      int maxSize = 100;             // array size
      ArrayPar arr;                 // reference to array
      arr = new ArrayPar(maxSize);  // create the array

      for(int j=0; j<maxSize; j++)  // fill array with
         {                          // random numbers
         long n = (int)(java.lang.Math.random()*199);
         arr.insert(n);
         }
      arr.display();                // display unsorted array

      // Beginning of the interval
      long pivot = 0;              // pivot value
      System.out.println("Pivot is " + pivot);
      int size = arr.size();
                                    // partition array
      int partDex = arr.partitionIt(0, size-1, pivot);
      System.out.println("Partition is at index " + partDex);
      arr.display();                // display partitioned array

      // End of the interval
      pivot = 199;              // pivot value
      System.out.println("Pivot is " + pivot);
      size = arr.size();
                                    // partition array
      partDex = arr.partitionIt(0, size-1, pivot);
      System.out.println("Partition is at index " + partDex);
      arr.display();                // display partitioned array

      // Middle of the interval
      pivot = 100;              // pivot value
      System.out.println("Pivot is " + pivot);
      size = arr.size();
                                          // partition array
      partDex = arr.partitionIt(0, size-1, pivot);
      
      System.out.println("Partition is at index " + partDex);
      arr.display();                // display partitioned array

      // Random of the interval
      pivot = (int)(java.lang.Math.random()*199);;              // pivot value
      System.out.println("Pivot is " + pivot);
      size = arr.size();
                                                // partition array
      partDex = arr.partitionIt(0, size-1, pivot);
            
      System.out.println("Partition is at index " + partDex);
      arr.display();                // display partitioned array

      // Last item of the array
      pivot = arr.getLastE();              // pivot value
      System.out.println("Pivot is " + pivot);
      size = arr.size();
                                                // partition array
      partDex = arr.partitionIt(0, size-1, pivot);
            
      System.out.println("Partition is at index " + partDex);
      arr.display();                // display partitioned array

      int t=0;
      while (t < 100) {
         arr.setComparisions(0);
         arr.setSwaps(0);
         pivot = (int)(java.lang.Math.random()*199);
         System.out.println("Pivot is " + pivot);
         size = arr.size();
         partDex = arr.partitionIt(0, size-1, pivot);
         System.out.println("Partition is at index " + partDex);
         arr.display();
         totalComparision += arr.getComparisions();
         totalSwap += arr.getSwaps();
         t++;
      }
      System.out.println("The average number of comparisions over 100 runs: " + totalComparision/100);
      System.out.println("The average number of swaps over 100 runs: " + totalSwap/100);
      }  // end main()
   }  // end class PartitionApp
////////////////////////////////////////////////////////////////


class ArrayPar
   {
   private long[] theArray;          // ref to array theArray
   private int nElems;               // number of data items
   private int swaps = 0;
   private int comparisons = 0;
//--------------------------------------------------------------
   public ArrayPar(int max)          // constructor
      {
      theArray = new long[max];      // create the array
      nElems = 0;                    // no items yet
      swaps = 0;
      comparisons = 0;
      }
//--------------------------------------------------------------
   public void insert(long value)    // put element into array
      {
      theArray[nElems] = value;      // insert it
      nElems++;                      // increment size
      }
//--------------------------------------------------------------
   public int size()                 // return number of items
      { return nElems; }
//--------------------------------------------------------------
   public void display()             // displays array contents
      {
      System.out.print("A=");
      for(int j=0; j<nElems; j++)    // for each element,
         System.out.print(theArray[j] + " ");  // display it
      System.out.println("");
      System.out.println("The number of swap: " + swaps);
      System.out.println("The number of comparision: " + comparisons);
      System.out.println("//---------------------------------------------------");
      }
//--------------------------------------------------------------
    public int partitionIt(int left, int right, long pivot)
       {
       int leftPtr = left - 1;           // right of first elem
       int rightPtr = right + 1;         // left of pivot
       while(true)
          {
          while(leftPtr < right &&       // find bigger item
                theArray[++leftPtr] < pivot){
                     comparisons++;  // (nop)
                }

          while(rightPtr > left &&       // find smaller item
                theArray[--rightPtr] > pivot){
                  comparisons++;  // (nop)
                }
          if(leftPtr >= rightPtr)        // if pointers cross,
             break;                      //    partition done
          else                           // not crossed, so
             swap(leftPtr, rightPtr);    //    swap elements
          }  // end while(true)
       return leftPtr;                   // return partition
       }  // end partitionIt()
//--------------------------------------------------------------
   public void swap(int dex1, int dex2)  // swap two elements
      {
      swaps++;
      long temp;
      temp = theArray[dex1];             // A into temp
      theArray[dex1] = theArray[dex2];   // B into A
      theArray[dex2] = temp;             // temp into B
      }  // end swap()
   public long getLastE(){
      return theArray[nElems-1];
   }
   public int getComparisions(){
      return comparisons;
   }
   public int getSwaps(){
      return swaps;
   }
   public void setComparisions(int comparisions){
      this.comparisons = comparisions;
   }
   public void setSwaps(int swaps){
      this.swaps = swaps;
   }
//--------------------------------------------------------------
   }  // end class ArrayPar
////////////////////////////////////////////////////////////////
