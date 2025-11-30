package Problem4;

import java.util.Scanner;

class Link {
   public int iData;
   public Link next; // next link in list
   // -------------------------------------------------------------

   public Link(int id) // constructor
   {
      iData = id;
   }

   // -------------------------------------------------------------
   public void displayLink() // display ourself
   {
      System.out.print("{" + iData + "} ");
   }
}

class LinkList {
   private Link first; // ref to first link on list
   private Link last;

   // -------------------------------------------------------------
   public LinkList() // constructor
   {
      first = null; // no links on list yet
      last = null;
   }

   // -------------------------------------------------------------
   public void insertFirst(int id) { // make new link
      Link newLink = new Link(id);
      newLink.next = first; // it points to old first link
      first = newLink; // now first points to this
      if(last == null){
         last = first;
      }
      last.next = first;
   }
   // -------------------------------------------------------------
   public void insertLast(int id) {
      Link newLink = new Link(id);
      if(first == null){
         insertFirst(id);
      }
      else{
         last.next = newLink;
         last = newLink;
         last.next = first;
      }
   }
   // -------------------------------------------------------------
   public int delete(int key) // delete link with given key
   { // (assumes non-empty list)
      Link current = first; // search for link
      Link previous = null;
      while (current.iData != key) {
            previous = current; // go to next link
            current = current.next;
      } // found it
      if (current == first){
         first = first.next;
         last.next = first;
      }
      else if(current == last){
         previous.next = last.next;
         last = previous;
      }
      else
         previous.next = current.next; // bypass it
      return current.iData;
   }
   // -------------------------------------------------------------
   public void displayList() // display the list
   {
      System.out.print("List (first-->last): ");
      Link current = first; // start at beginning of list
      while (current != last.next) // until end of list,
      {
         current.displayLink(); // print data
         current = current.next; // move to next link
      }
      System.out.println("");
   }
   // -------------------------------------------------------------
   public void elimination(int n, int k)
   {
      int noElems = n;
      Link current = first;
      int count = 1;
      System.out.print("Elimination order: ");
      while (noElems >= k) {
         if(count < k){
            count++;
            current = current.next;
         }
         else{
            System.out.print(delete(current.iData) + " ");
            current = current.next;
            noElems--;
            count = 1;
         }
      }
      current = first;
      while (noElems != 1) {
         System.out.print(delete(current.iData) + " ");
         current = current.next;
         noElems--;
      }
      System.out.println();
      System.out.println("Last person standing: " + current.iData);
   }
}

class Josephus {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      LinkList theList = new LinkList(); // make list

      int n, k, start;
      System.out.print("Enter the number of people in the circle: ");
      n = sc.nextInt();
      System.out.print("Enter the number used for counting off: ");
      k = sc.nextInt();
      System.out.print("Enter the number of the person where counting starts: ");
      start = sc.nextInt();
      for(int i=start;i<=n;i++){
         theList.insertLast(i);
      }
      for(int i=1;i<start;i++){
         theList.insertLast(i);
      }
      theList.elimination(n,k);
   }
}
