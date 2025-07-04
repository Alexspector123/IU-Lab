import java.util.Scanner;
import java.lang.Math;
public class Point2D {
    private double x;
    private double y;
    public Point2D(){
        x = 0;
        y = 0;
    }
    public Point2D(int x, int y){
        this.x = x;
        this.y = y;
    }
    public Point2D(Point2D p){
        this.x = p.x;
        this.y = p.y;
    }
    public void input(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter X: ");
        x = sc.nextInt();
        System.out.println("Enter Y: ");
        y = sc.nextInt();
    }
    public String toString(){
        String s = "(";
        char a = (char) (x + '0');
        s = s+a;
        a = ',';
        s = s+a;
        a = (char) (y + '0');
        s = s+a;
        a = ')';
        s = s+a;
        return s;
    } 
    public void move(int x, int y){
        this.x = x;
        this.y = y;
    }
    public boolean isOrigin(){
        if (x == 0 && y == 0)
        return true;
        else return false;
    }
    public double distance(Point2D p){
        double p2X = p.x;
        double p2Y = p.y;
        return Math.sqrt((x-p2X)*(x-p2X)+(y-p2Y)*(y-p2Y));
    }
    public static double distance(Point2D p1, Point2D p2){
        return Math.sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));
    }
}
