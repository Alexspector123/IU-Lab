public class Rectangle {
    private int height; 
    private int width;

    public int getHeight(){
        return this.height;
    }
    public int getWidth(){
        return this.width;
    }
    public Rectangle(int height, int width){
        check(height, width);
        visualize();
    }
    public void check(int height, int width){
        if(width<0)
        this.width = 1;
        else this.width = width;
        if(height<0)
        this.height = 1;
        else this.height = height;
    }
    public void visualize(){
        for(int i=0;i<height;i++)
        {
        for(int j=0;j<width;j++)
           System.out.print("*");
        System.out.print("\n");
        }
    }

}
