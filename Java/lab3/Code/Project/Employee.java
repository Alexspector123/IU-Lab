package Project;
public class Employee implements Comparable<Employee> {

    private String employeeId;
    private String employeeName;
    private int salaryPerHour;
    private int noOfLeavingDay;
    private int noOfTravelDay;

    public String getEmployeeId(){
        return this.employeeId;
    }
    public void setEmployeeId(){
        this.employeeId = employeeId;
    }
    public String getEmployeeName(){
        return this.employeeName;
    }
    public void setEmployeeName(){
        this.employeeName = employeeName;
    }
    public int getSalaryPerHour(){
        return this.salaryPerHour;
    }
    public void setSalaryPerHour(){
        this.salaryPerHour = salaryPerHour;
    }
    public int getNoOfLeavingDay(){
        return this.noOfLeavingDay;
    }
    public void setNoOfLeavingDay(){
        this.noOfLeavingDay = noOfLeavingDay;
    }
    public int getNoOfTravelDay(){
        return this.noOfLeavingDay;
    }
    public void setNoOfTravelDay(){
        this.noOfTravelDay = noOfTravelDay;
    }
    public Employee(String employeeId, String employeeName, int salaryPerHour, int noOfLeavingDay, int noOfTravelDay)
    {
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.salaryPerHour = salaryPerHour;
        this.noOfLeavingDay = noOfLeavingDay;
        this.noOfTravelDay = noOfTravelDay;
    }
    public int calculateWeeklySalary(){
        return (salaryPerHour*8*(5-noOfLeavingDay + noOfTravelDay/2));
    }
    @Override
    public int compareTo(Employee e) {
        if (noOfTravelDay < e.noOfTravelDay)
        {
            return -1;
        }
        else if (noOfTravelDay == e.noOfTravelDay)
        {
            if (noOfLeavingDay > e.noOfLeavingDay)
               return -1;
        }
        return 0;
    }
    @Override
    public String toString(){
        String s="[Name: ";
        s += employeeName;
        s += " - Salary Per Hour: ";
        s += salaryPerHour;
        s += " - Weekly Salary: ";
        s += this.calculateWeeklySalary();
        s += "]";
        return s;
    }
}
