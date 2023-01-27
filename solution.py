class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = []
        val = []
        output = []
        for i in range(1,len(nums),2):
            freq = nums[i-1]
            val = nums[i]
            for j in range(freq):
                output.append(val)
        return output
