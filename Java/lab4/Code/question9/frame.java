package question9;

import javax.swing.JFrame;

public class frame {
    public static void main(String[] args) {
        
    JFrame frame = new JFrame();
    drawShield shield = new drawShield();

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400,425);
    frame.setVisible(true);

    frame.add(shield);
    }
}
