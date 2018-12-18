using System.Collections.Generic;
using System.IO;
using System.Reflection;
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
            stringBuilder.Append("Day 12 Part 1 Solution: " + Part1(_initialState, _input));
            stringBuilder.Append("\nDay 12 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(string initialState, List<string> inputList)
        {
            var rules = GetRulesDictionary(inputList);
            
            //20 generations
            for (var i = 0; i < 20; i++)
            {
                //expand and loop through plants
            }

            return "";
        }

        public string Part2(List<string> inputList)
        {
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