package Animal.AnimalB;
public class Main {

    public static void main(String[] args) throws Exception {
        Dog dog1 = new Dog("Ein");
        Cat cat1 = new Cat("Yukichi");
        Dog dog2 = new Dog("Kuro");
        BigDog bd1 = new BigDog("Sadamaru");
        BigDog bd2 = new BigDog("Bond");
        System.out.println(dog1);
        System.out.println(cat1);
        System.out.println(dog2);
        dog1.greets();
        cat1.greets();
        dog2.greets();
        bd1.greets();
        bd1.greets(bd2);
        bd2.greets();
        bd2.greets(bd1);

    }
}
