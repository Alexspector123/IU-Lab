package Problem1.iv;

public class Car {
    private String name;
    private double miles;
    private double gallons;

    public Car(String name, double miles, double gallons){
        this.name = name;
        this.miles = miles;
        this.gallons = gallons;
    }
    public String getName(){
        return this.name;
    }
    public double getMiles(){
        return this.miles;
    }
    public double getGallons(){
        return this.gallons;
    }
    public double getMPS(){
        return miles/gallons;
    }

}