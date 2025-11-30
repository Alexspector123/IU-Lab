package Problem5;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main{

    static void subset(int[] arr, int index, List<Integer> sub){
        if(index == arr.length){
            System.out.println(sub);
            return;
        }
        subset(arr, index+1, sub);

        sub.add(arr[index]);
        subset(arr, index+1, sub);

        sub.remove(sub.size()-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        List<Integer> sub = new ArrayList<>();
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        subset(arr, 0,sub);
    }
}