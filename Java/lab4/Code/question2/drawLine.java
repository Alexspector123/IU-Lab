package question2;

import java.awt.Graphics;
import javax.swing.JPanel;

public class drawLine extends JPanel{
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        
        int width = getWidth();
        int height = getHeight();

        // draw the line from the upper-left to the lower-right
        g.drawLine(0, 0, width, height);

        // draw the line from the upper-right to the lower-left
        g.drawLine(0, height, width, 0);

        // draw the vertical line
        g.drawLine(width/2, 0, width/2, height);

        // draw the horizontal line
        g.drawLine(0, height/2, width, height/2);
    }
}
