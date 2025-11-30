package Problem1;

import java.util.*;

public class SimpleStack {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();

        int n;
        System.out.print("Input the Dec number: ");
        n = sc.nextInt();

        while (n > 0) {
            stack1.push(n);
            n/=8;
        }
        for(int i=0; i<stack1.size(); i++){
            stack2.push(stack1.get(i)%8);
        }
        System.out.print("The Octal number: ");
        while (!stack2.isEmpty()) {
            System.out.print(stack2.pop());
        }
    }
}

