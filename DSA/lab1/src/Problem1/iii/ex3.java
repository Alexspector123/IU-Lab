package Problem1.iii;

import java.util.Scanner;

public class ex3 {
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
        System.out.println("The smallest gap is: " + minGap(a,n));
    }

    static int minGap(int[] array, int element){
        int gap;
        if(element < 2)
            return 0;
        else{
            gap = array[1] - array[0];
            for(int i=2;i<element;i++){
                if(array[i]-array[i-1] < gap){
                    gap = array[i]-array[i-1];
                }
            }
            return gap;
        }
    }
}
