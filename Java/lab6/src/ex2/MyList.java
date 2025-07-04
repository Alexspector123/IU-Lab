package ex2;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> {

    private List<T> list;
    public MyList(){
        list = new ArrayList<>();
    }
    public void add(T value){
        list.add(value);
    }
    public void remove(T value){
        list.remove(value);    
    }
}