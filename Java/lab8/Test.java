public class Test {
    public static void main(String[] args) {
        Bank bank = new Bank("ABC", "HCM");
        Account savingAccount1 = new SavingAccount("sa01", "cus001", "Savings Account", 3000, 0.03, null);
        bank.addAccount(savingAccount1);
        Account savingAccount5 = new SavingAccount("sa05", "cus001", "Savings Account", 2000, 0.02, null);
        bank.addAccount(savingAccount5);
        Account checkingAccount1 = new CheckingAccount("ca01", "cus001", "Checking Account", 5000, 500, null);
        bank.addAccount(checkingAccount1);
        Account checkingAccount2 = new CheckingAccount("ca02", "cus002", "Checking Account", 4000, 400, null);
        bank.addAccount(checkingAccount2);
        Account savingAccount2 = new SavingAccount("sa02", "cus003", "Savings Account", 2000, 0.02, null);
        bank.addAccount(savingAccount2);
        Account checkingAccount3 = new CheckingAccount("ca03", "cus003", "Checking Account", 2000, 200, null);
        bank.addAccount(checkingAccount3);
        Account savingAccount3 = new SavingAccount("sa03", "cus004", "Savings Account", 6000, 0.05, null);
        bank.addAccount(savingAccount3);
        Account checkingAccount4 = new CheckingAccount("ca04", "cus004", "Checking Account", 7000, 700, null);
        bank.addAccount(checkingAccount4);
        Account savingAccount4 = new SavingAccount("sa04", "cus005", "Savings Account", 8000, 0.05, null);
        bank.addAccount(savingAccount4);
        Account checkingAccount5 = new CheckingAccount("ca05", "cus005", "Checking Account", 5000, 500, null);
        bank.addAccount(checkingAccount5);
        
        
        System.out.println(bank.toString());
    }
    
}
