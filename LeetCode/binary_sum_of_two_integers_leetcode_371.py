class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time O(1)
        # Space O(1)

        # Constraints: -1000 <= a, b <= 1000

        bitShortner = 0xffffffff

        while (b & bitShortner) > 0:
            a, b = (a ^ b), (a & b) << 1
        
        return (a & bitShortner) if b > 0 else a