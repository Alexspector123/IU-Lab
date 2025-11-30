// insertSort.java
// demonstrates insertion sort
// to run this program: C>java InsertSortApp
//--------------------------------------------------------------
package Problem3;

class ArrayIns
   {
   private long[] a;                 // ref to array a
   private int nElems;               // number of data items
   private int numberOfPass;
   private int totalPass;
//--------------------------------------------------------------
   public ArrayIns(int max)          // constructor
      {
      a = new long[max];                 // create the array
      nElems = 0;                        // no items yet
      numberOfPass = 0;
      totalPass = 0;
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
public int getNumberPass() // displays array contents
{
   return numberOfPass;
}
// --------------------------------------------------------------
public int getTotalPass() // displays array contents
{
   return totalPass;
}
//--------------------------------------------------------------
   public void display()             // displays array contents
      {
      for(int j=0; j<nElems; j++)       // for each element,
         System.out.print(a[j] + " ");  // display it
      System.out.println("");
      }
//--------------------------------------------------------------
   public void insertionSort()
      {
      int in, out;

      for(out=1; out<nElems; out++)     // out is dividing line
         {
         System.out.println("During InsertSort: ");
         numberOfPass = 0;
         long temp = a[out];            // remove marked item
         in = out;                      // start shifts at out
         while(in>0 && a[in-1] >= temp) // until one is smaller,
            {
            a[in] = a[in-1];            // shift item to right
            --in;                       // go left one position
            numberOfPass++;
            display();
            }
         a[in] = temp;                  // insert marked item
         System.out.println("The number of Pass: " + numberOfPass);
         totalPass+=numberOfPass;
         System.out.println("//--------------------------------------------------------------");
         }  // end for
      }  // end insertionSort()
//--------------------------------------------------------------
   }  // end class ArrayIns
////////////////////////////////////////////////////////////////
class InsertSortApp
   {
   public static void main(String[] args)
      {
      int maxSize = 100;            // array size
      ArrayIns arr;                 // reference to array
      arr = new ArrayIns(maxSize);  // create the array

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

      arr.insertionSort();          // insertion-sort them

      System.out.println("After SelectSort: ");
      arr.display(); // display them again

      System.out.println("The total number of comparision = " + arr.getTotalPass());

      System.out.println("The algorithms'complexity = " + (n*(n-1)/4));
      }  // end main()
   }  // end class InsertSortApp
