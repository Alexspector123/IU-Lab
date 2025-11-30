package Problem1.v;

public class Student
{
    public String fname, lname;
    public int grade;
    
    public Student(String fname, String lname, int grade)
    {
        this.fname = fname;
        this.lname = lname;
        this.grade = grade;
    }

    public String toString()
    {
        return fname + " " + lname + "\t" + grade;
    }
}
