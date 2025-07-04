package Question3;

public class MyClass {
    public static void main(String[] args) {
        int myArray[] = new int[7];
        // trying to access element 9
        try {
            System.out.println(myArray[9]);
        } catch (Exception e) {
            System.out.println("The element 9 does not exist!");
        }
    }
}
