package Double;

class HashTable {
    private DataItem[] hashArray;
    private int arraySize;
    private DataItem nonItem;

    HashTable(int size) {
        arraySize = size;
        hashArray = new DataItem[arraySize];
        nonItem = new DataItem(-1);
    }

    public void displayTable() {
        System.out.print("Table: ");
        for (int j = 0; j < arraySize; j++) {
            if (hashArray[j] != null)
                System.out.print(hashArray[j].getKey() + " ");
            else
                System.out.print("** ");
        }
        System.out.println("");
    }
    public int hashFunc1(int key) {
        return key % arraySize;
    }

    public int hashFunc2(int key) {
        return 5 - key % 5;
    }

    public int insert(int key, DataItem item) {

        int hashVal = hashFunc1(key);
        int stepSize = hashFunc2(key);

        int probeLength = 0;
        while (hashArray[hashVal] != null && hashArray[hashVal].getKey() != -1){

            System.out.println("\tAlready having item at " + hashVal + " ,starting to jump");
            hashVal += stepSize;
            hashVal %= arraySize;
            System.out.println("\tAfter jumped " + stepSize + " steps, hashVal: " + hashVal);
            probeLength++;
        }
        hashArray[hashVal] = item;
        System.out.println("Inserted item at " + hashVal);
        System.out.println("Probe length for insert: " + probeLength);
        return probeLength;
    }

    public DataItem delete(int key) {
        int hashVal = hashFunc1(key);
        int stepSize = hashFunc2(key);
        while (hashArray[hashVal] != null) {
            if (hashArray[hashVal].getKey() == key) {
                DataItem temp = hashArray[hashVal];
                hashArray[hashVal] = nonItem;
                return temp;
            }
            hashVal += stepSize;
            hashVal %= arraySize;
        }
        return null;
    }

    public DataItem find(int key) {
        int hashVal = hashFunc1(key);
        int stepSize = hashFunc2(key);

        int probeLength = 0;

        while (hashArray[hashVal] != null) {
            if (hashArray[hashVal].getKey() == key){
                System.out.println("Probe length for find: " + probeLength);
                return hashArray[hashVal];
            }
            System.out.println(key + " is not at " + hashVal + ", jump to another");
            hashVal += stepSize;
            hashVal %= arraySize;
            System.out.println("\tAfter jumped " + stepSize + " steps, hashVal: " + hashVal);
            probeLength++;
        }
        System.out.println("Probe length for find: " + probeLength);
        return null;
    }
}