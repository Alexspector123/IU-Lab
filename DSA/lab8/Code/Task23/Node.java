package Task23;

import java.util.ArrayList;

public class Node {

    public String name;
    public ArrayList<Edge> edge;
    boolean check;
    
    public Node(String name){
        this.name = name;
        edge = new ArrayList<>();
        check = false;
    }

    public void addEdge(Edge e){
        edge.add(e);
    }
}
