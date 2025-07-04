package Geometric.GeometricB;
public class Circle implements GeometricObject {
    protected double radius;
    private final static double pi = 3.14;
    public Circle(double radius){
        this.radius = radius;
    }
    public String toString(){
        String s = "Circle[radius=";
        s += radius;
        s += "]";
        return s;
    }
    @Override
    public double getPerimeter() {
        return (radius*2*pi);
    }

    @Override
    public double getArea() {
        return (radius*radius*pi);
    }
    
}
