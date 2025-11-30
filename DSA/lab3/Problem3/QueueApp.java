package Problem3;

import java.util.*;

class Queue
   {
   private int maxSize;
   private long[] timeProccessing;
   private int front;
   private int rear;
   private int nItems;
//--------------------------------------------------------------
   public Queue(int s)          // constructor
      {
      maxSize = s;
      timeProccessing = new long[maxSize];
      front = 0;
      rear = -1;
      nItems = 0;
      }
//--------------------------------------------------------------
   public void insert(long j)   // put item at rear of queue
      {
         if(isFull()){
            return;
         }
         if(rear == maxSize-1)         // deal with wraparound
            rear = -1;
         ++rear;
         timeProccessing[rear] = j;         // increment rear and insert
         nItems++;                     // one more item
         System.out.println("Customer " + (rear+1) + " added with service time " + j + " minutes");
      }
//--------------------------------------------------------------
   public long remove()         // take item from front of queue
      {
         if(isEmpty()){
            return -1;
         }
         long temp = timeProccessing[front++]; // get value and incr front
         if(front == maxSize)           // deal with wraparound
            front = 0;
         nItems--;                      // one less item
         return temp;
      }
//--------------------------------------------------------------
   public long removeItem(int n)         // take item from front of queue
      {
         if(isEmpty()){
         System.out.println("The queue is Empty");
         return -1;
         }
         int index = 0;
         for(int i=nItems-1; i>=0; i--){
            if(timeProccessing[i] == n){
               index = 1;
            }
            if(index == 1 && i>0){
               timeProccessing[i] = timeProccessing[i-1];
            }
         }
         front++;
         if(front == maxSize)           // deal with wraparound
            front = 0;
         nItems--;                      // one less item
         return n;
      }
//--------------------------------------------------------------
   public long peekFront()      // peek at front of queue
      {
      return timeProccessing[front];
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
//--------------------------------------------------------------
   public void displayFront()
      {
         System.out.println("The queue array: ");
         for(int i = 0; i<maxSize; i++){
            System.out.print(timeProccessing[i] + " ");
         }
         System.out.println();
         System.out.println("The front incides: " + timeProccessing[front]);
         System.out.println("The rear incides: " + timeProccessing[rear]);
      }
//--------------------------------------------------------------
   public void displayFrontRear()
      {
         int tempFront = front;
         System.out.println("The queue is: ");
         for(int i=0; i<nItems; i++){
            System.out.print(timeProccessing[tempFront] + " ");
            tempFront = (tempFront+1)%maxSize;
         }
         System.out.println();
      }
//--------------------------------------------------------------
   public void display()
      {
         displayFront();
         displayFrontRear();
      }
   }
class QueueApp
   {
   public static void main(String[] args)
      {
         Queue theQueue = new Queue(10);
         Random rand = new Random();

         for(int i=1; i<=10; i++){
            theQueue.insert(rand.nextInt(5));
            for(int j=0; j<theQueue.peekFront(); j++){
               System.out.println(i + " is servicing");
               if(rand.nextInt(1) == 0){
                  theQueue.insert(rand.nextInt(5) + 3);
               }
            }
            if(rand.nextInt(1) == 0){
               theQueue.insert(rand.nextInt(5) + 3);
            }
            System.out.println("Customer " + i + " served with service time " + theQueue.remove() +" minutes.");
         }
      }
   }
