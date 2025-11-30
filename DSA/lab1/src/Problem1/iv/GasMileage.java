package Problem1.iv;

    //********************************************************************
//  GasMileage.java       Author: Lewis/Loftus
//
//  Demonstrates the use of the Scanner class to read numeric data.
//********************************************************************

import java.util.Scanner;

public class GasMileage
{
   //-----------------------------------------------------------------
   //  Calculates fuel efficiency based on values entered by the
   //  user.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {

      Scanner scan = new Scanner (System.in);

      Car car1, car2;
      System.out.print ("Enter the number of miles and gallons of fuel used: ");
      car1 = new Car(scan.next(),scan.nextDouble(), scan.nextDouble());
      System.out.print ("Enter the number of miles and gallons of fuel used: ");
      car2 = new Car(scan.next(),scan.nextDouble(), scan.nextDouble());

      System.out.println(car1.getName() +": "+ car1.getMPS());
      System.out.println(car2.getName() +": "+ car2.getMPS());
   }
}

