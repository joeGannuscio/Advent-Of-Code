using AdventOfCode2018;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.InProcDataCollector;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day14Tests
    {
        [Theory]
        [InlineData(9, "5158916779")]
        [InlineData(5, "0124515891")]
        [InlineData(18, "9251071085")]
        [InlineData(2018, "5941429882")]
        public void GivenSampleInput_Part1_ProducesCorrectResult(int input, string expected)
        {
            var day14 = new Day14();
            var result = day14.Part1(input);

            Assert.Equal(expected, result);
        }

        [Theory]
        [InlineData(51589, "9")]
        [InlineData(92510, "18")]
        [InlineData(59414, "2018")]
        public void GivenSampleInput_Part2_ProducesCorrectResult(int input, string expected)
        {
            var day14 = new Day14();
            var result = day14.Part2(input);

            Assert.Equal(expected,result);
        }
    }
}