public class Player {
    private String choice;
    private int bet;
    private int wallet;
    public Player(int wallet){
        this.wallet = wallet;
    }
    public int getBet(){
        return this.bet;
    }
    public void setBet(int bet){
        this.bet = bet;
    }
    public String getChoice(){
        return this.choice;
    }
    public void setChoice(String choice){
        this.choice = choice;
    }
    public int getWallet(){
        return this.wallet;
    }
    public void addWallet(int amount){
        this.wallet += amount;
    }
}
