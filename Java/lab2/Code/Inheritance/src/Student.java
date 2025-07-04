public class Student extends Person {
    private String program;
    private int year;
    private double fee;

    public Student(String name, String address, String program, int year, double fee){
        super(name, address);
        this.program = program;
        this.year = year;
        this.fee = fee;
    }
    public String getProgram(){
        return this.program;
    }
    public void setProgram(String program)
    {
        this.program = program;
    }
    public int getYear(){
        return this.year;
    }
    public void setYear(int year)
    {
        this.year = year;
    }
    public double getFee(){
        return this.fee;
    }
    public void setFee(double fee)
    {
        this.fee = fee;
    }
    public String toString(){
        String s = "Student[Person[name = ";
        s = s + this.getName();
        String a = ", address = ";
        s = s + a;
        s = s + this.getAddress();
        a = ", program = ";
        s = s + a;
        s = s + program;
        a = ", year = ";
        s = s + a;
        s = s + String.valueOf(year);
        a = ", fee = ";
        s = s + a;
        s = s + String.valueOf(fee);
        a = "]";
        s = s + a;
        return s;
    }
}
