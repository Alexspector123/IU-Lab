package Shape.ShapeB;
public class Circle extends Shape{
    private double radius;

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
    // @Override
    public double getArea(){
        return (radius*radius*3.14);
    }
    // @Override
    public double getPerimeter(){
        return (radius*2*3.14);
    }
    // @Override
    public String toString(){
        String s = "A Circle with radius=";
        s += radius;
        s += ", which is a subclass of ";
        super.toString();
        return s;
    }
}
