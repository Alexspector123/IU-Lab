package question3;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawMovingLine1 extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        
        int width = getWidth();
        int height = getHeight();
        int i=0;
        int ratio = 10;
        int widthStep = width/ratio;
        int heightStep = height/ratio;
        while (i<width) {
            g.drawLine(0, 0, i*widthStep, height - i*heightStep);
            i++;
    }
}
}