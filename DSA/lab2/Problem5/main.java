package Problem5;

public class main {
    public static void main(String[] args) {
        List list = new List(10);
        
        list.insert("Phuong", "Nguyen", 41.02);
        list.insert("Huy", "Phan", 47.70);
        list.insert("Duy", "Le", 86.32);
        list.insert("Vinh", "Bui", 28.68);
        list.insert("Nga", "Nguyen", 67.14);
        list.insert("Ngan", "Nguyen", 68.46);
        list.insert("Anh", "Tran", 36.64);
        list.insert("Huy", "Nguyen", 72.00);
        list.insert("Long", "Nguyen", 48.89);
        list.insert("Ngan", "Phan", 86.35);

        
        System.out.println("Sort by First Name: ");
        list.sortFName();
        list.display();
        System.out.println("//--------------------------------");

        System.out.println("Sort by Last Name: ");
        list.sortLName();
        list.display();
        System.out.println("//--------------------------------");

        System.out.println("Sort by Grade: ");
        list.sortGrade();
        list.display();
    }
}

