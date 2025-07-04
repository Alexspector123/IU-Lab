import java.util.Scanner;

public class BigSmallGame {
    public static void main(String[] args) throws Exception {
        String exit = "true";
        int i=1;
        Scanner sc = new Scanner(System.in);
        House house = new House(1000);
        Player player = new Player(100);
        System.out.println("The house has $1000");
        System.out.println("The player has $100");
        System.out.println("Try your luck to win all money of the house!");
        while(exit.equals("true") && player.getWallet()!=0 && house.getWallet()!=0)
        {
            System.out.println("Round "+i+": ");
            System.out.println("How much do you want to bet?");
            player.setBet(sc.nextInt());
            sc.nextLine();
            System.out.println("You have bet $"+player.getBet()+"!");
            System.out.println("Do you want to bet big or small?(big/small)");
            player.setChoice(sc.nextLine());
            System.out.print("The dices are: ");
            house.rollDices();
            house.printDices();
            System.out.println();
            System.out.println("The sum of 3 dices is "+house.sumDices()+"!");
            System.out.println(player.getChoice());
            System.out.println(house.checkDicesResult());
            if(player.getChoice() == house.checkDicesResult())
            {
                System.out.println("You Won $"+player.getBet()+"!");
                house.addWallet(-player.getBet());
                player.addWallet(player.getBet());
            }
            else
            {
                System.out.println("You Lost $"+player.getBet()+"!");
                house.addWallet(player.getBet());
                player.addWallet(-player.getBet());
            }
            System.out.println("The house has $"+house.getWallet());
            System.out.println("The player has $"+player.getWallet());
            if(player.getWallet()==0)
            System.out.println("You Lose the game");
            else if(house.getWallet()==0)
            System.out.println("You Win the game");
            else
            {
            System.out.println("Do you still want to continue to play?(true/false)");
            exit = sc.next();
            i++;
            }
        }
    }
}
