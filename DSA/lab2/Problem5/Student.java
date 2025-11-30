package Problem5;

public class Student {

    private String fname;
    private String lname;
    private double grade;

    public Student(String fname, String lname, double grade){
        this.fname = fname;
        this.lname = lname;
        this.grade = grade;
    }

    public String getFname(){
        return this.fname;
    }
    public String getLname(){
        return this.lname;
    }
    public double GetGrade(){
        return this.grade;
    }
    @Override
    public String toString(){
        String s = "(";
        s += fname + ", " + lname + ", " + grade + ")";
        return s;
    }
}

