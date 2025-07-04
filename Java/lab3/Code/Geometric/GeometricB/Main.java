package Geometric.GeometricB;
public class Main {
    public static void main(String[] args) throws Exception {
        Circle c1 = new Circle(4.5);
        System.out.println(c1);
         
        ResizableCircle c2 = new ResizableCircle(5.5);
        c2.resize(10);
        System.out.println(c2);
}
}
