package question4;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawLine1 extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int width = getWidth();
        int height = getHeight();
        int i=0;
        int ratio = 15;
        int widthStep = width/ratio;
        int heightStep = height/ratio;
        while (i<width) {
            g.drawLine(0, i*heightStep, i*widthStep, height);
            i++;
        }
    } 
}
