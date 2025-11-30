package Problem3;

import java.util.Scanner;

public class sum {
    static int findsum(int[] a, int n){
        if(n==1)
            return a[0];
        return a[n-1] + findsum(a, n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(findsum(arr,5));
    }
}
