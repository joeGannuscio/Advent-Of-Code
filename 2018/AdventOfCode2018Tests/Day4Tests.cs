﻿using System.Collections.Generic;
using AdventOfCode2018;
using Xunit;

namespace AdventOfCode2018Tests
{
    public class Day4Tests
    {
        [Fact]
        public void GivenSampleInput_Part1_ReturnsCorrectValue()
        {
            var sampleInput = new List<string>() { "[1518-11-01 00:00] Guard #10 begins shift", "[1518-11-01 00:05] falls asleep", "[1518-11-01 00:25] wakes up", "[1518-11-01 00:30] falls asleep", "[1518-11-01 00:55] wakes up", "[1518-11-01 23:58] Guard #99 begins shift", "[1518-11-02 00:40] falls asleep", "[1518-11-02 00:50] wakes up", "[1518-11-03 00:05] Guard #10 begins shift", "[1518-11-03 00:24] falls asleep", "[1518-11-03 00:29] wakes up", "[1518-11-04 00:02] Guard #99 begins shift", "[1518-11-04 00:36] falls asleep", "[1518-11-04 00:46] wakes up", "[1518-11-05 00:03] Guard #99 begins shift", "[1518-11-05 00:45] falls asleep", "[1518-11-05 00:55] wakes up" };
            var day4 = new Day4();
            var expected = "240";
            var result = day4.Part1(sampleInput);

            Assert.Equal(expected, result);
        }

        [Fact]
        public void GivenSampleInput_Part2_ReturnsCorrectValue()
        {
            var sampleInput = new List<string>() { "[1518-11-01 00:00] Guard #10 begins shift", "[1518-11-01 00:05] falls asleep", "[1518-11-01 00:25] wakes up", "[1518-11-01 00:30] falls asleep", "[1518-11-01 00:55] wakes up", "[1518-11-01 23:58] Guard #99 begins shift", "[1518-11-02 00:40] falls asleep", "[1518-11-02 00:50] wakes up", "[1518-11-03 00:05] Guard #10 begins shift", "[1518-11-03 00:24] falls asleep", "[1518-11-03 00:29] wakes up", "[1518-11-04 00:02] Guard #99 begins shift", "[1518-11-04 00:36] falls asleep", "[1518-11-04 00:46] wakes up", "[1518-11-05 00:03] Guard #99 begins shift", "[1518-11-05 00:45] falls asleep", "[1518-11-05 00:55] wakes up" };
            var day4 = new Day4();
            var expected = "4455";
            var result = day4.Part2(sampleInput);

            Assert.Equal(expected, result);
        }
    }
}