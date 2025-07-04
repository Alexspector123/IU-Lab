package Animal.AnimalB;
abstract class Animal{
    protected String name;
    public Animal(String name){
        this.name = name;
    }
    abstract void greets();
}