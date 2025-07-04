import java.util.Scanner;

public class commerce {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a new ID for order: ");
        Order order = new Order();
        order.setOrderID(sc.next());
        int n;
        System.out.print("How many items in the order: ");
        n = sc.nextInt();
        for(int i=0;i<n;i++)
        {
            String ID, name;
            double price;
            sc.nextLine();
            System.out.print("Please enter the ID of item "+i+": ");
            ID = sc.nextLine();
            System.out.print("Please enter the name of item "+i+": ");
            name = sc.nextLine();
            System.out.print("Please enter the price of item "+i+": ");
            price = sc.nextDouble();
            Item item = new Item(ID, name, price);
            order.add(item);
        }
        System.out.println("You have a new order with ID: "+order.getOrderID());
        System.out.println("In the order, you have "+n+" items");
        System.out.format("The average price in the order is: %.2f",order.calculateAverageCost());
    }
}
