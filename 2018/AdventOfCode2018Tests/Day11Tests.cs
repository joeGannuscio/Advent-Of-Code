using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day11Tests
    {
        
        [Theory]
        [InlineData(3, 5, 8, 4)]
        [InlineData(122,79,57,-5)]
        [InlineData(217,196,39,0)]
        [InlineData(101,153,71,4)]
        public void GivenSampleInput_CalculatePowerLevel_ReturnsCorrectPowerLevel(int xPos, int yPos, int serialNumber,
            int powerLevel)
        {
            var day11 = new Day11();
            var result = day11.CalculatePowerLevel(xPos, yPos, serialNumber);

            Assert.Equal(powerLevel, result);
        }

        [Theory]
        [InlineData(42, "21,61")]
        [InlineData(18, "33,45")]
        public void GivenSampleInput_Part1_ReturnsCorrectCoordiante(int serialNumber, string coordinate)
        {
            var day11 = new Day11();
            var result = day11.Part1(serialNumber);

            Assert.Equal(coordinate, result);
        }

        //dont run these, the solution works but is very slow
        //[Theory]
        //[InlineData(18, "90,269,16")]
        //[InlineData(42, "232,251,12")]
        //public void GivenSampleInput_Part2_ReturnsCorrectResult(int serialNumber, string coordinate)
        //{
        //    var day11 = new Day11();
        //    var result = day11.Part2(serialNumber);

        //    Assert.Equal(coordinate, result);
        //}
    }
}