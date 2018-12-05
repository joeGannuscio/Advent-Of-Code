using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace AdventOfCode2018
{
    public class Day3
    {

        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day3Input.txt");
        private List<string> _input;
        private Cell[,] _cellArray;
        private int _width = 1000;
        private int _height = 1000;

        public Day3()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 3 Part 1 Solution: " + Part1(_input, _width, _height));
            stringBuilder.Append("\nDay 3 Part 2 Solution: " + Part2(_input, _width, _height));
            return stringBuilder.ToString();
        }

        public string Part1(List<string> input, int gridWidth, int gridHeight)
        {
            var commandList = InputCleaner(input);
            var result = 0;
            _cellArray = new Cell[gridWidth,gridHeight];
            GridInitializer(gridWidth, gridHeight);
            
            foreach (var command in commandList)
            {
                //loop through width
                //loop through height

                for (int i = command.XPosition; i < command.XPosition + command.Width; i++)
                {
                    for (int j = command.YPosition; j < command.YPosition + command.Height; j++)
                    {
                        _cellArray[i, j].UseCount++;
                            
                    }
                }
            }

            foreach (var cell in _cellArray)
            {
                if (cell.UseCount > 1)
                    result++;
            }

            return result.ToString();
        }

        public string Part2(List<string> input, int gridWidth, int gridHeight)
        {
            
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

        //"#123 @2,1: 3x3"
        private List<Command> InputCleaner(List<string>input)
        {
            var commands = new List<Command>();

            foreach (string str in input)
            {
                var splitStr = Regex.Split(str, "\\D+");
                commands.Add(new Command()
                {
                    Id= Convert.ToInt32(splitStr[1]),
                    XPosition = Convert.ToInt32(splitStr[2]),
                    YPosition = Convert.ToInt32(splitStr[3]),
                    Width = Convert.ToInt32(splitStr[4]),
                    Height = Convert.ToInt32(splitStr[5]),
                    

                });   
            }

            return commands;
        }

        private void GridInitializer(int x, int y)
        {
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    _cellArray[i,j] = new Cell()
                    {
                        UseCount = 0,
                    };
                }
            }
        }

    }

    public class Cell
    {

        public Cell()
        {
            CommandIDs = new List<int>();
        }
        public int UseCount { get; set; }
        public List<int> CommandIDs { get; set; }
    }

    public class Command
    {
        public int Id { get; set; }
        public int XPosition { get; set; }
        public int YPosition { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
    }
}