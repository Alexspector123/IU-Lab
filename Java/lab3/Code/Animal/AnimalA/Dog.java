package Animal.AnimalA;
public class Dog extends Mammal{
    public Dog(String name){
        super(name);
    }
    public void greets(){
        System.out.println("Woof");
    }
    public void greets(Dog d){
        System.out.println("Woooof");
    }
    // @Override
    public String toString(){
        String s = "Dog[Mammal[Animal[name=";
        s += name;
        s += "]";
        s += "]";
        s += "]";
        return s;
    }
}