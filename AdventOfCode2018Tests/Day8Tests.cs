using AdventOfCode2018;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day8Tests
    {

        [Fact]
        public void GivenSampleInput_Part1_ReturnsCorrectSum()
        {
            var sampleInput = new List<int>() { 2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2 };
            var day8 = new Day8();
            var expected = "138";
            var result = day8.Part1(sampleInput);

            Assert.Equal(expected, result);
        }

        [Fact]
        public void GivenSampleInput_Part2_ReturnsCorrectSum()
        {
            var sampleInput = new List<int>() { 2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2 };
            var day8 = new Day8();
            var expected = "66";
            var result = day8.Part2(sampleInput);

            Assert.Equal(expected, result);
        }
    }
}
