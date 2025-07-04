package question8;

import javax.crypto.spec.DESKeySpec;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class frame {
    public static void main(String[] args) {
        
    JFrame frame = new JFrame();
    drawing rect = new drawing();

    for(int i=0;i<5;i++){
        int length = Integer.parseInt(JOptionPane.showInputDialog("Enter the length of the bar "+(i+1)));
        rect.setLength(length);
    }
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(250,250);
    frame.setVisible(true);
    frame.add(rect);
}
}