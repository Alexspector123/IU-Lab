public class Staff extends Person {
    String school;
    double pay;
    public Staff(String name, String address, String school, double pay){
        super(name, address);
        this.school = school;
        this.pay = pay;
    }
    public String getSchool(){
        return this.school;
    }
    public void setSchool(String school)
    {
        this.school = school;
    }
    public double getPay(){
        return this.pay;
    }
    public void setPay(double pay)
    {
        this.pay = pay;
    }
    public String toString(){
        String s = "Staff[Person[name = ";
        s = s + this.getName();
        String a = ", address = ";
        s = s + a;
        s = s + this.getAddress();
        a = ", school = ";
        s = s + a;
        s = s + school;
        a = ", pay = ";
        s = s + a;
        s = s + String.valueOf(pay);
        a = "]";
        s = s + a;
        return s;
    }
}
