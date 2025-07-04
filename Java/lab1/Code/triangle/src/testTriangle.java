import java.util.Scanner;
public class testTriangle {
    public static void main(String[] args){
        System.out.println("Please enter 3 numbers for the sides of a triangle: ");
        Scanner sc = new Scanner(System.in);
        double a,b,c;
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        Triangle t = new Triangle(a, b, c);
        System.out.println(t.verify());
    }
}
