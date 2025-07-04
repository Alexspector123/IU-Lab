package question3;
import javax.swing.JFrame;
public class frame {
    public static void main(String[] args) {
        drawMovingLine2 line = new drawMovingLine2();
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(250,250);
        frame.setVisible(true);
        
        frame.add(line);
    }
}
