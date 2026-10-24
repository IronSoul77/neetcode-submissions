class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for key in nums:
            if key not in freq:
                freq[key] = 0
            freq[key] += 1

        sorted_keys = sorted(freq, key=freq.get, reverse=True)

        return sorted_keys[:k]
            