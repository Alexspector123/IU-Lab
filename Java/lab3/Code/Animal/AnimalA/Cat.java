package Animal.AnimalA;
public class Cat extends Mammal{
        public Cat(String name){
            super(name);
        }
        public void greets(){
            System.out.println("Meow");
        }
        // @Override
        public String toString(){
            String s = "Cat[Mammal[Animal[name=";
            s += name;
            s += "]";
            s += "]";
            s += "]";
            return s;
        }
}