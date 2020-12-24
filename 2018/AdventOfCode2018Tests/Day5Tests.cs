using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day5Tests
    {
        [Fact]
        public void GivenSampleString_Part1_ReturnsCorrectCount()
        {
            var sampleInput = @"dabAcCaCBAcCcaDA";
            var day5 = new Day5();
            var result = day5.Part1(sampleInput);

            Assert.Equal("10", result);
        }

        [Fact]
        public void GivenSampleString_Part2_ReturnsCorrectCount()
        {
            var sampleInput = @"dabAcCaCBAcCcaDA";
            var day5 = new Day5();
            var result = day5.Part2(sampleInput);

            Assert.Equal("4", result);
        }
    }
}