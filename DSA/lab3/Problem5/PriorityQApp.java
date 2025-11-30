package Problem5;

class PriorityQ
   {
   // array in sorted order, from max at 0 to min at size-1
   private int maxSize;
   private long[] queArray;
   private int nItems;
//-------------------------------------------------------------
   public PriorityQ(int s)          // constructor
      {
      maxSize = s;
      queArray = new long[maxSize];
      nItems = 0;
      }
//-------------------------------------------------------------
   public void insert(long item)    // insert item
      {
         queArray[nItems++] = item;

         int j;

         for(j = nItems-1; j>0; j--){
            if(queArray[j] > queArray[j-1]){
               swap(j, j-1);
            }
         }
         display();
}
//-------------------------------------------------------------
   public long remove()             // remove minimum item
      { return queArray[--nItems]; }
//-------------------------------------------------------------
   public long peekMin()            // peek at minimum item
      { return queArray[nItems-1]; }
//-------------------------------------------------------------
   public boolean isEmpty()         // true if queue is empty
      { return (nItems==0); }
//-------------------------------------------------------------
   public boolean isFull()          // true if queue is full
      { return (nItems == maxSize); }
//-------------------------------------------------------------
   public void display()
   { 
      for(int i=nItems-1; i>=0; i--){
         System.out.print(queArray[i] + " ");
      }
      System.out.println();
   }
//-------------------------------------------------------------
   public void swap(int a, int b){
      long temp = queArray[a];
      queArray[a] = queArray[b];
      queArray[b] = temp;
   }
}
class PriorityQApp
   {
   public static void main(String[] args)
      {
      PriorityQ thePQ = new PriorityQ(5);
      thePQ.insert(30);
      thePQ.insert(50);
      thePQ.insert(10);
      thePQ.insert(40);

      }
   }
