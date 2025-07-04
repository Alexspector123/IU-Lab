public abstract class Account{
    private String accountID;
    private String customerID;
    private String accountType;
    private double balance;
    private String password;
    
    public Account(String accountID, String customerID, String accountType, double balance, String password) {
        this.accountID = accountID;
        this.customerID = customerID;
        this.accountType = accountType;
        this.balance = balance;
        this.password = password;
    }
    
    public String getAccountID(){
        return accountID;
    }
    public void setAccountID(String accountID){
        this.accountID = accountID;
    }
    public String getCustomerID(){
        return customerID;
    }
    public void setCustomerID(String customerID){
        this.customerID = customerID;
    }
    public String getAccountType(){
        return accountType;
    }
    public void setAccountType(String accountType){
        this.accountType = accountType;
    }
    public double getBalance(){
        return balance;
    }
    public void setBalance(double balance){
        this.balance = balance;
    }
    public String getPassword(){
        return password;
    }
    public void setPassword(String password){
        this.password = password;
    }
    
    public abstract boolean withdraw(double amount);
    
}