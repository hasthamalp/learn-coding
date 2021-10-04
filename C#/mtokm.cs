//C# program to convert a meter to kilo-meter and vice versa.

using System;

public class Distance
{
    public static double MeterToKilometer(double meter)
    {
        double KM = 0;

        KM = meter / 1000;

        return KM;
    }

    public static double KilometerToMeter(double km)
    {
        double METER = 0;

        METER = km * 1000;
 
        return METER;
    }

    static void Main()
    {
        double meter = 0;
        double km    = 0;

        Console.Write("Enter the value of meter : ");
        meter = double.Parse(Console.ReadLine());

        km = MeterToKilometer(meter);
        Console.WriteLine("Kilometer : "+km+"km");

        Console.Write("Enter the value of kilometer : ");
        km = double.Parse(Console.ReadLine());

        meter = KilometerToMeter(km);
        Console.WriteLine("Meter : " + meter + "m");

    }
}
