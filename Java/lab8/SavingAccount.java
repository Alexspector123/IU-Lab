public class SavingAccount extends Account implements Comparable<SavingAccount> {

    private double interestRate;

    public SavingAccount(String accID, String cusID, String accType, double initBalance, double interestRate, String password){
        super(accID, cusID, accType, initBalance, password);
        this.interestRate = interestRate;
    }
    public double getInterestRate(){
        return interestRate;
    }
    public void setInterestRate(double interestRate){
        this.interestRate = interestRate;
    }
    @Override
    public boolean withdraw(double amount) {
        if(getBalance() < amount){
            return false;
        }
        else{
            setBalance(getBalance() - amount);
            return true;
        }
    }
    @Override
    public int compareTo(SavingAccount savingAccount) {
        if(interestRate > savingAccount.interestRate){
            return -1;
        }
        return 0;
    }
    @Override
    public String toString(){
        String s = "";
        s = s + "accID: "+getAccountID() + "; cusID:"+getCustomerID()+ "; " + getAccountType()+"; initial balance : "+getBalance() + "; Interest Rate : "+getInterestRate() + "; Password : "+getPassword(); 
        return s;
    }
}
