using AdventOfCode2018;
using System.Collections.Generic;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day2Tests
    {
        private Day2 _day2;

        [Fact]
        public void GivenSampleInput_Day2Part1_ReturnsCorrectChecksum()
        {
            var sampleInput = new List<string>() { "abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab" };
            _day2 = new Day2();
            var result = _day2.Part1(sampleInput);
            Assert.Equal(12, result);
        }

        [Fact]
        public void GivenSampleInput_Day2Part2_ReturnsCorrectString()
        {
            var sampleInput = new List<string> { "abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz" };
            _day2 = new Day2();
            var result = _day2.Part2(sampleInput);
            Assert.True(result.Equals("fgij"));
        }
    }
}
