class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time O(1)
        # Space O(1)

        # Constraints: -1000 <= a, b <= 1000

        mask = 0xffffffff # binary of int -1

        while (b & mask) > 0:
            a, b = (a ^ b), (a & b) << 1
        
        return (a & mask) if b > 0 else a