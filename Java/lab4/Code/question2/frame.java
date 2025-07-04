package question2;
import javax.swing.JFrame;
public class frame {
    public static void main(String[] args) {
        drawLine panel = new drawLine();
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(250,250);
        frame.setVisible(true);
        
        frame.add(panel);
    }
}
