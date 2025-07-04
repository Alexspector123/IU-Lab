import java.util.ArrayList;

public class Order {
    private String ID;
    private ArrayList<Item> itemList; 

    public void setOrderID(String ID){
        this.ID = ID;
    }
    public String getOrderID(){
        return this.ID;
    }
    public void add(Item item){
        itemList.add(item);
    }
    public Order(){
        itemList = new ArrayList<>();
    }
    public double calculateAverageCost(){
        double average = 0;
        for(Item item : itemList)
        average += item.getItemPrice();
        average /= itemList.size();
        return average;
    }
}
