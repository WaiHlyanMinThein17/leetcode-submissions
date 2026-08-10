class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            complement = running_sum - k

            if complement in prefix:
                count += prefix[complement]

            prefix[running_sum] = prefix.get(running_sum, 0) + 1

        return count