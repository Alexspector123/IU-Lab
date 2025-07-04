//Complete this code or write your own from scratch
package Question2;
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh)
    {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        in.nextLine();
        Map<String, Integer> list = new HashMap<String,Integer>();
        for(int i=0;i<n;i++)
        {
            String name=in.nextLine(); 
            int phone= in.nextInt();
            list.put(name, phone);
            in.nextLine();
        }
        while(in.hasNext())
        {
            String s = in.nextLine();
            if(list.containsKey(s)){
                System.out.println(s+ "="+ list.get(s));
            }
            else{
                System.out.println("Not found");
            }
        }
        }
    }



