package question3;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawMovingLine2 extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int width = getWidth();
        int height = getHeight();
        int i=0;
        int ratio = 10;
        int widthStep = width/ratio;
        int heightStep = height/ratio;
        while (i<width) {
            g.drawLine(0, 0, i*widthStep, height - i*heightStep);
            g.drawLine(width, height, i*widthStep, height - i*heightStep);
            g.drawLine(0, height, i*heightStep, i*widthStep);
            g.drawLine(width, 0, i*heightStep, i*widthStep);
            i++;
        }
    } 
}
