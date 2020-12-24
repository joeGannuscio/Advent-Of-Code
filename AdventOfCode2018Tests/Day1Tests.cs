using AdventOfCode2018;
using System;
using System.Collections.Generic;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day1Tests
    {
        private Day1 _day1;

        [Theory]
        [InlineData(1, -2, 3, 1, 3)]
        public void GivenFourInputs_Day1Part1_ReturnsCorrectResult(int value1, int value2, int value3, int value4, int expected)
        {
            _day1 = new Day1();
            var inputList = new List<int> { value1, value2, value3, value4 };
            var result = _day1.Part1(inputList);
            Assert.Equal(expected, result);
        }

        [Theory]
        [InlineData(1, 1, 1, 3)]
        [InlineData(1, 1, -2, 0)]
        [InlineData(-1, -2, -3, -6)]
        public void GivenThreeInputs_Day1Part1_ReturnsCorrectResult(int value1, int value2, int value3, int expected)
        {
            _day1 = new Day1();
            var inputList = new List<int> { value1, value2, value3 };
            var result = _day1.Part1(inputList);
            Assert.Equal(expected, result);
        }

        [Theory]
        [InlineData(1, -2, 3, 1, 2)]
        public void GivenFourInputs_Day1Part2_ReturnsCorrectResult(int value1, int value2, int value3, int value4, int expected)
        {
            _day1 = new Day1();
            var inputList = new List<int> { value1, value2, value3, value4 };
            var result = _day1.Part2(inputList);
            Assert.Equal(expected, result);
        }

        [Theory]
        [InlineData(3, 3, 4, -2, -4, 10)]
        [InlineData(-6, 3, 8, 5, -6, 5)]
        [InlineData(7, 7, -2, -7, -4, 14)]
        public void GivenFiveInputs_Day1Part2_ReturnsCorrectResult(int value1, int value2, int value3, int value4, int value5, int expected)
        {
            _day1 = new Day1();
            var inputList = new List<int> { value1, value2, value3, value4, value5 };
            var result = _day1.Part2(inputList);
            Assert.Equal(expected, result);
        }
    }
}
