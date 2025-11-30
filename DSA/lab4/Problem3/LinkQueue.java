package Problem3;

class LinkQueue {
    private FirstLastList theList;
    private int noElems;

    // --------------------------------------------------------------
    public LinkQueue() // constructor
    {
        theList = new FirstLastList();
        noElems = 0;
    } // make a 2-ended list
    // --------------------------------------------------------------

    public boolean isEmpty() // true if queue is empty
    {
        return theList.isEmpty();
    }

    // --------------------------------------------------------------
    public void insert(long j) // insert, rear of queue
    {
        theList.insertLast(j);
        noElems++;
    }

    // --------------------------------------------------------------
    public long remove() // remove, front of queue
    {
        noElems--;
        return theList.deleteFirst();
    }

    // --------------------------------------------------------------
    public void displayQueue() {
        System.out.print("Queue (front-->rear): ");
        theList.displayList();
    }
    // --------------------------------------------------------------
    public void removeMultiple(long n){
        theList.deleteMultiple(n);
        return;
    }    // --------------------------------------------------------------
    public int size(){
        return noElems;
    }
}
