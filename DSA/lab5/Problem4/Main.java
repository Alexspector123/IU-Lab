package Problem4;

import java.util.Scanner;

public class Main {
    static int gcd(int p, int q){
        if(q==0)
        return p;
        return gcd(q,p%q);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        System.out.println(gcd(m, n));
    }
}
