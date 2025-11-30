package Problem6;

import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class Flight {
    private String ID;
    private Date time;
    private int priority;

    public Flight(String ID, Date time, int priority){
        this.ID = ID;
        this.time = time;
        this.priority = priority;
    }
    public String getID(){
        return this.ID;
    }
    public Date getTime(){
        return this.time;
    }
    public int getPriority(){
        return this.priority;
    }
    
    @Override
    public String toString(){
        
        DateFormat date = new SimpleDateFormat("hh:mm");

        String s = "(";
        s += ID + date.format(time) + ")";
        return s;
    }
}

