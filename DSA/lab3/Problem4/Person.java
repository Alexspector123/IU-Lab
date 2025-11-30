package Problem4;

public class Person {

    private String Fname;
    private String Lname;

    public Person(String Fname, String Lname){
        this.Fname = Fname;
        this.Lname = Lname;
    }

    @Override
    public String toString(){
        String s = Fname + " " + Lname;
        return s;
    }
}
