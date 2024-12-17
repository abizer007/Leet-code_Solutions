class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left, current_sum, min_length = 0, 0, float('inf')

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

                # Early exit: If minimum length is 1, we can't do better
                if min_length == 1:
                    return 1

        return min_length if min_length != float('inf') else 0
