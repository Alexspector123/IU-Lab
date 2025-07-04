package question7;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

import javax.swing.JPanel;

public class drawColorRectangle extends JPanel {
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g);
    }
    public void draw(Graphics g){
        int a = getWidth() / 2;
        int count = a/10;
        int b = getHeight() / 2;
        int width = 40;
        int height = 30;
        Random rand = new Random();
        do{
            if(a - count * width > 0 && b - count * height > 0){
                g.setColor(new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256)));
                g.fillRect(a - count*width, b - count*height,count*width*2, count*height*2);
            }
            count--;
        }
        while(count > 0);
    }    
}
