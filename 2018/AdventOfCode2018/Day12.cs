using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Text;

namespace AdventOfCode2018
{
    public class Day12
    {

        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
            "InputFiles/Day12Input.txt");

        private List<string> _input;

        private string _initialState =
            "##.###.......#..#.##..#####...#...#######....##.##.##.##..#.#.##########...##.##..##.##...####..####";

        public Day12()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 12 Part 1 Solution: " + Part1(_initialState, _input, 20));
            stringBuilder.Append("\nDay 12 Part 2 Solution: " + Part2(_initialState,_input));
            return stringBuilder.ToString();
        }

        public string Part1(string initialState, List<string> inputList, int numberOfGenerations)
        {
            var rules = GetRulesDictionary(inputList);
            var currentState = initialState;
            var genBuilder = new StringBuilder();
            var sum = 0;
            var addedToFront = 0;

            // 20 generations
            for (var i = 0; i < numberOfGenerations; i++)
            {
                currentState = "..." + currentState + "...";
                genBuilder.Clear();

                addedToFront += 1;

                for (var p = 2; p < currentState.Length - 2; p++)
                {
                    var window = currentState.Substring(p - 2, 5);

                    if (rules.ContainsKey(window))
                    {
                        genBuilder.Append(rules[window]);
                    }
                    else
                    {
                        genBuilder.Append(".");
                    }
                }

                currentState = genBuilder.ToString();
            }

            for (var p = 0; p < currentState.Length; p++)
            {
                if (currentState[p].Equals('#'))
                {
                    sum += (p - addedToFront);
                }
            }

            return sum.ToString();
        }

        public string Part2(string initialState, List<string> inputList)
        {
            //stabilizes at 23 new plants per iteration
            //find the point where it stabilizes and then extrapolate to 50 billion

            var curSum = 0;
            var prevSum = 0;
            long result = 0;

            for (var i = 0; i < 1000; i++)
            {
                prevSum = curSum;
                curSum = Convert.ToInt32(Part1(initialState, inputList, i));

                if (curSum - prevSum == 23)
                {
                    result = curSum + 23 * (50000000000 - i);
                    return result.ToString();
                }
            }

            return "";

        }

        private List<string> InputReader(string inputString)
        {
            var inputList = new List<string>();

            var fileStream = File.OpenRead(inputString);
            var streamReader = new StreamReader(fileStream);
            string line;
            while ((line = streamReader.ReadLine()) != null)
            {
                inputList.Add(line);
            }

            return inputList;
        }

        private Dictionary<string, string> GetRulesDictionary(List<string> input)
        {
            var dict = new Dictionary<string, string>();

            foreach (var str in input)
            {
                var temp = str.Split(" => ");
                dict.Add(temp[0], temp[1]);
            }

            return dict;
        }
    }
}