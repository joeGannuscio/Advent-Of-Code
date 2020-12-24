using System.Collections.Generic;
using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day12Tests
    {
        [Fact]
        public void GivenSampleInput_Part1_ReturnsCorrectSum()
        {
            var initialState = "#..#.#..##......###...###";
            var sampleInput = new List<string>()
            {
                "...## => #",
                "..#.. => #",
                ".#... => #",
                ".#.#. => #",
                ".#.## => #",
                ".##.. => #",
                ".#### => #",
                "#.#.# => #",
                "#.### => #",
                "##.#. => #",
                "##.## => #",
                "###.. => #",
                "###.# => #",
                "####. => #",
            };
            var generations = 20;
            var expected = "325";
            var day12 = new Day12();
            var result = day12.Part1(initialState, sampleInput, generations);

            Assert.Equal(expected, result);
        }
    }
}