package Problem6;

class Queue
   {
   private int maxSize;
   private String[] queArray;
   private int front;
   private int rear;
   private int nItems;
//--------------------------------------------------------------
   public Queue(int s)          // constructor
      {
      maxSize = s;
      queArray = new String[maxSize];
      front = 0;
      rear = -1;
      nItems = 0;
      }
//--------------------------------------------------------------
   public void insert(String j)   // put item at rear of queue
      {
      if(rear == maxSize-1)         // deal with wraparound
         rear = -1;
      queArray[++rear] = j;         // increment rear and insert
      nItems++;                     // one more item
      }
//--------------------------------------------------------------
   public String remove()         // take item from front of queue
      {
      String temp = queArray[front++]; // get value and incr front
      if(front == maxSize)           // deal with wraparound
         front = 0;
      nItems--;                      // one less item
      return temp;
      }
//--------------------------------------------------------------
   public String peekFront()      // peek at front of queue
      {
      return queArray[front];
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
   }
class serviceCenter{
   private Queue vipQ;
   private Queue regularQ;

   public serviceCenter(){
      vipQ = new Queue(10);
      regularQ = new Queue(10);
   }
   public void enqueue(String cusName, boolean isVip){
      if(isVip == true){
         vipQ.insert(cusName);
      }
      else{
         regularQ.insert(cusName);
      }
   }
   public String serve_customer(){
      String s = "Nobody to serve!";
      if(!vipQ.isEmpty()){
         s = vipQ.remove();
      }
      else{
         if(!regularQ.isEmpty()){
            s = regularQ.remove();
         }
      }
      return s;
   }
}
class QueueApp
   {
   public static void main(String[] args)
      {
         serviceCenter service = new serviceCenter();

         service.enqueue("Alice", false);
         service.enqueue("Bob", true);
         service.enqueue("Charlie", false);

         System.out.println("Serve " + service.serve_customer());
         System.out.println("Serve " + service.serve_customer());
         System.out.println("Serve " + service.serve_customer());
      }
   }
