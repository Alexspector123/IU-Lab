package Project;

import java.text.SimpleDateFormat;

public class Main {
    public static void main(String[] args) throws Exception {
        Employee e1 = new Employee("01","Huy", 2000, 2, 3);
        Employee e2 = new Employee("02", "Phuong", 3000, 1, 2);
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Project p1 = new Project("A1", dateFormat.parse("10/05/2024"), dateFormat.parse("20/09/2024"));
        p1.listOfEmployee.add(e1);
        p1.listOfEmployee.add(e2);
        p1.toString();
        Double s = p1.estimateBudget();
        System.out.printf("Estimate Budget of project p1 is: %.2f",s);
    }
}
