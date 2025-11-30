// highArray.java
// demonstrates array class with high-level interface
// to run this program: C>java HighArrayApp
////////////////////////////////////////////////////////////////
package Problem2.iii;

import java.util.Random;

class HighArray
   {
   private long[] a;                 // ref to array a
   private int nElems;               // number of data items
   public int counter;
   //-----------------------------------------------------------
   public HighArray(int max)         // constructor
      {
      a = new long[max];                 // create the array
      nElems = 0;                        // no items yet
      }
   //-----------------------------------------------------------
   public boolean find(long searchKey)
      {                              // find specified value
      int j;
      counter = 0;
      for(j=0; j<nElems; j++){            // for each element,
         counter++;                       // count the number of comparision
         if(a[j] == searchKey)           // found item?
            break;                       // exit loop before end
      }
      if(j == nElems)                    // gone to end?
         return false;                   // yes, can't find it
      else
         return true;                    // no, found it
      }  // end find()
   //-----------------------------------------------------------
   public void insert(long value)    // put element into array
      {
      a[nElems] = value;             // insert it
      nElems++;                      // increment size
      }
   //-----------------------------------------------------------
   public boolean delete(long value)
      {
      int j;
      for(j=0; j<nElems; j++)        // look for it
         if( value == a[j] )
            break;
      if(j==nElems)                  // can't find it
         return false;
      else                           // found it
         {
         for(int k=j; k<nElems; k++) // move higher ones down
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
   public long getMax()    // put element into array
      {
      if(nElems == 0){
         return -1;                  // if the array is empty
      }
      else{
         int highestKey = 0;
         for(int i=1; i<nElems; i++){
            if(a[i] > a[highestKey]) highestKey = i;
         }
         return a[highestKey];
         }
      }
   //-----------------------------------------------------------
   public void noDups()    // put element into array
      {
         for(int i=0; i<nElems-1; i++){
            for(int j=i+1; j<nElems; j++){
               if(a[i] == a[j]){
                  delete(a[i]);
                  i--;  
                  break;
               }
            }
         }
      }
   //-----------------------------------------------------------
   }  // end class HighArray
////////////////////////////////////////////////////////////////
class HighArrayApp
   {
   public static void main(String[] args)
      {

      int maxSize = 1000;            // array size
      HighArray arr;                // reference to array
      arr = new HighArray(maxSize); // create the array
      double average = 0;

      Random rand = new Random();
      for(int i=0; i<maxSize-1;i++){
         arr.insert(rand.nextInt(1000));
      }

      arr.display();                // display items

      arr.noDups();

      System.out.println("After deleted all duplicate element: ");
      arr.display();                // display items again

      for(int i=0; i<maxSize; i++){
         int searchKey = rand.nextInt(1000);           // search for item
         if(arr.find(searchKey))
            System.out.println("Found " + searchKey);
         else
            System.out.println("Can't find " + searchKey);
         System.out.println("The number of comparision: " + arr.counter);
         average += arr.counter;
      }

      System.err.println("The average number of comparision: " + (average/1000));
      System.err.println("The highest key in the array: " + arr.getMax());


      }  // end main()
   }  // end class HighArrayApp
