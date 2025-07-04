package Shape.ShapeA;
public class Circle extends Shape{
    private double radius = 1.0;

    public Circle(){
        this.radius = 1.0;
    }
    public Circle(double radius){
        this.radius = radius;
    }
    public Circle(double radius, String color, boolean filled){
        super(color, filled);
        this.radius = radius;
    }
    public double getRadius(){
        return this.radius;
    }
    public void setRadius(double radius){
        this.radius = radius;
    }
    public double getArea(){
        return (radius*radius*3.14);
    }
    public double getPerimeter(){
        return (radius*2*3.14);
    }
    // @Override
    public String toString(){
        String s = "A Circle with radius=";
        s += radius;
        s += ", which is a subclass of ";
        s += super.toString();
        return s;
    }
}
