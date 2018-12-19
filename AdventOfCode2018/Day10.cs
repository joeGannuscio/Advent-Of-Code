using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace AdventOfCode2018
{
    public class Day10
    {
        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day10Input.txt");
        private List<Point> _input;

        public Day10()
        {
            _input = InputReader(_inputPath);
        }

        public void GetResults()
        {
            Part1(_input);
        }

        public void Part1(List<Point> input)
        {
            var time = 0;
            var userEntry = "";

            

            while (!userEntry.Equals("stop"))
            {

                Console.WriteLine(time.ToString()+'\n');
                foreach (var point in input)
                {
                    point.XPos += point.XVel;
                    point.YPos += point.YVel;
                }

                var xMin = input.Min(p => p.XPos);
                var xMax = input.Max(p => p.XPos);
                var yMin = input.Min(p => p.YPos);
                var yMax = input.Max(p => p.YPos);

                if (xMin > -200 && yMin > -200 && xMax < 300 && yMax < 300)
                {
                    for (var i = yMin; i <= yMax; i++)
                    {
                        for (var j = xMin; j <= xMax; j++)
                        {
                            Console.Write(input.Any(p => p.XPos == j && p.YPos == i) ? "*" : ".");
                        }
                        Console.WriteLine();
                        
                    }
                    userEntry = Console.ReadLine();
                }
                time++;
                
                

            }            
        }

        private List<Point> InputReader(string inputString)
        {
            var stringList = new List<string>();
            var inputList = new List<Point>();

            var fileStream = File.OpenRead(inputString);
            var streamReader = new StreamReader(fileStream);
            string line;
            while ((line = streamReader.ReadLine()) != null)
            {
                stringList.Add(line);
            }

            foreach (var str in stringList)
            {
                var splitStr = Regex.Split(str, "[^\\d-]+");
                inputList.Add(new Point()
                {
                    XPos = Convert.ToInt32(splitStr[1]),
                    YPos = Convert.ToInt32(splitStr[2]),
                    XVel = Convert.ToInt32(splitStr[3]),
                    YVel = Convert.ToInt32(splitStr[4])
                });
            }

            return inputList;
        }
    }

    public class Point
    {
        public int XPos { get; set; }
        public int YPos { get; set; }
        public int XVel { get; set; }
        public int YVel { get; set; }
    }
}