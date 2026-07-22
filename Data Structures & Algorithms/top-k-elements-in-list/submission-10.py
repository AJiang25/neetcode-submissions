class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        # the index is now the frequency
        # each number can be the same so we + 1
        bucket = [[] for _ in range(len(nums) + 1)]

        # Get the frequencies
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # append them to the bucket using the freq as the index
        for num, count in freq.items():
            bucket[count].append(num)
        
        # pick the top k num from the buckets in reverse
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
