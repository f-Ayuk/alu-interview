#!//usr/bin/python3

def rain(walls):
    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height on the left for each bar
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate the maximum height on the right for each bar
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the trapped water for each bar
    total_water = 0
    for i in range(n):
        water_at_i = min(left_max[i], right_max[i]) - walls[i]
        total_water += max(water_at_i, 0)

    return total_water

# Example usage:
elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain(elevation_map))  # Output: 6
