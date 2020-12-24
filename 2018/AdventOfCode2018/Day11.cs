using System;
using System.Globalization;
using System.Text;

//https://adventofcode.com/2018/day/11

namespace AdventOfCode2018
{
    public class Day11
    {

        private int _input = 7400;
        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 11 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 11 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(int input)
        {
            int[,] grid = new int[300,300];

            grid = FillTheGrid(input);

            var maxPower = 0;
            var xPos = 0;
            var yPos = 0;
            var size = 0;

            for (var i = 0; i < 298; i++)
            {
                for (var j = 0; j < 298; j++)
                {
                    var powerLevel = grid[i, j] + grid[i + 1, j] + grid[i + 2, j] + 
                                     grid[i, j + 1] + grid[i + 1, j + 1] + grid[i + 2, j + 1] + 
                                     grid[i, j + 2] + grid[i + 1, j + 2] + grid[i + 2, j + 2];

                    if (powerLevel > maxPower)
                    {
                        maxPower = powerLevel;
                        xPos = i;
                        yPos = j;
                    }
                }
            }

            var result = $"{xPos},{yPos}";

            return result;
        }

        public string Part2(int input)
        {
            int[,] grid = new int[300, 300];

            grid = FillTheGrid(input);

            var maxPower = 0;
            var xPos = 0;
            var yPos = 0;
            var size = 0;
            var powerLevel = 0;

            var sizeIndex = 300;

            while (sizeIndex > 0)
            {
                for (var i = 0; i < 300 - sizeIndex; i++)
                {
                    for (var j = 0; j < 300 - sizeIndex; j++)
                    {
                        powerLevel = 0;
                        for (var k = 0; k < sizeIndex; k++)
                        {
                            for (var l = 0; l < sizeIndex; l++)
                            {
                                powerLevel += grid[i + k, j + l];
                            }
                        }

                        if (powerLevel > maxPower)
                        {
                            maxPower = powerLevel;
                            xPos = i;
                            yPos = j;
                            size = sizeIndex;
                        }

                    }
                }

                sizeIndex--;
            }

            var result = $"{xPos},{yPos},{size}";

            return result;
        }

        public int CalculatePowerLevel(int xPos, int yPos, int serialNumber)
        {
            //rack id xPos + 10
            //pl = rack id * yPos
            //pl += serialNumber
            //pl = hundreds digit of pl
            //subtract 5 from pl

            var rackId = xPos + 10;
            var powerLevel = rackId * yPos;
            powerLevel += serialNumber;
            powerLevel *= rackId;
            powerLevel = (int) Math.Abs(powerLevel / 100 % 10);
            powerLevel -= 5;

            return powerLevel;
        }

        private int[,] FillTheGrid(int serialNumber)
        {
            int[,] grid = new int[300, 300];

            for (var i = 0; i < 300; i++)
            {
                for (var j = 0; j < 300; j++)
                {
                    grid[i, j] = CalculatePowerLevel(i, j, serialNumber);
                }
            }

            return grid;
        }
    }
}