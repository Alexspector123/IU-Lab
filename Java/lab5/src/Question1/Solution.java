package Question1;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        for(int i=0;i<n;i++){
            arr.add(sc.nextInt());
        }
        int q = sc.nextInt();
        String s;
        for(int i=0;i<q;i++){
            sc.nextLine();
            s = sc.nextLine();
            if(s.equals("Insert")){
                int index, num;
                index = sc.nextInt();
                num = sc.nextInt();
                arr.add(index, num);
            }
            else if(s.equals("Delete")){
                int index;
                index = sc.nextInt();
                arr.remove(index);
            }
        }
        
    for(Integer a:arr){
        System.out.print(a+" ");
    }
    }
}
