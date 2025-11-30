package Problem6;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;

public class main {
    public static void main(String[] args) throws ParseException {

        Scanner sc = new Scanner(System.in);
        DateFormat date = new SimpleDateFormat("hh:mm");

        int n;
        n = sc.nextInt();
        
        List list = new List(n);

        for(int i=0;i<n;i++){
            list.insert(sc.next(),date.parse(sc.next()), sc.nextInt());
        }

        System.out.println("Input the number of runways: ");
        list.setRunways(sc.nextInt());

        list.sort();
        list.display();
    }
}
