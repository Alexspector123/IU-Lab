// selectSort.java
// demonstrates selection sort
// to run this program: C>java SelectSortApp
////////////////////////////////////////////////////////////////
package Problem2;

class ArraySel
   {
   private long[] a;                 // ref to array a
   private int nElems;               // number of data items
   private int numberOfCompare = 0;
   private int totalCompare = 0;
//--------------------------------------------------------------
   public ArraySel(int max)          // constructor
      {
      a = new long[max];                 // create the array
      nElems = 0;                        // no items yet
      }
//--------------------------------------------------------------
   public void insert(long value)    // put element into array
      {
      a[nElems] = value;             // insert it
      nElems++;                      // increment size
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
//--------------------------------------------------------------
   public void display()             // displays array contents
      {
      for(int j=0; j<nElems; j++)       // for each element,
         System.out.print(a[j] + " ");  // display it
      System.out.println("");
      }
//--------------------------------------------------------------
   public void selectionSort()
      {
      int out, in, min;

      for(out=0; out<nElems-1; out++)   // outer loop
         {
            System.out.println("During SelectSort: ");
            numberOfCompare = 0;
            min = out;                     // minimum
            for(in=out+1; in<nElems; in++){ // inner loop
               if(a[in] < a[min] )         // if min greater,
                  min = in;               // we have a new min
               numberOfCompare++;
               display();

            }
            System.out.println("The number of Compare: " + numberOfCompare);
            totalCompare += numberOfCompare;
            System.out.println("The items that are swapped: " + out + ", " +min);
            swap(out, min);                // swap them
            System.out.println("//--------------------------------------------------------------");
         }  // end for(out)
      }  // end selectionSort()
//--------------------------------------------------------------
   private void swap(int one, int two)
      {
      long temp = a[one];
      a[one] = a[two];
      a[two] = temp;
      }
//--------------------------------------------------------------
   }  // end class ArraySel
////////////////////////////////////////////////////////////////
class SelectSortApp
   {
   public static void main(String[] args)
      {
      int maxSize = 100;            // array size
      ArraySel arr;                 // reference to array
      arr = new ArraySel(maxSize);  // create the array

      arr.insert(77);               // insert 10 items
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

      System.out.println("Before SelectSort: ");
      arr.display(); // display items

      arr.selectionSort(); // selection-sort them

      System.out.println("After SelectSort: ");
      arr.display(); // display them again

      System.out.println("The total number of comparision = " + arr.getTotalCompare());

      System.out.println("The algorithms'complexity = " + (n*(n-1)/2));
      }  // end main()
   }  // end class SelectSortApp
////////////////////////////////////////////////////////////////
