package Animal.AnimalA;
public class Mammal extends Animal{
    public Mammal(String name){
        super(name);
    }
    // @Override
    public String toString(){
        String s = "Mammal[Animal[name=";
        s += name;
        s += "]";
        s += "]";
        return s;
    }
}
