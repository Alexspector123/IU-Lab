import java.lang.Math;
public class Triangle {
    private Point2D p1;
    private Point2D p2;
    private Point2D p3;
    public Triangle(Point2D p1, Point2D p2, Point2D p3){
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }
    public double perimeter(){
        return (Point2D.distance(p1,p2)+Point2D.distance(p2,p3)+Point2D.distance(p1,p3));
    }
    public double area(){
        double a = Point2D.distance(p1,p2);
        double b = Point2D.distance(p2,p3);
        double c = Point2D.distance(p1,p3);
        double s = (a+b+c)/2;
        return Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }
}
