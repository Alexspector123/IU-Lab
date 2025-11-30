package Problem1;
public class Main {
    static int puzzle(int base, int limit){ 
    //base and limit are nonnegative numbers 
        if ( base > limit ) 
            return -1; 
        else if ( base == limit ) 
            return 1; 
        else 
            return base * puzzle(base + 1, limit); 
    }
    public static void main(String[] args) {
        System.out.println(puzzle(14,10));
        System.out.println(puzzle(4,7));
        System.out.println(puzzle(0,0));
    }
}
