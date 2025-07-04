package question6;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawCircle extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int a = getWidth()/2;
        int b = getHeight()/2;
        int count = a/10;
        int radius = 25;
        int i=0;
        do {
            if(a - count * radius > 0 && b - count * radius > 0){
            g.drawArc(a - count*radius, b - count*radius, count*radius*2, count*radius*2, 0, 360);
            }
            count--;
        }
        while (count > 0);
        }    
}
