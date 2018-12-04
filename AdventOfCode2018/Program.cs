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
                case "day1":
                    var day1 = new Day1();
                    Console.WriteLine(day1.GetResults());
                    break;
                case "day2":
                    var day2 = new Day2();
                    Console.WriteLine(day2.GetResults());
                    break;
                default:
                    Console.WriteLine("Not found");
                    break;     
            }

            Console.ReadLine();
        }
    }
}
