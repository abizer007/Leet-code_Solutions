class Solution(object):
        def containsDuplicate(self, nums):
            # Create a set to store seen elements
            seen = set()

            # Iterate through the list
            for num in nums:
                # If the number is already in the set, return True
                if num in seen:
                    return True

                # Add the number to the set
                seen.add(num)

            # If no duplicates are found, return False
            return False

if __name__ == "__main__":
    solution = Solution()
