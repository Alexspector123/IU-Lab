import java.util.Random;
public class Particle {
    private int x;
    private int y;
    public Particle(int x, int y){
        this.x = x;
        this.y = y;
    }
    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }
    public void move(){
        Random random = new Random();
        int X1=0;
        int Y1=0;
        while(X1 == 0 || X1 == Box.getWidth() - 1)
        X1 = x + random.nextInt(3) - 1;
        this.x = X1;
        while(Y1 == 0 || Y1 == Box.getHeight() - 1)
        Y1 = y + random.nextInt(3) - 1;
        this.y = Y1;
    }
    
}
