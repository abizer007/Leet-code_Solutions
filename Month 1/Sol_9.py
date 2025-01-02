def merge(intervals):
    # Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        # If the list of merged intervals is empty or there is no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge the intervals by updating the end time of the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]

print(merge(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]
print(merge(intervals2))  # Output: [[1, 5]]
