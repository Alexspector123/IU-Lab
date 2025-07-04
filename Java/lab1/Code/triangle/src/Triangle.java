public class Triangle {
    private double a;
    private double b;
    private double c;
    public double getA(){
        return this.a;
    }
    public double getB(){
        return this.b;
    }
    public double getC(){
        return this.c;
    }
    public Triangle(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public String verify(){
        if((a+b) <= c || (b+c) <= a || (c+a) <= b)
        return "Not triangle";
        else if (a==b && b==c)
        return "Equilateral Triangle";
        else if (a==b || b==c || c==a)
        return "Isosceles Triangle";
        else return "Scalene Triangle";
    }
}
