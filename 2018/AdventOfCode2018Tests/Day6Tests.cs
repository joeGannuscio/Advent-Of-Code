using System.Collections.Generic;
using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day6Tests
    {

        [Fact]
        public void GivenSampleCoordinates_Part1_ReturnsCorrectValue()
        {
            List<string> sampleInput = new List<string>() {"1,1", "1,6", "8,3", "3,4", "5,5", "8,9"};
            var day6 = new Day6();
            var result = day6.Part1(sampleInput);
            var expected = "17";

            Assert.Equal(expected, result);
            
        }
    }
}