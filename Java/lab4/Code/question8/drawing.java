package question8;

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JPanel;

public class drawing extends JPanel {

    private ArrayList<Integer> totalLength = new ArrayList<>();

    public void setLength(int length){
        this.totalLength.add(length);
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        int y = getHeight()/6;
        Random rand = new Random();
        for(Integer length : totalLength){
            g.setColor(new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256)));
            g.fillRect(0,y,length,20);
            y+=30;
        }
    }
}
