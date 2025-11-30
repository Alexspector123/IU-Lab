package Problem5;

import java.util.*;

class PriorityQueue
   {
   private long[] timeProccessing;
   private long[] no;
   private int maxSize;
   private int nItems;
//--------------------------------------------------------------
   public PriorityQueue(int s)          // constructor
      {
      maxSize = s;
      timeProccessing = new long[maxSize];
      no = new long[maxSize];
      nItems = 0;
      }
//--------------------------------------------------------------
   public void insert(long item, int t)   // put item at rear of queue
      {
         if(isFull()){
            return;
         }
         timeProccessing[nItems] = item;
         no[nItems] = t;
         nItems++;

         int j;

         for(j = nItems-1; j>0; j--){
            if(timeProccessing[j] > timeProccessing[j-1]){
               swap(j, j-1);
            }
         }
         
         System.out.println("Customer " + t + " added with service time " + item + " minutes");
      }
//--------------------------------------------------------------
    public long remove()         // take item from front of queue
      {
         if(isEmpty()){
            return -1;
         }
         return timeProccessing[--nItems]; 
      }
//--------------------------------------------------------------
    public long peekMin()            // peek at minimum item
        { 
            return timeProccessing[nItems-1]; 
        }
//--------------------------------------------------------------
   public boolean isEmpty()    // true if queue is empty
      {
      return (nItems==0);
      }
//--------------------------------------------------------------
   public boolean isFull()     // true if queue is full
      {
      return (nItems==maxSize);
      }
//--------------------------------------------------------------
   public int size()           // number of items in queue
      {
      return nItems;
      }
//-------------------------------------------------------------
    public void swap(int a, int b){
        long temp = timeProccessing[a];
        timeProccessing[a] = timeProccessing[b];
        timeProccessing[b] = temp;

        temp = no[a];
        no[a] = no[b];
        no[b] = temp;
 }
   }
class App{
   public static void main(String[] args)
      {
         PriorityQueue theQueue = new PriorityQueue(10);
         Random rand = new Random();
         
         int t = 1;
         theQueue.insert(rand.nextInt(5)+3,t++);

         for(int i=1; i<=10; i++){
            for(int j=0; j<theQueue.peekMin(); j++){
               System.out.println(i + " is servicing");
            }
            if(rand.nextInt(1) == 0){
               theQueue.insert(rand.nextInt(5) + 3,t++);
            }
            System.out.println("Customer " + i + " served with service time " + theQueue.remove() +" minutes.");
         }
      }
   }
