using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;


//https://adventofcode.com/2018/day/8

namespace AdventOfCode2018
{
    public class Day8
    {

        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day8Input.txt");
        private List<int> _input;

        public Day8()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 8 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 8 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(List<int> input)
        {
            var index = 0;
            var root = BuildNode(input, ref index);
            var result = root.SumMetadata();

            return result.ToString();
        }

        public string Part2(List<int> input)
        {
            var index = 0;
            var root = BuildNode(input, ref index);
            var result = root.Value();

            return result.ToString();
        }

        public Node BuildNode(List<int> input, ref int index)
        {
            var node = new Node();
            var children = input[index++];
            var metadata = input[index++];

            //add children
            for (var i = 0; i < children; i++)
            {
                node.Children.Add(BuildNode(input, ref index));
            }

            //add metadata
            for (var i = 0; i < metadata; i++)
            {
                node.Metadata.Add(input[index++]);
            }


            return node;
        }

        private List<int> InputReader(string path)
        {
            var input = File.ReadAllText(_inputPath);
            var splitInput = input.Split(' ');
            var inputList = new List<int>();
            foreach (var str in splitInput)
            {
                inputList.Add(int.Parse(str));
            }

            return inputList;
        }
    }

    public class Node
    {
        public Node()
        {
            Children = new List<Node>();
            Metadata = new List<int>();
        }

        public List<Node> Children { get; set; } 
        public List<int> Metadata { get; set; }

        public int SumMetadata()
        {
            return Metadata.Sum() + Children.Sum(c => c.SumMetadata());
        }

        public int Value()
        {
            var value = 0;

            if (!Children.Any())
            {
                return Metadata.Sum();
            }

            foreach(var point in Metadata)
            {
                if (point <= Children.Count)
                {
                    value = value + Children[point - 1].Value();
                }
            }

            return value;
        }
    }
}
