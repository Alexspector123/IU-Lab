package Problem1.i;

import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        System.out.println("Input the number of element: ");
        int n;
        n = scan.nextInt();
        int[] a = new int[n];
        System.out.println("Input the element of array: ");
        for(int i=0;i<4;i++){
            a[i] = scan.nextInt();
        }
        int number = 0;
        for(int i=0;i<4;i++){
            number = number*10 + a[i];
        }
        System.out.println("The number is: ");
        System.out.println(number);
    }
}
