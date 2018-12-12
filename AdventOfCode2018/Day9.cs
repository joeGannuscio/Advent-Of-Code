using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;

namespace AdventOfCode2018
{
    public class Day9
    {
        private long _players = 448;
        private long _lastMarble = 71628;

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 9 Part 1 Solution: " + Part1(_players, _lastMarble));
            stringBuilder.Append("\nDay 9 Part 2 Solution: " + Part2(_players, _lastMarble));
            return stringBuilder.ToString();
        }

        public string Part1(long players, long lastMarble)
        {

            var gameList = new LinkedList<long>();
            var playerArray = new long[players];
            var currentMarble = gameList.AddFirst(0);
            
            for (var i = 1; i < lastMarble; i++)
            {
                if (i % 23 == 0)
                {

                    
                    //go back 7 marbles
                    for (var j = 0; j < 7; j++)
                    {
                        currentMarble = currentMarble.Previous ?? gameList.Last;
                    }

                    playerArray[i % players] += i + currentMarble.Value;
                    var removeMarble = currentMarble;
                    currentMarble = currentMarble.Next;
                    gameList.Remove(removeMarble);


                }
                else
                {
                    currentMarble = gameList.AddAfter(currentMarble.Next ?? gameList.First, i);
                }

                
            }

            var result = playerArray.Max();

            return result.ToString();
        }

        public string Part2(long players, long lastMarble)
        {
            var result = Part1(_players, _lastMarble * 100);
            return result;
        }
    }
}