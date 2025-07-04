package Animal.AnimalB;
public class BigDog extends Dog{
    public BigDog(String name){
        super(name);
    }
    @Override
    public void greets(){
        System.out.println("Woow");
    }
    @Override
    public void greets(Dog d){
        System.out.println("Woooof");
    }
    public void greets(BigDog bd){
        System.out.println("Woooof");
    }
}
