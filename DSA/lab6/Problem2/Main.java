package Problem2;

import java.util.Random;

public class Main {
   private long[] a; // ref to array a
   private long[] a1; // copy of array a
   private int nElems; // number of data items
   private int totalCompare;
   private int totalSwap;
   private int totalCopy;
   // --------------------------------------------------------------

   public Main(int max) // constructor
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
   // mergeSort
   public void mergeSort() {
      long[] workSpace = new long[nElems];
      recMergeSort(workSpace, 0, nElems - 1);
   }

   // -----------------------------------------------------------
   private void recMergeSort(long[] workSpace, int lowerBound,
         int upperBound) {
      if (lowerBound == upperBound)
         return;
      else {
         int mid = (lowerBound + upperBound) / 2;
         recMergeSort(workSpace, lowerBound, mid);
         recMergeSort(workSpace, mid + 1, upperBound);
         merge(workSpace, lowerBound, mid + 1, upperBound);
      }
      totalCompare++;
   } // end recMergeSort()
     // -----------------------------------------------------------

   private void merge(long[] workSpace, int lowPtr,
         int highPtr, int upperBound) {
      int j = 0;
      int lowerBound = lowPtr;
      int mid = highPtr - 1;
      int n = upperBound - lowerBound + 1;

      while (lowPtr <= mid && highPtr <= upperBound)
         if (a[lowPtr] < a[highPtr])
            workSpace[j++] = a[lowPtr++];
         else
            workSpace[j++] = a[highPtr++];
      totalCompare++;
      while (lowPtr <= mid) {
         workSpace[j++] = a[lowPtr++];
         totalCompare++;
         totalCopy++;
      }

      while (highPtr <= upperBound) {
         workSpace[j++] = a[highPtr++];
         totalCompare++;
         totalCopy++;
      }

      for (j = 0; j < n; j++) {
         a[lowerBound + j] = workSpace[j];
      }
   } // end merge()
     // --------------------------------------------------------------

   private void swap(int one, int two) {
      long temp = a[one];
      a[one] = a[two];
      a[two] = temp;
      totalSwap++; // increase number of swap by 1
   }

   // --------------------------------------------------------------
   // Quicksort
   public void quickSort() {
      recQuickSort(0, nElems - 1);
   }

   // --------------------------------------------------------------
   public void recQuickSort(int left, int right) {
      int size = right - left + 1;
      if (size < 10)
         insertionSort(left, right);
      else {
         long median = medianOf3(left, right);
         int partition = partitionIt(left, right, median);
         recQuickSort(left, partition - 1);
         recQuickSort(partition + 1, right);
      }
      totalCompare++;
   } // end recQuickSort()
     // --------------------------------------------------------------

   public long medianOf3(int left, int right) {
      int center = (left + right) / 2;
      if (a[left] > a[center]) {
         totalCompare++;
         swap(left, center);
      }
      if (a[left] > a[right]) {
         totalCompare++;
         swap(left, right);
      }
      if (a[center] > a[right]) {
         totalCompare++;
         swap(center, right);
      }

      swap(center, right - 1);
      return a[right - 1];
   } // end medianOf3()
     // --------------------------------------------------------------

   public int partitionIt(int left, int right, long pivot) {
      int leftPtr = left;
      int rightPtr = right - 1;
      while (true) {
         while (a[++leftPtr] < pivot) {
            totalCompare++;
         }
         ; // (nop)
         while (a[--rightPtr] > pivot) {
            totalCompare++;
         }
         ; // (nop)
         if (leftPtr >= rightPtr)
            break;
         else
            swap(leftPtr, rightPtr);
      }
      swap(leftPtr, right - 1);
      return leftPtr;
   } // end partitionIt()
     // --------------------------------------------------------------
     // insertion sort

   public void insertionSort(int left, int right) {
      int in, out;
      // sorted on left of out
      for (out = left + 1; out <= right; out++) {
         long temp = a[out];
         in = out;
         while (in > left && a[in - 1] >= temp) {
            totalCompare++;
            a[in] = a[in - 1];
            --in;
         }
         a[in] = temp;
      } // end for
   } // end insertionSort()
     // --------------------------------------------------------------
     // Shell Sort
   public void shellSort() {
      int inner, outer;
      long temp;
      int h = 1;
      while (h <= nElems / 3)
         h = h * 3 + 1;
      while (h > 0) {
         for (outer = h; outer < nElems; outer++) {
            temp = a[outer];
            inner = outer;
            while (inner > h - 1 && a[inner - h] >= temp) {
               totalCompare++;
               totalCopy++;
               a[inner] = a[inner - h];
               inner -= h;
            }
            a[inner] = temp;
         }
         h = (h - 1) / 3;
      } // end while(h>0)
   } // end shellSort()
     // --------------------------------------------------------------
   public void resetArr() {
      for (int i = 0; i < nElems; i++) {
         a[i] = a1[i];
      }
      totalCompare = 0;
      totalSwap = 0;
      totalCopy = 0;
   }
}

class SortApp {
   public static void main(String[] args) {
      int[] maxSizes = { 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000 };
      Main arr; // reference to array
      int size = 0;
      while (size < maxSizes.length) {
         int maxSize = maxSizes[size];
         arr = new Main(maxSize); // create the array
         Random rand = new Random();
         for (int i = 0; i < maxSize; i++) {
            arr.insert(rand.nextInt(maxSize));
         }
         System.out.println("Array Size: " + maxSize);
         System.out.printf("%-15s %-15s %-15s %-15s%n", "Algorithm", "Comparision", "Swap", "Copy");
         System.out.println("//--------------------------------------------------------------");

         arr.mergeSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Merge Sort", arr.getTotalCompare(), arr.getTotalSwap(),
               arr.getTotalCopy());
         arr.resetArr();

         arr.shellSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Shell Sort", arr.getTotalCompare(), arr.getTotalSwap(),
               arr.getTotalCopy());
         arr.resetArr();

         arr.quickSort();
         System.out.printf("%-15s %-15d %-15d %-15d%n", "Quick Sort", arr.getTotalCompare(), arr.getTotalSwap(),
               arr.getTotalCopy());
         arr.resetArr();

         size++;
         System.out.println("//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
      }
   }
}