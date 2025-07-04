package question7;

import javax.swing.JFrame;

public class frame {
    public static void main(String[] args) {
        
    JFrame frame = new JFrame();
    drawColorRectangle circle = new drawColorRectangle();

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(250,250);
    frame.setVisible(true);

    frame.add(circle);
    }
}
