// orderedArray.java
// demonstrates ordered array class
// to run this program: C>java OrderedApp
////////////////////////////////////////////////////////////////
package Problem2.iv;

import java.util.Random;

class OrdArray
   {
   private long[] a;                 // ref to array a
   private int nElems;               // number of data items
   int counter;
   //-----------------------------------------------------------
   public OrdArray(int max)          // constructor
      {
      a = new long[max];             // create array
      nElems = 0;
      }
   //-----------------------------------------------------------
   public int size()
      { return nElems; }
   //-----------------------------------------------------------
   public int find(long searchKey)
      {
      int lowerBound = 0;
      int upperBound = nElems-1;
      int curIn;
      counter = 0;

      while(true)
         {
         curIn = (lowerBound + upperBound ) / 2;
         counter++;
         if(a[curIn]==searchKey){
            return curIn;              // found it
         }
         else if(lowerBound > upperBound)
            return nElems;             // can't find it
         else                          // divide range
            {
            if(a[curIn] < searchKey)
               lowerBound = curIn + 1; // it's in upper half
            else
               upperBound = curIn - 1; // it's in lower half
            }  // end else divide range
         }  // end while
      }  // end find()
   //-----------------------------------------------------------
   public void insert(long value)    // put element into array
      {
      int j;
      for(j=0; j<nElems; j++)        // find where it goes
         if(a[j] > value)            // (linear search)
            break;
      for(int k=nElems; k>j; k--)    // move bigger ones up
         a[k] = a[k-1];
      a[j] = value;                  // insert it
      nElems++;                      // increment size
      }  // end insert()
   //-----------------------------------------------------------
   public boolean delete(long value)
      {
      int j = find(value);
      if(j==nElems)                  // can't find it
         return false;
      else                           // found it
         {
         for(int k=j; k<nElems; k++) // move bigger ones down
            a[k] = a[k+1];
         nElems--;                   // decrement size
         return true;
         }
      }  // end delete()
   //-----------------------------------------------------------
   public void display()             // displays array contents
      {
      for(int j=0; j<nElems; j++)       // for each element,
         System.out.print(a[j] + " ");  // display it
      System.out.println("");
      }
   //-----------------------------------------------------------
   }  // end class OrdArray
////////////////////////////////////////////////////////////////
class OrderedApp
   {
   public static void main(String[] args)
      {

      int maxSize = 1000;             // array size
      OrdArray arr;                  // reference to array
      arr = new OrdArray(maxSize);   // create the array
      double average = 0;

      Random rand = new Random();
      for(int i=0;i<maxSize;i++){
         arr.insert(rand.nextInt(1000));
      }

      arr.display();                 // display items

      for(int i=0;i<maxSize;i++){
         int searchKey = rand.nextInt(1000);            // search for item
         if(arr.find(searchKey) != arr.size())
            System.out.println("Found " + searchKey);
         else
            System.out.println("Can't find " + searchKey);
         System.out.println("The number of comparision: " + arr.counter);
         average += arr.counter;
      }
      
      System.err.println("The average number of comparision: " + (average/1000));
      
      }  // end main()
   }  // end class OrderedApp
