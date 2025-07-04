package Animal.AnimalA;

public class Animal{
    protected String name;
    public Animal(String name){
        this.name = name;
    }
    public String toString(){
        String s = "Animal[name=";
        s += name;
        s += "]";
        return s;
    }
}