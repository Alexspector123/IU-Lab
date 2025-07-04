package Shape.ShapeA;
public class Shape{
    private String color = "red";
    private boolean filled = true;
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
    public String toString(){
        String s = "A Shape with color of ";
        s += color;
        s += " and ";
        if(filled == true)
        s += "filled";
        else s += "Not filled";
        return s;
    }
}