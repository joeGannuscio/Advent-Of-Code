using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace AdventOfCode2018
{
    public class Day4
    {
        private string _inputPath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "InputFiles/Day4Input.txt");
        private List<string> _input = new List<string>();

        public Day4()
        {
            _input = InputReader(_inputPath);
        }

        public string GetResults()
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.Append("Day 4 Part 1 Solution: " + Part1(_input));
            stringBuilder.Append("\nDay 4 Part 2 Solution: " + Part2(_input));
            return stringBuilder.ToString();
        }

        public string Part1(List<string> input)
        {
            var eventList = EventReader(input).OrderBy(e => e.Timestamp);
            var guardList = ProcessGuardDetails(eventList.ToList());

            var sleepyGuard = guardList.Aggregate((g, h) => g.MinutesSlept > h.MinutesSlept ? g : h);
            var sleepyMinute = sleepyGuard.MinuteDictionary.Aggregate((m, n) => m.Value > n.Value ? m : n);

            var result = sleepyMinute.Key * sleepyGuard.Id;

            return result.ToString();
        }

        public string Part2(List<string> input)
        {
            var guardList = ProcessGuardDetails(EventReader(input).OrderBy(e => e.Timestamp).ToList());

            var maxGuard = new Guard();
            var maxGuardMaxMin = 0; 
            foreach (var guard in guardList)
            {
                if (guardList.First() == guard)
                {
                    maxGuard = guard;
                    maxGuardMaxMin = guard.MinuteDictionary.Aggregate((m, n) => m.Value > n.Value ? m : n).Value;
                }
                if (guard.MinuteDictionary.Any())
                {
                    if (guard.MinuteDictionary.Aggregate((m, n) => m.Value > n.Value ? m : n).Value > maxGuardMaxMin)
                        maxGuard = guard;
                }
                

            }

            var result = maxGuard.Id * maxGuard.MinuteDictionary.Aggregate((m, n) => m.Value > n.Value ? m : n).Key;

            return result.ToString();
        }

        private List<Guard> ProcessGuardDetails(List<Entry> entries)
        {
            var guardList = new List<Guard>();
            var id = 0;

            foreach (var entry in entries)
            {

                if (entry.Event.Contains("Guard"))
                {
                    id = Convert.ToInt32(Regex.Split(entry.Event, "\\D+")[1]);
                    if (!guardList.Exists(g => g.Id == id))
                    {
                        guardList.Add(new Guard()
                        {
                            Id = id
                        });
                    }
                    continue;
                }

                if (entry.Event.Contains("falls"))
                {
                    var curGuard = guardList.First(g => g.Id == id);
                    curGuard.StartSleep = entry.Timestamp;
                    continue;
                }

                if (entry.Event.Contains("wakes"))
                {
                    var curGuard = guardList.First(g => g.Id == id);
                    curGuard.StopSleep = entry.Timestamp;

                    //process sleep details
                    var span = curGuard.StopSleep.Subtract(curGuard.StartSleep);
                    curGuard.MinutesSlept = curGuard.MinutesSlept + (int)span.TotalMinutes;

                    var startMin = curGuard.StartSleep.Minute;
                    var stopMin = curGuard.StopSleep.Minute;

                    for (var i = startMin; i < stopMin; i++)
                    {
                        if (curGuard.MinuteDictionary.ContainsKey(i))
                        {
                            curGuard.MinuteDictionary[i]++;
                        }
                        else
                        {
                            curGuard.MinuteDictionary.Add(i, 1);
                        }
                    }
                }
            }

            return guardList;
        }

        private List<string> InputReader(string inputPath)
        {
            var inputList = new List<string>();

            var fileStream = File.OpenRead(inputPath);
            var streamReader = new StreamReader(fileStream);
            string line;
            while ((line = streamReader.ReadLine()) != null)
            {
                inputList.Add(line);
            }

            return inputList;
        }

        private List<Entry> EventReader(List<string> input)
        {
            var entries = new List<Entry>();

            foreach (var entry in input)
            {
                entries.Add(new Entry()
                {
                    Timestamp = Convert.ToDateTime(entry.Substring(1, 16)),
                    Event = entry.Substring(19)
                });
            }

            return entries;
        }

    }

    public class Guard
    {
        public Guard()
        {
            MinuteDictionary = new Dictionary<int, int>();
            MinutesSlept = 0;
        }

        public int Id { get; set; }
        public int MinutesSlept { get; set; }
        public DateTime StartSleep { get; set; }
        public DateTime StopSleep { get; set; }
        public Dictionary<int,int> MinuteDictionary { get; set; }
    }

    public class Entry
    {
        public DateTime Timestamp { get; set; }
        public string Event { get; set; }
    }
}
