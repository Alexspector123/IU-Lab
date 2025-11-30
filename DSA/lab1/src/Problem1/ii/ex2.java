package Problem1.ii;

import java.util.Scanner;

public class ex2 {
    public static void main(String[] args) throws Exception {

        Scanner scan = new Scanner(System.in);

        int n;
        System.out.println("Input the number of element: ");
        n = scan.nextInt();

        int[] a = new int[n];
        System.out.println("Input the element of array: ");
        for(int i=0;i<n;i++){
            a[i] = scan.nextInt();
        }

        System.out.println("The median of the array: " + a[n/2]);
    }
}
