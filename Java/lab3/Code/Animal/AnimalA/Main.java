package Animal.AnimalA;
public class Main {
    public static void main(String[] args) throws Exception {
        Dog dog1 = new Dog("Ein");
        Cat cat1 = new Cat("Yukichi");
        Dog dog2 = new Dog("Bond");
        System.out.println(cat1);
        System.out.println(dog1);
        System.out.println(dog2);
        dog1.greets();
        cat1.greets();
        dog2.greets(dog1);
    }
}
