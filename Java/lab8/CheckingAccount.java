public class CheckingAccount extends Account implements Comparable<CheckingAccount> {

    private double overdraftAmount;

    public CheckingAccount(String accID, String cusID, String accType, double Balance, double overdraftAmount, String password){
        super(accID, cusID, accType, Balance, password);
        this.overdraftAmount = overdraftAmount;
    }
    public double getOverdraftAmount(){
        return overdraftAmount;
    }
    public void setOverdraftAmount(double overdraftAmount){
        this.overdraftAmount = overdraftAmount;
    }
    @Override
    public boolean withdraw(double amount) {
        if(getBalance() < amount){
            if(amount - getBalance() > overdraftAmount){
                return false;
            }
            else{
                overdraftAmount = overdraftAmount - (amount - getBalance());
                setBalance(0);
                return true;
            }
        }
        else{
            setBalance(getBalance() - amount);
            return true;
        }
    }
    @Override
    public int compareTo(CheckingAccount checkingAccount) {
            if(overdraftAmount > checkingAccount.overdraftAmount){
                return -1;
            }
            return 0;
    }
    @Override
    public String toString(){
        String s = "";
        s = s + "accID: "+getAccountID() + "; cusID:"+getCustomerID()+ "; " + getAccountType()+"; initial balance : "+getBalance() + "; Overdraft amount : "+getOverdraftAmount() + "; Password : "+getPassword(); 
        return s;
    }
}
