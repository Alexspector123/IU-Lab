package Project;
import java.util.*;

public class Project {
    private String projectId;
    private Date startDate;
    private Date endDate;
    ArrayList<Employee> listOfEmployee;

    public String getProjectId(){
        return this.projectId;
    }
    public void setProjectId(String projectId){
        this.projectId = projectId;
    }
    public Date getStartDate(){
        return this.startDate;
    }
    public void setStartDate(Date startDate){
        this.startDate = startDate;
    }
    public Date getEndDate(){
        return this.endDate;
    }
    public void setEndDate(Date endDate){
        this.endDate = endDate;
    }
    public Project(String projectId, Date startDate, Date endDate){
        this.projectId = projectId;
        this.startDate = startDate;
        this.endDate = endDate;
        listOfEmployee = new ArrayList<Employee>();
    }
    public Double estimateBudget(){
        int day = (int) ((endDate.getTime() - startDate.getTime())/(1000*60*60*24));
        double budget = 0;
        for(Employee e : listOfEmployee)
        {
            budget += e.getSalaryPerHour() * 24 * day;
        }
        return budget;
    }
    @Override
    public String toString(){
        Collections.sort(listOfEmployee);
        listOfEmployee.forEach(System.out::println);
        String s = "";
        return s;
    }
}

