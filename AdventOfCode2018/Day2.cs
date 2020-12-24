﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

//https://adventofcode.com/2018/day/2

namespace AdventOfCode2018
{
    public class Day2
    {
        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day2Input.txt");
        private List<string> _input = new List<string>();

        public Day2()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 2 Part 1 Solution: " + Part1(_input).ToString());
            stringBuilder.Append("\nDay 2 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public int Part1(List<string> input)
        {
            var twoCount = 0;
            var threeCount = 0;

            twoCount = input.Count(id => id.GroupBy(letter => letter).Any(group => group.Count() == 2));
            threeCount = input.Count(id => id.GroupBy(letter => letter).Any(group => group.Count() == 3));

            var checksum = twoCount * threeCount;
            return checksum;
        }

        public string Part2(List<string> input)
        {
            var differenceCount = 0;
            StringBuilder stringBuilder = new StringBuilder();

            foreach(var str in input)
            {
                foreach (var id in input)
                {
                    if (!id.Equals(str))
                    {
                        for (var i = 0; i < id.Length; i++)
                        {
                            if (!str[i].Equals(id[i]))
                            {
                                differenceCount++;
                            }
                            else
                            {
                                stringBuilder.Append(id[i]);
                            }
                        }

                        if (differenceCount == 1)
                        {
                            return stringBuilder.ToString();
                        }
                        else
                        {
                            differenceCount = 0;
                            stringBuilder.Clear();
                        }
                    }
                }
            }
            

            return "no results found";

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

    }
}
