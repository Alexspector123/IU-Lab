package Shape.ShapeB;
abstract class Shape{
    protected String color;
    protected boolean filled = true;
    public Shape(){
        this.color = "green";
        this.filled = true;
    }
    public Shape(String color, boolean filled){
        this.color = color;
        this.filled = filled;
    }
    public String getColor(){
        return this.color;
    }
    public void setColor(){
        this.color = color;
    }
    public boolean isFilled(){
        return this.filled;
    }
    public void setFilled(){
        this.filled = filled;
    }
    public abstract double getArea();
    public abstract double getPerimeter();
    public String toString(){
        String s = "A Shape with color of ";
        s += color;
        s += "and ";
        if(filled == true)
        s += "filled";
        else s += "Not filled";
        return s;
    }
}