package Task23;
public class Edge {

    public Node node1;
    public Node node2;

    public int weight;

    public Edge(Node node1, Node node2, int weight){
        this.node1 = node1;
        this.node2 = node2;
        this.weight = weight;
    }
}