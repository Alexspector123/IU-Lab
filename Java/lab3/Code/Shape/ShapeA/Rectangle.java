package Shape.ShapeA;
public class Rectangle extends Shape {
    private double width = 1.0;
    private double length = 1.0;

    public Rectangle(){
        this.width = 1.0;
        this.length = 1.0;
    }
    public Rectangle(double width, double length){
        this.width = width;
        this.length = length;
    }
    public Rectangle(double width, double length, String color, boolean filled){
        super(color,filled);
        this.width = width;
        this.length = length;
    }
    public double getWidth(){
        return this.width;
    }
    public void setWidth(double width){
        this.width = width;
    }
    public double getLength(){
        return this.length;
    }
    public void setLength(double length){
        this.length = length;
    }
    public double getArea(){
        return (length*width);
    }
    public double getPerimeter(){
        return ((width + length)*2);
    }
    // @Override
    public String toString(){
        String s = "A Rectangle with width=";
        s += width;
        s += " and length=";
        s += length;
        s += ", which is a subclass of ";
        s += super.toString();
        return s;
    }
}
