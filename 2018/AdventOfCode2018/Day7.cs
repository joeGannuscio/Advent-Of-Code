using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

namespace AdventOfCode2018
{
    public class Day7
    {
        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day7Input.txt");
        private List<string> _input;
        private int _numberOfWorkers = 5;

        public Day7()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 7 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 7 Part 2 Solution: " + Part2(_input, _numberOfWorkers));
            return stringBuilder.ToString();
        }

        public string Part1(List<string> input)
        {
            var steps = InputParser(input);
            var result = GetStepOrder(steps);

            return result;

        }

        public string Part2(List<string> input, int numberOfWorkers)
        {
            var steps = InputParser(input);
            

            return "";
        }

        private List<string>InputReader(string inputPath)
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

        private string GetStepOrder(List<Step> steps)
        {
            var result = new StringBuilder();

            var uniqueSteps = new List<string>();

            foreach (var step in steps)
            {
                if (!uniqueSteps.Contains(step.Base))
                    uniqueSteps.Add(step.Base);
                else if (!uniqueSteps.Contains(step.Next))
                    uniqueSteps.Add(step.Next);
            }

            uniqueSteps = uniqueSteps.OrderBy(s => s).ToList();

            while (uniqueSteps.Any())
            {

                string curStep = "";

                foreach (var step in uniqueSteps)
                {
                    if (steps.All(s => s.Next != step))
                    {
                        curStep = step;
                        break;
                    }
                }

                result.Append(curStep);
                uniqueSteps.Remove(curStep);
                steps.RemoveAll(s => s.Base == curStep);
            }

            return result.ToString();
        }

        private List<Step> InputParser(List<string> inputList)
        {
            var stepList = new List<Step>();

            foreach (var input in inputList)
            {
                var splitStr = input.Split(' ');
                stepList.Add(new Step()
                {
                    Base = splitStr[1],
                    Next = splitStr[7]
                });
            }

            return stepList;
        }
    }

    public class Step
    {
        public string Base { get; set; }
        public string Next { get; set; }
    }
}