package Shape.ShapeA;
public class Main {
    public static void main(String[] args) throws Exception {
                Shape s1 = new Shape("red", true);
                System.out.println(s1);
        
                Circle c = new Circle();
                c.setRadius(5);
                System.out.println(c);
                System.out.println("\tArea: " + c.getArea());
                System.out.println("\tPerimeter: " + c.getPerimeter());
        
                Rectangle r = new Rectangle();
                r.setWidth(30);
                r.setLength(20);
                System.out.println(r);
                System.out.println("\tArea: " + r.getArea());
                System.out.println("\tPerimeter: " + r.getPerimeter());
        
                Square sq = new Square(10, "Yellow", false);
                System.out.println(sq);
                System.out.println("\tArea: " + sq.getArea());
                System.out.println("\tPerimeter: " + sq.getPerimeter());
    }
}
