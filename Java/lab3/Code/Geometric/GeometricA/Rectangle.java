package Geometric.GeometricA;
public class Rectangle implements GeometricObject {
    private double width;
    private double length;
    public Rectangle(double width, double length){
        this.width = width;
        this.length = length;
    }
    public String toString(){
        String s = "Circle[radius=";
        s += width;
        s += ", length=";
        s += length;
        s += "]";
        return s;
    }
    @Override
    public double getPerimeter() {
        return (width*length);
    }

    @Override
    public double getArea() {
        return (width*length);
    }
    
}
