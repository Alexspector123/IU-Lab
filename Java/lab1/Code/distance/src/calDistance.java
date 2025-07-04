import java.util.Scanner;
public class calDistance {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first point x and y: ");
        double x = sc.nextDouble();
        double y = sc.nextDouble();
        Point A = new Point(x, y);
        System.out.println("Enter the second point x and y: ");
        x = sc.nextDouble();
        y = sc.nextDouble();
        Point B = new Point(x, y);
        System.out.print("The distance of two points is: ");
        System.out.format("%.2f",A.distances(B));
}
}
