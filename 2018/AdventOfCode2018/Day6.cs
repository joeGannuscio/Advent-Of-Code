using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

namespace AdventOfCode2018
{
    public class Day6
    {
        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day6Input.txt");
        private List<string> _input;

        public Day6()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 6 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 6 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(List<string> input)
        {

            var inputCoordinates = ConvertInputToCoordinates(input);
            var xMax = inputCoordinates.Max(c => c.XPos);
            var yMax = inputCoordinates.Max(c => c.YPos);

            var grid = new int[xMax + 2, yMax + 2];


            for (int x = 0; x <= xMax + 1; x++)
            {
                for (int y = 0; y <= yMax + 1; y++)
                {
                    var distances = inputCoordinates
                        .Select((c, i) => (i, dist: Math.Abs(c.XPos - x) + Math.Abs(c.YPos - y)))
                        .OrderBy(c => c.dist)
                        .ToArray();

                    if (distances[1].dist != distances[0].dist)
                    {
                        grid[x, y] = distances[0].Item1;
                    }
                    else
                    {
                        grid[x, y] = -1;
                    }

                }
            }
            
            var excluded = new List<int>();
            var counts = Enumerable.Range(-1, inputCoordinates.Count + 1).ToDictionary(i => i, c => 0);

            for (int x = 0; x <= xMax + 1; x++)
            {
                for (int y = 0; y <= yMax + 1; y++)
                {
                    if (x == 0 || y == 0 ||
                        x == xMax + 1 || y == yMax + 1)
                    {
                        excluded.Add(grid[x, y]);
                    }
                    counts[grid[x, y]] += 1;
                }
            }
            

            excluded = excluded.Distinct().ToList();
            var result = counts.Where(kvp => !excluded.Contains(kvp.Key))
                .OrderByDescending((kvp => kvp.Value));

            return result.Max(r => r.Value).ToString();
        }

        public string Part2(List<string> input)
        {
            var inputCoordinates = ConvertInputToCoordinates(input);
            var xMax = inputCoordinates.Max(c => c.XPos);
            var yMax = inputCoordinates.Max(c => c.YPos);

            var grid = new int[xMax + 2, yMax + 2];
            var count = 0;


            for (int x = 0; x <= xMax + 1; x++)
            {
                for (int y = 0; y <= yMax + 1; y++)
                {
                    var distances = inputCoordinates
                        .Select((c, i) => (i, dist: Math.Abs(c.XPos - x) + Math.Abs(c.YPos - y)))
                        .OrderBy(c => c.dist)
                        .ToArray();

                    if (distances[1].dist != distances[0].dist)
                    {
                        grid[x, y] = distances[0].Item1;
                    }
                    else
                    {
                        grid[x, y] = -1;
                    }

                    if (distances.Sum(c => c.dist) < 10000)
                        count++;
                }
            }

            return count.ToString();
        }

        private List<string> InputReader(string inputPath)
        {
            var inputList = new List<string>();

            var fileStream = File.OpenRead(inputPath);
            var streamReader = new StreamReader(fileStream);
            string line;
            while ((line = streamReader.ReadLine()) != null)
            {
                inputList.Add(line);
            }

            return inputList;
        }

        private List<Coordinate> ConvertInputToCoordinates(List<string> input)
        {
            var coordinates = new List<Coordinate>();

            foreach (var val in input)
            {
                var splitStr = val.Split(',');
                coordinates.Add(new Coordinate()
                {
                    XPos = Convert.ToInt32(splitStr[0]),
                    YPos = Convert.ToInt32(splitStr[1])
                });
            }

            return coordinates;
        }

        private int CalculateManhattanDistance(int x1, int x2, int y1, int y2)
        {
            var distance = Math.Abs(x1 - x2) + Math.Abs(y1 - y2);
            return distance;
        }

        
    }

    public class Coordinate
    {
        public int XPos { get; set; }
        public int YPos { get; set; }
        public int ClosestCount { get; set; }
                
    }
}