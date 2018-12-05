using System;

namespace AdventOfCode2018
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Specify day to get solution:");
            var day = Console.ReadLine();

            switch(day)
            {
                case "1":
                    var day1 = new Day1();
                    Console.WriteLine(day1.GetResults());
                    break;
                case "2":
                    var day2 = new Day2();
                    Console.WriteLine(day2.GetResults());
                    break;
                case "3":
                    var day3 = new Day3();
                    Console.WriteLine(day3.GetResults());
                    break;
                default:
                    Console.WriteLine("Not found");
                    break;     
            }

            Console.ReadLine();
        }
    }
}
