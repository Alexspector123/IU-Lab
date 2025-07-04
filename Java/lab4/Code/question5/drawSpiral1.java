package question5;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawSpiral1 extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int width = getWidth();
        int height = getHeight();
        int a=width/2;
        int b=height/2;
        int c=a;
        int d=b;
        int i=10;
        char direction = 'd';
        while (c<width) {
            if(direction == 'd')
            d+=i;
            else if(direction == 'l')
            c-=i;
            else if(direction == 'u')
            d-=i;
            else if(direction == 'r')
            c+=i;
            g.drawLine(a, b, c, d);
            switch (direction) {
                case 'd':
                    direction = 'l';
                    break;
                case 'l':
                    direction = 'u';
                    break;
                case 'u':
                    direction = 'r';
                    break;
                case 'r':
                    direction = 'd';
                    break;
                default:
                    break;
            }
        a=c;
        b=d;
        i+=10;
        }
    } 
}
