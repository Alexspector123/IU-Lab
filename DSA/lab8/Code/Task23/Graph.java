package Task23;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;

public class Graph {

    public Map<String, Node> nodes;

    public Graph() {
        nodes = new HashMap<>();
    }

    public void addNode(String s) {
        Node node = new Node(s);
        nodes.put(s, node);
    }

    public void addEdge(String s1, String s2, int weight) {
        Node node1 = new Node(s1);
        Node node2 = new Node(s2);

        if (node1 == null || node2 == null) {
            System.out.println("Both nodes must exist before adding an edge");
        } else {
            Edge edge = new Edge(node1, node2, weight);
            node1.addEdge(edge);
            node2.addEdge(edge);
        }
    }

    private int countPath(Node start, Node end) {
        if (start == end) {
            return 1;
        }
        start.check = true;
        int totalPath = 0;
        Node next;
        for (Edge edge : start.edge) {
            if (edge.node1 == start) {
                next = edge.node2;
            } else {
                next = edge.node1;
            }
            if (!next.check) {
                totalPath += countPath(next, end);
            }
        }
        start.check = false;
        return totalPath;
    }

    public void reset() {
        for (Node node : nodes.values()) {
            node.check = false;
        }
    }

    public void DFS(String s, String e) {
        reset();
        Stack<String> path = new Stack<>();
        Stack<Node> st = new Stack<>();

        Node start = nodes.get(s);
        Node end = nodes.get(e);
        Node current = start;

        int size;
        Node next, node1, node2;

        while (current != end) {
            next = null;
            if (!current.check) {
                path.add(current.name);
                st.add(current);
                current.check = true;
            }
            size = current.edge.size();
            for (int i = 0; i < size; i++) {
                node1 = current.edge.get(i).node1;
                node2 = current.edge.get(i).node2;
                if (node1 != current && !node1.check) {
                    next = node1;
                    break;
                }
                if (node2 != current && !node2.check) {
                    next = node2;
                    break;
                }
            }
            if (next == null) {
                if (!st.isEmpty()) {
                    current = st.pop();
                    path.pop();
                } else {
                    System.out.println("Don't have any path!");
                    return;
                }
            } else {
                current = next;
            }
        }
        path.add(e);
        System.out.println("Longest path from " + start.name + " to " + end.name + "is: " + path);
    }

    public void BFS(String s, String e) {

        reset();

        Node start = nodes.get(s);
        Node end = nodes.get(e);
        Node current = start;

        LinkedList<String> path = new LinkedList<>();
        HashMap<Node, Node> hashmap = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();

        queue.add(current);
        current.check = true;

        int size;
        Node node1, node2, node3;

        while (!queue.isEmpty()) {
            current = queue.poll();
            size = current.edge.size();
            node3 = null;
            for (int i = 0; i < size; i++) {
                node1 = current.edge.get(i).node1;
                node2 = current.edge.get(i).node2;
                if (node1 != current && !node1.check) {
                    node1.check = true;
                    queue.add(node1);
                    hashmap.put(node1, current);
                    node3 = node1;
                }
                if (node2 != current && !node2.check) {
                    node2.check = true;
                    queue.add(node2);
                    hashmap.put(node2, current);
                    node3 = node2;
                }
            }
            if (node3 == end) {
                current = node3;
                break;
            }
        }

        while (current != start) {
            node3 = hashmap.get(current);
            path.addFirst(current.name);
            current = node3;
        }

        path.addFirst(start.name);

        System.out.println("Shortest path from " + start.name + " to " + end.name + " is: " + path);
    }
    public void dijkstra(String s, String e){
        reset();

        HashMap<String, String> parent = new HashMap<>();
        HashMap<String, Integer> distance = new HashMap<>();
        HashMap<String, String> path = new HashMap<>();

        Node start = nodes.get(s);
        Node end = nodes.get(e);
        Node current = start;

        distance.put(s,0);
        start.check = true;

        while (true) {
            int min = Integer.MAX_VALUE;
            String key = null;

            for(Edge edge : current.edge){
                Node neighbor = (edge.node1 != current) ? edge.node1 : edge.node2;
                if(neighbor.check) continue;

                int newDist = distance.get(current.name) + edge.weight;

                if(!distance.containsKey(neighbor.name) || newDist < distance.get(neighbor.name)){
                    distance.put(neighbor.name, newDist);
                    parent.put(neighbor.name, current.name);
                }
            }
            for(Map.Entry<String, Integer> entry : distance.entrySet()){
                if(!nodes.get(entry.getKey()).check && entry.getValue() < min){
                    min = entry.getValue();
                    key = entry.getKey();
                }
            }
            
            if(key == null) break;
                current = nodes.get(key);
                current.check = true;
                path.put(key, parent.get(key));
            
            if(current == end) break;
        }
        LinkedList<String> way = new LinkedList<>();

        while (current != start) {
            way.addFirst(current.name);
            current = nodes.get(path.get(current.name));
        }
        way.addFirst(start.name);
        System.out.println("Shortest path from " + start.name + " to " + end.name + " is: " + way);
    }
}
