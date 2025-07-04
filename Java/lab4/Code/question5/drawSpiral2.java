package question5;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawSpiral2 extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int width = getWidth();
        int height = getHeight();
        int a=width/2;
        int b=height/2;
        int radius = 10;
        int i = 2;
        int r = radius*i;
        char side = 'd';
        
        g.drawArc(a,b,radius, radius, 0, 180);
        a-=radius;
        
        for(int j=0;j<1000;j++) {
        r = radius*i;
        b-= radius/2;
        switch (side) {
            case 'd':
            g.drawArc(a,b,r, r, 0, -180);
            side = 'u';
            break;
            case 'u':
            g.drawArc(a,b,r, r, 0, 180);
            a-=radius;
            side = 'd';
            break;
            default:
                break;
        }
        i++;
        }
        }
} 
