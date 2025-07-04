import java.lang.Math;
public class Point{
    private double x;
    private double y;
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }
    public double distances(Point B){
        return Math.sqrt(Math.pow(x-B.x,2)+Math.pow(y-B.y,2));
    }
}