using System;
using System.Collections.Generic;
using System.Text;
using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    
    public class Day3Tests
    {
        [Fact]
        public void GivenSampleInput_Part1_ReturnsCorrectResult()
        {
            var sampleInput = new List<string>() {"#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"};
            var expected = "4";
            var width = 11;
            var height = 9;
            var day3 = new Day3();
            var result = day3.Part1(sampleInput, width, height);
        }

        [Fact]
        public void GivenSampleInput_Part2_ReturnsId3()
        {
            var sampleInput = new List<string>() { "#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2" };
            var expected = "3";
            var width = 11;
            var height = 9;
            var day3 = new Day3();
            var result = day3.Part2(sampleInput, width, height);
        }
    }
}
