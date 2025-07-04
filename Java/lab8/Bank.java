import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Bank {
    private String name;
    private String address;
    private ArrayList<Account> listofAccount;
    
    public Bank(String name, String address){
        this.name = name;
        this.address = address;
        listofAccount = new ArrayList<Account>();
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getAddress(){
        return address;
    }
    public void setAddress(String address){
        this.address = address;
    }
    public void addAccount(Account account){
        try {
            listofAccount.add(account);
            System.out.println(account.getCustomerID() + " " + account.getAccountType() + " " + account.getAccountID() + " was added successfully!");
        } catch (Exception e) {
            System.out.println("Couldn't add this account");
        }
    }
    public void removeAccount(String accountID){
        try {
            for(int i = 0; i<listofAccount.size();i++){
                if(listofAccount.get(i).getAccountID() == accountID){
                    listofAccount.remove(0);
                }
            }
        } catch (Exception e) {
            System.out.println("Couldn't remove this account");
        }
    }
    public String displayAccountByAccountID(String accountID){
        String s = "No result";
        for(Account account : listofAccount){
            if(account.getAccountID() == accountID){
                s = account.toString();
            }
        }
        return s;
    }
    public Account login(String accountID, String password){
        String s = "Incorrect accountID or password";
        for(Account account : listofAccount){
            if(account.getAccountID() == accountID && account.getPassword() == password){
                return account;
            }
        }
        System.out.println(s);
        return null;
    }
    public String toString(){
    //    Collections.sort(listofAccount);
        String s = "";
        s = s + "Name: "+getName() + "; Address:"+getAddress();
        s = s + "; List of Account in the bank:\n";
        for(Account account : listofAccount){
            s = s + account.toString();
            s = s + "\n";
        }
        return s;
    }
}
