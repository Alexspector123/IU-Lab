package Problem3;

import java.util.Scanner;

public class min {
    static int findmin(int[] a, int n){
        if(n==1)
            return a[0];
        return Math.min(a[n-1], findmin(a, n-1));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(findmin(arr,n));
    }
}
