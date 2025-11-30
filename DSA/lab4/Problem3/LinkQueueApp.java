package Problem3;

import java.util.Random;

class LinkQueueApp {
   public static void main(String[] args) {
      LinkQueue theQueue = new LinkQueue();
      Random rand = new Random();
      int n = 5;
      System.out.println("There are 5 customers!");
      int in=1;
      int out = 1;
      while (out <= n) {
         int join = rand.nextInt(10)+1;
         if(join <= 5){
            int time = rand.nextInt(15)+1;
            System.out.println("The customer " + in + " arrived and service in " + time + " minutes");
            theQueue.insert(time);
            in++;
         }
         System.out.println("The customer " + out + " is serving");
         if(join > 5 && out<in){
            System.out.println("The customer " + out + " is served");
            theQueue.remove();
            out++;
         }
      }


      /*theQueue.insert(20); // insert items
      theQueue.insert(40);

      theQueue.displayQueue(); // display queue

      theQueue.insert(60); // insert items
      theQueue.insert(80);
      theQueue.insert(20);

      theQueue.displayQueue(); // display queue

      //theQueue.remove(); // remove items
      //theQueue.remove();

      theQueue.removeMultiple(20);

      theQueue.displayQueue(); // display queue*/
   }
}
