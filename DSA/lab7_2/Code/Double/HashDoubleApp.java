package Double;
import java.io.*;

class HashDoubleApp {
    public static void main(String[] args) throws IOException {
        int aKey;
        DataItem aDataItem;
        int n;
        int primeSize = 13, nonPrimeSize = 14;
        int totalProbeLengthPrime = 0, totalProbeLengthNonPrime = 0;
        double averageProbeLengthPrime = 0.0, averageProbeLengthNonPrime = 0.0;
        double loadFactor;

        // get sizes
        System.out.print("Enter initial number of items: ");
        n = getInt();

        // make table
        HashTable primeTable = new HashTable(primeSize);
        HashTable nonPrimeTable = new HashTable(nonPrimeSize);

        for (int j = 0; j < n; j++) {
            aKey = (int) (java.lang.Math.random() * 2 * primeSize);
            aDataItem = new DataItem(aKey);
            totalProbeLengthPrime += primeTable.insert(aKey, aDataItem);
            totalProbeLengthNonPrime += nonPrimeTable.insert(aKey, aDataItem);
        }
        averageProbeLengthPrime = (double) totalProbeLengthPrime/n;
        averageProbeLengthNonPrime = (double) totalProbeLengthNonPrime/n;
        System.out.println("Prime table size: " + primeSize);
        System.out.println("Average probe length for prime size: " + averageProbeLengthPrime);
        System.out.println("Non-prime table size: " + nonPrimeSize);
        System.out.println("Average probe length for non-prime size: " + averageProbeLengthNonPrime);
        
    }

    public static String getString() throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        String s = br.readLine();
        return s;
    }

    public static char getChar() throws IOException {
        String s = getString();
        return s.charAt(0);
    }

    public static int getInt() throws IOException {
        String s = getString();
        return Integer.parseInt(s);
    }
}