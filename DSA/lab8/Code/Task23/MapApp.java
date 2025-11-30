package Task23;

public class MapApp {
    public static void main(String[] args) {
        Graph graph = new Graph();

        graph.addNode("A");
        graph.addNode("B");
        graph.addNode("C");
        graph.addNode("D");
        graph.addNode("E");
        graph.addNode("F");
        graph.addNode("G");
        graph.addNode("H");
        graph.addNode("I");
        graph.addNode("J");
        graph.addNode("K");
        graph.addNode("L");
        graph.addNode("M");

        graph.addEdge("A", "B", 15);
        graph.addEdge("B", "M", 20);
        graph.addEdge("B", "D", 13);
        graph.addEdge("D", "H", 11);
        graph.addEdge("K", "H", 12);
        graph.addEdge("M", "C", 20);
        graph.addEdge("M", "G", 9);
        graph.addEdge("C", "F", 12);
        graph.addEdge("H", "F", 10);
        graph.addEdge("H", "L", 14);
        graph.addEdge("G", "I", 19);
        graph.addEdge("L", "J", 10);
        graph.addEdge("A", "M", 18);
        graph.addEdge("B", "C", 8);
        graph.addEdge("D", "E", 20);
        graph.addEdge("D", "K", 13);
        graph.addEdge("K", "J", 14);
        graph.addEdge("M", "F", 14);
        graph.addEdge("C", "E", 18);
        graph.addEdge("E", "H", 11);
        graph.addEdge("H", "I", 8);
        graph.addEdge("F", "I", 15);
        graph.addEdge("I", "L", 17);

        graph.dijkstra("A", "K");
        graph.dijkstra("B", "L");
    }
}
