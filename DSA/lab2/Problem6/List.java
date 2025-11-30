package Problem6;

import java.util.Date;

import Problem5.Student;

public class List {
    private Flight[] fl;
    private int nElems;
    private int runways;

    public List(int max)
    {
        fl = new Flight[max];
        nElems = 0;
    }
    public void setRunways(int runways){
        this.runways = runways;
    }
    public int getRunways(){
        return this.runways;
    }

    public void insert(String ID, Date time, int priority)
    {
        fl[nElems] = new Flight(ID, time, priority);
        nElems++;
    }
    public void display()
    {
        int n = 1;
        while (n <= getRunways()){
            System.out.print("Runways "+n+": ");
            for(int i=0; i<nElems; i++){
                if((i>0 && fl[i].getTime().compareTo(fl[i-1].getTime())==0) || 
                (i<nElems-1 && fl[i].getTime().compareTo(fl[i+1].getTime())==0)){
                    if(fl[i].getPriority() == n){
                        System.out.print(fl[i].toString() + ", ");
                    }
                }
                else if(n==1){
                    System.out.print(fl[i].toString() + ", ");
                }
            }
            System.out.println("");
            n++;
        }
    }
    public void sort(){
        for(int i=0; i<nElems-1; i++){
            for(int j=i+1; j<nElems; j++){
                if(fl[i].getPriority() > fl[j].getPriority()){
                    swap(i, j);
                }
            }
        }
        for(int i=0; i<nElems-1; i++){
            for(int j=i+1; j<nElems; j++){
                if(fl[i].getTime().compareTo(fl[j].getTime()) > 0){
                    swap(i, j);
                }
            }
        }
    }
    public void swap(int i, int j){
        Flight temp = fl[i];
        fl[i] = fl[j];
        fl[j] = temp;
   }
}
