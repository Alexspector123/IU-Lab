package Problem6;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        
        JFrame frame = new JFrame("Sierpinski triangle");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        String n = JOptionPane.showInputDialog("Number n: ");
        STriangle triangle = new STriangle(Integer.parseInt(n));
        frame.add(triangle);

        frame.setVisible(true);
    }
}
