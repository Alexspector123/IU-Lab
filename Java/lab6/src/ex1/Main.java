package ex1;

public class Main {
    public static void main(String[] args){

        MyPair<String, Integer> pair1 = new MyPair<String, Integer>("Anders", 13);

        MyPair<String, Double> pair2 = new MyPair<String,Double>("Phoenix", 39.7);

        MyPair<String, Integer> grades[] = new MyPair[5];
        grades[0] = new MyPair<String, Integer>("Huy", 10);
        grades[1] = new MyPair<String, Integer>("Phuong", 11);
        grades[2] = new MyPair<String, Integer>("Hitori", 12);

        for(MyPair<String, Integer> pair : grades){
            System.out.println(pair);
        }

        MyPair<MyPair<Integer, Integer>, String> appointment = new MyPair<>(new MyPair<>(10 , 11), "Huy");
        System.out.println(appointment.Fst.Snd);
        
        pair1 = pair1.swap(grades[0]);
        System.out.println(pair1);
    }
}
