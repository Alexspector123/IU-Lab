package Problem1;
// -------------------------------------------------------------

// Representing arithmetic expressions by binary tree
// CS 501 
// Zdravko Markov
// -------------------------------------------------------------

import java.util.LinkedList;
import java.util.Queue;

class Tree {

   private Node root;

   public Tree(Node root) {
      this.root = root;
   }

   public static void main(String[] args) {

      Node a = node(2);
      Node b = node(3);
      Node c = node('+', a, b);
      Node d = node(5);
      Node e = node(1);
      Node f = node('-', d, e);
      Node g = node('*', c, f);
      Node h = node(8);
      Node i = node('/', g, h);

      Node j = node(2);
      Node k = node(3);
      Node l = node('+', j, k);
      Node m = node(5);
      Node n = node(1);
      Node o = node('-', m, n);
      Node p = node('*', l, o);
      Node q = node(8);
      Node r = node('/', p, q);

      Tree tree = new Tree(i);
      Tree tree2 = new Tree(r);

      // Node i =
      // node('/',node('*',node('+',node(2),node(3)),node('-',node(5),node(1))),node(8));

      System.out.println("Tree:");
      showTree(0, i);
      System.out.print("Prefix: ");
      prefix(i);
      System.out.print("\nPostfix: ");
      postfix(i);
      System.out.print("\nInfix: ");
      infix(i);
      System.out.println("\nCount elements: " + tree.countNElems());
      System.out.println("\nCount height: " + tree.countHeight());
      System.out.println("\nCount height: " + tree.countLeaves());
      if(tree.isBalanced()){
         System.out.println("It is balanced!");
      }
      else{
         System.out.println("It is unbalanced!");
      }
      if(tree.isIdentical(tree2)){
         System.out.println("It is Identical!");
      }
      else{
         System.out.println("It is not Identical!");
      }
   }

   // -------------------------------------------------------------
   public static Node node(char op, Node l, Node r) {
      Node a = new Node();
      a.leftChild = l;
      a.rightChild = r;
      return a;
   }

   // -------------------------------------------------------------
   public static Node node(int val) {
      Node a = new Node();
      a.value = val;
      return a;
   }

   // -------------------------------------------------------------
   public static void prefix(Node t) {
      
      if (t.leftChild == null && t.rightChild == null)
         System.out.print(t.value + " ");
      else {
         prefix(t.leftChild);
         prefix(t.rightChild);
      }
   }

   // -------------------------------------------------------------
   public static void postfix(Node t) {
      if (t.leftChild == null && t.rightChild == null)
         System.out.print(t.value + " ");
      else {
         postfix(t.leftChild);
         postfix(t.rightChild);
      }
   }

   // -------------------------------------------------------------
   public static void infix(Node t) {
      if (t.leftChild == null && t.rightChild == null)
         System.out.print(t.value);
      else {
         System.out.print("(");
         infix(t.leftChild);
         infix(t.rightChild);
         System.out.print(")");
      }
   }


   // -------------------------------------------------------------
   public static void showTree(int n, Node t) {
      tab(n);
      if (t.leftChild == null && t.rightChild == null)
         System.out.println(t.value);
      else {
         showTree(n + 2, t.leftChild);
         showTree(n + 2, t.rightChild);
      }
   }

   // -------------------------------------------------------------
   public static void tab(int n) {
      for (int i = 0; i < n; i++)
         System.out.print(" ");
   }

   // -------------------------------------------------------------
   public int countNElems() {
      if (root == null) {
         return 0;
      }
      int count = 0;
      Queue<Node> queue = new LinkedList<>();
      queue.offer(root);

      while (!queue.isEmpty()) {
         Node current = queue.poll();
         count++;

         if (current.leftChild != null) {
            queue.offer(current.leftChild);
         }
         if (current.rightChild != null) {
            queue.offer(current.rightChild);
         }
      }
      return count;
   }
   // -------------------------------------------------------------
   public int countHeight() {
      if (root == null) {
         return 0;
      }
      int count = 0;
      Queue<Node> queue = new LinkedList<>();
      queue.offer(root);

      while (!queue.isEmpty()) {
         int levelSize = queue.size();
         for (int i = 0; i < levelSize; i++) {
            Node current = queue.poll();

            if (current.leftChild != null) {
               queue.offer(current.leftChild);
            }
            if (current.rightChild != null) {
               queue.offer(current.rightChild);
            }
         }
         count++;
      }
      return count;
   }

   // -------------------------------------------------------------
   public int countLeaves() {
      if (root == null) {
         return 0;
      }
      int count = 0;
      Queue<Node> queue = new LinkedList<>();
      queue.offer(root);

      while (!queue.isEmpty()) {
         Node current = queue.poll();
         if (current.leftChild == null && current.leftChild == null)
            count++;

         if (current.leftChild != null) {
            queue.offer(current.leftChild);
         }
         if (current.rightChild != null) {
            queue.offer(current.rightChild);
         }
      }
      return count;
   }
   // -------------------------------------------------------------
   public int countHeightWithNode(Node root) {
      if (root == null) {
         return 0;
      }
      int count = 0;
      Queue<Node> queue = new LinkedList<>();
      queue.offer(root);

      while (!queue.isEmpty()) {
         int levelSize = queue.size();
         for (int i = 0; i < levelSize; i++) {
            Node current = queue.poll();

            if (current.leftChild != null) {
               queue.offer(current.leftChild);
            }
            if (current.rightChild != null) {
               queue.offer(current.rightChild);
            }
         }
         count++;
      }
      return count;
   }
   // -------------------------------------------------------------
   public boolean isBalanced() {
      if (root == null) {
         return true;
      }
      Queue<Node> queue = new LinkedList<>();
      queue.offer(root);
      while (!queue.isEmpty()) {
         Node current = queue.poll();
         int left = 0, right = 0;

         if (current.leftChild != null) {
            queue.offer(current.leftChild);
            left = countHeightWithNode(current.leftChild);
         }
         if (current.rightChild != null) {
            queue.offer(current.rightChild);
            right = countHeightWithNode(current.rightChild);
         }
         if(Math.abs(right-left) == 2){
            return false;
         }
      }
      return true;
   }
   // -------------------------------------------------------------
   public Node getRoot() {
      return this.root;
   }
   // -------------------------------------------------------------
   public boolean isIdentical(Tree tree) {
      if(root == null && tree.getRoot() == null){
         return true;
      }
      Queue<Node> queue1 = new LinkedList<>();
      Queue<Node> queue2 = new LinkedList<>();
      queue1.offer(root);
      queue2.offer(tree.getRoot());
      while (!queue1.isEmpty() && !queue2.isEmpty()) {
         Node current1 = queue1.poll();
         Node current2 = queue2.poll();

         if(current1.value != current2.value){
            return false;
         }

         if (current1.leftChild != null) {
            queue1.offer(current1.leftChild);
         }
         if (current2.leftChild != null) {
            queue2.offer(current2.leftChild);
         }
         if (current1.rightChild != null) {
            queue1.offer(current1.rightChild);
         }
         if (current2.rightChild != null) {
            queue2.offer(current2.rightChild);
         }
      }
      return true;
   }
}
// -------------------------------------------------------------

class Node {
   int value;
   Node leftChild;
   Node rightChild;
}
