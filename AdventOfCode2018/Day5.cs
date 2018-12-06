using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

//https://adventofcode.com/2018/day/5

namespace AdventOfCode2018
{
    public class Day5
    {

        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day5Input.txt");
        private string _input;

        public Day5()
        {
            _input = File.ReadAllText(_inputPath);
        }
            

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 5 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 5 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(string input)
        {
            var result = ProcessPolymer(input);

            return result.Length.ToString();
        }

        public string Part2(string input)
        {
            var listOfChars = input.Select(c => c.ToString().ToUpperInvariant()).Distinct().ToList();
            var minPolymer = 0;
            string polymer;

            foreach (var c in listOfChars)
            {

                polymer = input.Replace(c, "");
                polymer = polymer.Replace(c.ToLowerInvariant(), "");

                var processed = ProcessPolymer(polymer);

                if (minPolymer == 0)
                {
                    minPolymer = processed.Length;
                }
                else
                {
                    if (minPolymer > processed.Length)
                        minPolymer = processed.Length;
                }

            }

            return minPolymer.ToString();
        }

        private string ProcessPolymer(string input)
        {
            int i = 0;

            while (i < input.Length - 1)
            {
                if (char.IsUpper(input[i]))
                {
                    if (input[i + 1].Equals(char.ToLower(input[i])))
                    {
                        input = input.Remove(i, 2);
                        i = 0;
                    }
                }
                else
                {
                    if (input[i + 1].Equals(char.ToUpper(input[i])))
                    {
                        input = input.Remove(i, 2);
                        i = 0;
                    }
                }

                i++;
            }

            return input;
        }
    }
}