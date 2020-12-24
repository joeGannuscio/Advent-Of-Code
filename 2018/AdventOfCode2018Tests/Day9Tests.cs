using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day9Tests
    {
        [Theory]
        [InlineData(9, 25, "32")]
        [InlineData(10, 1618, "8317")]
        [InlineData(13, 7999, "146373")]
        [InlineData(21, 6111, "54718")]
        [InlineData(30, 5807, "37305")]
        public void GivenSampleInput_Part1_ReturnsCorrectScore(int players, int lastMarbleValue, string highScore)
        {
            var day9 = new Day9();
            var result = day9.Part1(players, lastMarbleValue);

            Assert.Equal(highScore, result);
        }
    }
}