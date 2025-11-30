package Problem1.iv;

import java.util.Scanner;

public class GasMileage1
{
      public static void main (String[] args)
   {
      double miles;
      double gallons, mpg;

      Scanner scan = new Scanner (System.in);

      System.out.print ("Enter the number of miles: ");
      miles = scan.nextDouble();

      System.out.print ("Enter the gallons of fuel used: ");
      gallons = scan.nextDouble();

      mpg = miles / gallons;

      System.out.println ("Miles Per Gallon: " + mpg);
   }
}
