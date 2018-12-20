using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

//https://adventofcode.com/2018/day/14

namespace AdventOfCode2018
{
    public class Day14
    {
        private int _input = 598701;

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 14 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 14 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(int input)
        {
            var scoreboard = new List<int> { 3, 7 };

            scoreboard = GenerateScoreboard(input+10, scoreboard);

            var result = new StringBuilder();

            for (var i = input; i < input + 10; i++)
            {
                result.Append(scoreboard[i]);
            }

            return result.ToString();
        }

        public string Part2(int input)
        {

            var scoreboard = new List<int> {3, 7};
            var elf1 = 0;
            var elf2 = 1;
            var stringInput = input.ToString();
            var result = 0;

            while (true)
            {
                var find = new string(scoreboard.Skip(scoreboard.Count - stringInput.Length - 1).Select(x => x.ToString()[0]).ToArray());

                if (find.Contains(stringInput))
                {
                    find = new string(scoreboard.Select(x => x.ToString()[0]).ToArray());
                    result = find.IndexOf(stringInput);
                    break;
                }
                
                var sum = scoreboard[elf1] + scoreboard[elf2];

                if (sum >= 10)
                    scoreboard.Add(1);
                scoreboard.Add(sum % 10);

                elf1 = (elf1 + scoreboard[elf1] + 1) % scoreboard.Count;
                elf2 = (elf2 + scoreboard[elf2] + 1) % scoreboard.Count;
            }
            
            return result.ToString();
        }

        private List<int> GenerateScoreboard(int input, List<int> scoreboard)
        {
            var elf1 = 0;
            var elf2 = 1;

            while (scoreboard.Count < input)
            {

                var sum = scoreboard[elf1] + scoreboard[elf2];

                if (sum >= 10)
                    scoreboard.Add(1);
                scoreboard.Add(sum % 10);

                elf1 = (elf1 + scoreboard[elf1] + 1) % scoreboard.Count;
                elf2 = (elf2 + scoreboard[elf2] + 1) % scoreboard.Count;
            }

            return scoreboard;
        }
    }
}