import java.util.ArrayList;

public class Management {
    public static void main(String[] args) {
        Student student = new Student("Thanh Huy", "Anderson", "Computer Science", 2, 2646100.123);
        Staff staff = new Staff("Dong Phuong", "Nolan", "Gottingen", 2646100.123);
        System.out.println("Student's information: "+student.toString());
        System.out.println("Staff's information: "+staff.toString());
    }
}
