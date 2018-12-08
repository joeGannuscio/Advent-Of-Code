using System.Collections.Generic;
using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day7Tests
    {

        private List<string> _sampleInput = new List<string>()
        {
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."
        };

        [Fact]
        public void GivenSampleInput_Part1_ReturnsCorrectString()
        {
            var expected = "CABDFE";
            var day7 = new Day7();
            var result = day7.Part1(_sampleInput);

            Assert.Equal(expected, result);
        }

        [Fact]
        public void GivenSampleInput_Part2_ReturnsCorrectTime()
        {
            var expected = "15";
            var day7 = new Day7();
            var result = day7.Part2(_sampleInput, 2);

            Assert.Equal(expected, result);
        }
    }
}