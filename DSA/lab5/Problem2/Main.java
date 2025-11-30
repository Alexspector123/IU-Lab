package Problem2;

import java.util.Scanner;

public class Main {
    static double sum(int n){
        if(n==1)
            return 1;
        return 1.0/n + sum(n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(sum(n));
    }
}
