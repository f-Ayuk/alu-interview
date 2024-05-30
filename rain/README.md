##ALU INTERVIEW

The problem of trapping rainwater involves calculating the amount of water trapped between bars representing different elevations in an elevation map. When it rains, water accumulates between these bars, and the task is to determine the total amount of water trapped.

Here’s an algorithmic approach to solve this problem:

1. Brute Force Approach:
	- Iterate through each bar in the elevation map.
	- For each bar, find the highest bars on the left and right sides.
	- Take the smaller of the two heights.
	- The difference between the smaller height and the height of the current element is the amount of water that can be stored in this array element.
	- Sum up the water trapped for all bars to get the total amount of rainwater retained.

2. Example:
	- Consider an elevation map represented by the array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].
	- Visualize the elevation map and identify the areas where water can be trapped between the bars.
	- Calculate the amount of water trapped using manual calculations, following the water trapping process.

3. Time Complexity: The above approach has a time complexity of O(n) because we traverse the elevation map twice (once for left_max and once for right_max).

4. Space Complexity: The space complexity is O(n) due to the additional arrays left_max and right_max.

> Feel free to use this approach to calculate rainwater retention for any given elevation map! If you have further questions or need additional clarification, feel free to ask. 🌧️🚀
