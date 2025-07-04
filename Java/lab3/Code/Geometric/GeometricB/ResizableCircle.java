package Geometric.GeometricB;
public class ResizableCircle extends Circle implements Resizable{

    public ResizableCircle(double radius){
        super(radius);
    }
    public String toString(){
        String s = "Resizable[Circle[radius=";
        s += radius;
        s += "]]";
        return s;
    }
    @Override
    public void resize(int percent) {
        radius *= percent/100.0;
    }
    
}
