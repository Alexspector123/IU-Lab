package question9;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

import javax.swing.JPanel;

public class drawShield extends JPanel {

    private Color[] colors = {Color.RED, Color.WHITE, Color.RED, Color.BLUE};

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        this.setBackground(Color.BLACK);
        draw(g);
    }
    public void draw(Graphics g){
        int i = 0;
        int a = getWidth() / 2;
        int b = getHeight() / 2;
        int count = 4;
        int radius = getWidth() / 8;
        do{
            if(i < 3){
                if(i % 2 == 0)
                g.setColor(new Color(0xb40000));
                else
                g.setColor(new Color(0xffffff));
            }
            else 
            g.setColor(new Color(0x000064));
            g.fillArc(a - count * radius, b - count * radius,count*radius*2,count*radius*2, 180, -180);
            g.fillArc(a - count * radius,b - count * radius,count*radius*2,count*radius*2,0,-180);
            i++;
            count--;
        }
        while(count > 0);

        g.setColor(Color.WHITE);
        int[] xPoint = {a, a+13*radius/48, a+45*radius/48, a+18*radius/48, a+28*radius/48, a, a-28*radius/48, a-18*radius/48, a-45*radius/48, a-13*radius/48};
        int[] yPoint = {b - radius - 1, b-15*radius/48, b-15*radius/48, b+8*radius/48, b+38*radius/48, b+22*radius/48, b+38*radius/48, b+8*radius/48, b-15*radius/48, b-15*radius/48};
        g.fillPolygon(xPoint,yPoint,10);
    }    
}

 