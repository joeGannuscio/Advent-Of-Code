using System;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.IO;
using System.Reflection;
using System.Linq;

//https://adventofcode.com/2018/day/1

namespace AdventOfCode2018
{
    public class Day1
    {

        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day1Input.txt");
        private List<int> _input = new List<int>();

        public Day1()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 1 Part 1 Solution: " + Part1(_input).ToString());
            stringBuilder.Append("\nDay 1 Part 2 Solution: " + Part2(_input).ToString());

            return stringBuilder.ToString();

        }

        public int Part1(List<int> input)
        {
            var result = 0;

            foreach(var value in input)
            {
                result += value;
            }

            return result;
        }

        public int Part2(List<int> input)
        {
            var frequencyList = new Dictionary<int, int>();
            var result = 0;
            var inputCount = input.Count;
            var index = 0;

            while(true)
            {
                if (index < inputCount)
                {
                    result += input[index];
                }
                else
                {
                    index = 0;
                    result += input[index];
                }

                if (frequencyList.ContainsKey(result))
                {
                    frequencyList[result]++;
                    if (frequencyList[result] > 1)
                        return result;
                }
                else
                    frequencyList.Add(result, 1);

                index++;


            }
        }

        private List<int> InputReader(string inputPath)
        {
            var inputList = new List<int>();

            var fileStream = File.OpenRead(inputPath);
            var streamReader = new StreamReader(fileStream);
            string line;
            while((line = streamReader.ReadLine()) != null)
            {
                inputList.Add(Convert.ToInt32(line));
            }
            
            return inputList;
        }
    }
}
