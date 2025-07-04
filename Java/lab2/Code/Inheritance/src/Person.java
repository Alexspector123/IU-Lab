public class Person{
    private String name;
    private String address;
    public Person(String name, String address){
        this.name = name;
        this.address = address;
    }
    public String getName(){
        return this.name;
    }
    public String getAddress(){
        return this.address;
    }
    public void setAddress(String address){
        this.address = address;
    }
    public String toString(){
        String s = "Person[name = ";
        s = s + name;
        String a = ", address = ";
        s = s + a;
        s = s + address;
        a = "]";
        s = s + a;
        return s;
    }
    
}