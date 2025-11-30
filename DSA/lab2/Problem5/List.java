package Problem5;

public class List {
   private Student[] st;
   private int nElems;

   public List(int max)
   {
      st = new Student[max];
      nElems = 0;
   }

   public void insert(String fname, String lname, double grade)
   {
      st[nElems] = new Student(fname, lname, grade);
      nElems++;
   }
   public void display()
   {
      for (int i = 0; i < nElems; i++)
         System.out.println(st[i].toString());
      System.out.println("");
   }
   public void sortFName(){
      for(int i=0; i<nElems-1; i++){
         for(int j=i+1; j<nElems; j++){
            if(st[i].getFname().compareTo(st[j].getFname()) > 0){
               swap(i, j);
            }
         }
      }
   }
   public void sortLName(){
      for(int i=0; i<nElems-1; i++){
         for(int j=i+1; j<nElems; j++){
            if(st[i].getLname().compareTo(st[j].getLname()) > 0){
               swap(i, j);
            }
         }
      }
   }
   public void sortGrade(){
      for(int i=0; i<nElems-1; i++){
         for(int j=i+1; j<nElems; j++){
            if(st[i].GetGrade() > st[j].GetGrade()){
               swap(i, j);
            }
         }
      }
   }
   public void swap(int i, int j){
      Student temp = st[i];
      st[i] = st[j];
      st[j] = temp;
   }
}
