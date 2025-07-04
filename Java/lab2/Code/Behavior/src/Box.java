import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Box {
    char[][] c;
    private static int width;
    private static int height;
    private int num;
    private int step;
    Random random = new Random();
    ArrayList<Particle> particleList;
    
    public static int getWidth(){
        return width;
    }
    public static int getHeight(){
        return height;
    }
    public Box(int width, int height) {
        this.width = width;
        this.height = height;
        c = new char[height][width];
        particleList = new ArrayList<>();
    }
    public void update(){
        Scanner sc = new Scanner(System.in);
        System.out.printf("Enter the number of particle: ");
        num = sc.nextInt();
        for(int i=0;i<num;i++)
        {Particle p = new Particle(random.nextInt(width - 2)+1,random.nextInt(height - 2)+1);
        particleList.add(p);
        }
        System.out.printf("Enter the number of step: ");
        step = sc.nextInt();
        for(int i=0;i<height;i++)
        {
            for(int j=0;j<width;j++)
        {
            if(i==0 || i==(height - 1))
            c[i][j] = '-';
            else if(j==0 || j==(width - 1))
            c[i][j] = '|';
            else c[i][j] = ' ';
        }
        }
        for(int k=1;k<=step;k++)
        {
            if(num <= (width - 2)*(height - 2))
            {
            System.out.println("Step "+k+": ");
            for(Particle particle : particleList)
            {
                particle.move();
            }
            
            for(int i=0; i<num-1;i++)
            {
                for(int j=i+1;j<num;j++)
                {
                    if(particleList.get(i).getX() == particleList.get(j).getX() && particleList.get(i).getY() == particleList.get(j).getY()){
                        Particle p = new Particle(random.nextInt(width - 2)+1,random.nextInt(height - 2)+1);
                        particleList.add(p);
                        num++;
                    }
                }
            } 
            for(Particle particle : particleList)
            {
                c[particle.getY()][particle.getX()] = '*';
            }
            for(int i=0;i<height;i++)
            {
                for(int j=0;j<width;j++)
            {
                System.out.printf("%c", c[i][j]);
            }
            System.out.println();
            }
            for(Particle paritle : particleList)
            {
                c[paritle.getY()][paritle.getX()] = ' ';
            }
        }
    }
    }
}