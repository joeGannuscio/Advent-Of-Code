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
                case "4":
                    var day4 = new Day4();
                    Console.WriteLine(day4.GetResults());
                    break;
                case "5":
                    var day5 = new Day5();
                    Console.WriteLine(day5.GetResults());
                    break;
                case "6":
                    var day6 = new Day6();
                    Console.WriteLine(day6.GetResults());
                    break;
                case "7":
                    var day7 = new Day7();
                    Console.WriteLine(day7.GetResults());
                    break;
                case "8":
                    var day8 = new Day8();
                    Console.WriteLine(day8.GetResults());
                    break;
                case "9":
                    var day9 = new Day9();
                    Console.WriteLine(day9.GetResults());
                    break;
                case "10":
                    var day10 = new Day10();
                    day10.GetResults();
                    break;
                case "11":
                    var day11 = new Day11();
                    Console.WriteLine(day11.GetResults());
                    break;
                case "12":
                    var day12 = new Day12();
                    Console.WriteLine(day12.GetResults());
                    break;
                case "14":
                    var day14 = new Day14();
                    Console.WriteLine(day14.GetResults());
                    break;
                default:
                    Console.WriteLine("Not found");
                    break;     
            }

            Console.ReadLine();
        }
    }
}
