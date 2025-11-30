package Huffman;

import java.util.*;

// -------------------------------------------------------------
// Representing Huffman coding tree
// -------------------------------------------------------------
class Tree
{
   // -------------------------------------------------------------
   public static Node node(char character, int value) {
      Node a = new Node();
      a.character = character;
      a.value = value;
      return a;
   }
   // -------------------------------------------------------------
   public static Node node(char character, int value, Node leftChild, Node rightChild) {
      Node a = new Node();
      a.character = character;
      a.value = value;
      a.leftChild = leftChild;
      a.rightChild = rightChild;
      return a;
   }
   // -------------------------------------------------------------
   public static Node huffmanTree(Map<Character, Integer> frequencyMap) {
      PriorityQueue<Node> queue = new PriorityQueue<>(Comparator.comparingInt(node -> node.value));

      for (Map.Entry<Character, Integer> entry : frequencyMap.entrySet()) {
         queue.add(node(entry.getKey(), entry.getValue()));
      }

      // Build the Huffman Tree
      while (queue.size() > 1) {
         Node left = queue.poll();
         Node right = queue.poll();

         Node current = node('-', left.value + right.value);
         current.leftChild = left;
         current.rightChild = right;

         queue.add(current);
      }
      return queue.poll();
   }
   // -------------------------------------------------------------
   public static void prefix(Node t) {
      if (t.leftChild==null && t.rightChild==null) 
            System.out.print(t.character+" ");
      else
      {
          System.out.print(t.character+" ");
          prefix(t.leftChild);
          prefix(t.rightChild);
      } 
   }

   // -------------------------------------------------------------
   public static void postfix(Node t) {
      if (t.leftChild==null && t.rightChild==null) 
            System.out.print(t.character+" ");
      else
      {
          postfix(t.leftChild);
          postfix(t.rightChild);
          System.out.print(t.character+" ");
      }  
   }

   // -------------------------------------------------------------
   public static void infix(Node t) {
      if (t.leftChild==null && t.rightChild==null) 
            System.out.print(t.character);
      else
      {
          System.out.print("(");
          infix(t.leftChild);
          System.out.print(t.character);
          infix(t.rightChild);
          System.out.print(")");
      } 
   }

   // -------------------------------------------------------------
   public static void showTree(int n, Node t) {
      tab(n);
      if (t.leftChild==null && t.rightChild==null) 
           System.out.println(t.character);
      else
      {
          System.out.println(t.character);
          showTree(n+2,t.leftChild);
          showTree(n+2,t.rightChild);
      }
   }

   // -------------------------------------------------------------
   public static void tab(int n) {
      for (int i = 0; i < n; i++)
         System.out.print(" ");
   }

   // -------------------------------------------------------------
}

class Node {
   char character;  
   int value;    
   Node leftChild;
   Node rightChild;
}

public class Huffman {
   public static void main(String[] args) {
      String s = "I am a student at International University. My name is Phan Tran Thanh Huy. I am working on a DSA lab";
      s = s.toLowerCase();
      Map<Character, Integer> map = new HashMap<>();
      for(int i=0;i<s.length();i++){
         if(!map.containsKey(s.charAt(i))){
            map.put(s.charAt(i),1);
         }
         else{
            map.replace(s.charAt(i), map.get(s.charAt(i))+1);
         }
      }

      Node root = Tree.huffmanTree(map);
      
      System.out.println("Huffman Codes:");
      Tree.showTree(0,root);
   }
}
