public class Item {
    private String ID;
    private String name;
    private double price;

    public void setItemID(String ID){
        this.ID = ID;
    }
    public String getItemID(){
        return this.ID;
    }
    public void setItemName(String name){
        this.name = name;
    }
    public String getItemName(){
        return this.name;
    }
    public void setItemPrice(double price){
        this.price = price;
    }
    public double getItemPrice(){
        return this.price;
    }
    public Item(String ID, String name, double price){
        this.ID = ID;
        this.name = name;
        this.price = price;
    }
}
