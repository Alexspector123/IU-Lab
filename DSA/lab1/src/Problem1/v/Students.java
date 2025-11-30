package Problem1.v;

import java.util.Scanner;
import java.io.*;

public class Students
{
    public static void main (String[] args) throws IOException
    {   String first_name, last_name;
        int grade, total=0, count=0;
        double average;
        Scanner fileInput = new Scanner(new File("src/Problem1/v/students.txt"));
        while (fileInput.hasNext())
        {
            first_name = fileInput.next();
            last_name = fileInput.next();
            grade = fileInput.nextInt();
            
            Student st = new Student(first_name, last_name, grade);
            
            System.out.println(st);
            total = total + grade; 
            count++;
        }
        average = (double)total/count;
        System.out.println("There are " + count + " students with average grade " + average);

        /*String first_name, last_name;
        int grade, totalExcellent=0, totalOk=0, totalFailure=0, excellentCount=0, okCount=0, failureCount=0, totalGrade=0, count=0;
        Scanner fileInput = new Scanner(new File("src/Problem1/v/students.txt"));
        for(; fileInput.hasNext(); ){
            first_name = fileInput.next();
            last_name = fileInput.next();
            grade = fileInput.nextInt();
            
            Student st = new Student(first_name, last_name, grade);
            
            if(st.grade > 89){
                totalExcellent += grade;
                System.out.println(st.lname + ": excellent");
                excellentCount++;
            }
            else if (st.grade >= 60 && st.grade <= 89){
                totalOk += grade;
                System.out.println(st.lname + ": ok");
                okCount++;
            }
            else{
                totalFailure += grade;
                System.out.println(st.lname + ": failure");
                failureCount++;
            }
            totalGrade += grade;
            count++;
        }
        
        System.out.println("There are " + count + " students with average grade: " + (double)(totalGrade/count));
        System.out.println("There are " + excellentCount + " students with average excellent grade: " + (double)(totalExcellent/excellentCount));
        System.out.println("There are " + okCount + " students with average excellent grade: " + (double)(totalOk/okCount));
        System.out.println("There are " + failureCount + " students with average excellent grade: " + (double)(totalFailure/failureCount)); */
        
    }
}
