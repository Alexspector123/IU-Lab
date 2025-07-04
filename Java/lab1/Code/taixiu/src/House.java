import java.util.Random;
public class House {
    private byte MIN_SMALL;
    private byte MAX_SMALL;
    private byte MIN_BIG;
    private byte MAX_BIG;
    private int wallet;
    Dice[] dices;
    private final static int num = 3;
    public House(int wallet){
        this.wallet = wallet;
        dices = new Dice[3];
        for(int i=0;i<dices.length;i++)
        dices[i] = new Dice();
    }
    public void rollDices(){
        Random random = new Random();
        for(int i=0;i<num;i++)
        {
            dices[i].roll(random.nextInt(6)+1);
        }
    }
    public void printDices(){
        for(int i=0;i<num;i++)
        {
            System.out.print(dices[i].getValue()+" ");
        }
    }
    public int sumDices(){
        int sum = 0;
        for(int i=0;i<num;i++)
        sum+=dices[i].getValue();
        return sum;
    }
    public Dice[] getDices(){
        return this.dices;
    }
    public String checkDicesResult(){
        if(dices[0]==dices[1] && dices[1]==dices[2])
        return "Same";
        else if (sumDices()>=4 && sumDices()<=10)
        return "Big";
        else if (sumDices()>=11 && sumDices()<=17)
        return "Small";
        else return null;
    }
    public int getWallet(){
        return this.wallet;
    }
    public void addWallet(int amount){
        this.wallet += amount;
    }
}
