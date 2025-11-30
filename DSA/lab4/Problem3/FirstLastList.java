package Problem3;

class FirstLastList {
    private Link first; // ref to first item
    private Link last; // ref to last item
    // -------------------------------------------------------------

    public FirstLastList() // constructor
    {
        first = null; // no items on list yet
        last = null;
    }

    // -------------------------------------------------------------
    public boolean isEmpty() // true if no links
    {
        return first == null;
    }

    // -------------------------------------------------------------
    public void insertLast(long dd) // insert at end of list
    {
        Link newLink = new Link(dd); // make new link
        if (isEmpty()) // if empty list,
            first = newLink; // first --> newLink
        else
            last.next = newLink; // old last --> newLink
        last = newLink; // newLink <-- last
    }

    // -------------------------------------------------------------
    public long deleteFirst() // delete first link
    { // (assumes non-empty list)
        long temp = first.dData;
        if (first.next == null) // if only one item
            last = null; // null <-- last
        first = first.next; // first --> old next
        return temp;
    }

    // -------------------------------------------------------------
    public void displayList() {
        Link current = first; // start at beginning
        while (current != null) // until end of list,
        {
            current.displayLink(); // print data
            current = current.next; // move to next link
        }
        System.out.println("");
    }

    // -------------------------------------------------------------
    public void deleteMultiple(long n) {
        Link current = first;
        Link previous = null;
        while (current != null) {
            if(current.dData == n){
                if(current == first) deleteFirst();
                else if(current == last){
                    previous.next = null;
                    last = previous;
                }
                else{
                    previous.next = current.next;
                    current = current.next;
                }
            }
            previous = current;
            current = current.next;
        }
    }
}
