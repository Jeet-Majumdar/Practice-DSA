"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # https://www.youtube.com/watch?v=H9bfqozjoqs
        # Time O(amount*len(coins))
        # Memory O(amount)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

        # # Recursion based own solution
        # # Based on explaination https://www.youtube.com/watch?v=H9bfqozjoqs
        # coins.sort(reverse=True)
        # df = {i:1 for i in coins}
        # df[0] = 0
        # def _minFinder(val):
        #     if val < 0:
        #         return -1
        #     if val in df.keys():
        #         return df[val]
        #     list_options = []
        #     for i in coins:
        #         opt = _minFinder(val - i)
        #         if opt > 0:
        #             list_options.append(opt)
        #     if len(list_options) > 0:
        #         df[val] = min(list_options)+1
        #     else:
        #         df[val] = -1
        #     #print(list_options, val, df)
        #     return df[val]
        
        # return _minFinder(amount)
