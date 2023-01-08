# P-adic-Presentation
Python code to demonstrate the existence of p-adic numbers
Inspired by the video demonstration in: https://www.youtube.com/watch?v=3gyHKCDq1YA&t=532s

The code is setup so that a user may experiment with different inputs to look for patterns in the way a sequence of increasing powers evolves.

Not all inputs result in interesting patterns, or even patterns at all. The easiest way to find a triangle pattern, similar to the one shown in the video, is to use an input with power = base, and change the starting_value until you get your desired result. It is recommended to keep depth = accuracy so that the matplotlib results look square. The code will run quickly regardless of the accuracy and depth parameters, so feel free to put any value you wish. (The table representation may become unreadable with high values of depth and/or accuracy)

Input used in the video: starting_value = 2, depth = 60, accuracy = 100, power = 10, base = 10.
