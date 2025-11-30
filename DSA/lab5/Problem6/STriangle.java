package Problem6;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

import javax.swing.JPanel;

public class STriangle extends JPanel {

    private int n;

    public STriangle(int n){
        this.n = n;
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);

        draw(g, 700, 200, 400, n);
    }
    public void draw(Graphics g, int x, int y, int size, int n){

        int[] xPoints = {x, x-size/2, x+size/2};
        int[] yPoints = {y, y+size, y+size};
        g.setColor(Color.BLACK);
        if(n == 0){
            g.fillPolygon(xPoints, yPoints, 3);
            return;
        }
        draw(g, x,y,size/2,n-1);
        draw(g, x-size/4, y+size/2,size/2, n-1);
        draw(g, x+size/4, y+size/2,size/2, n-1);
    }    
}