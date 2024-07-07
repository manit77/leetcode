"""

https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-05

1518. Water Bottles

There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:


Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

"""


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
       
        bottle_drank = numBottles
        remainder = 0
        
        while numBottles >= numExchange:
            remainder = numBottles % numExchange
            numBottles = (numBottles // numExchange)
            bottle_drank += numBottles
            numBottles = numBottles + remainder
                       
        return bottle_drank
    
    def checkResults(self, expected, result):      
        if expected != result:
            print("!!! test result failed, expected",
                    expected, " but got", result)
            return False

        print("test result passed, expected", expected, " and got ", result)
        return True

sol = Solution()
# result = sol.numWaterBottles(9, 3)
# sol.checkResults(13, result)

# result = sol.numWaterBottles(15, 4)
# sol.checkResults(19, result)

result = sol.numWaterBottles(15, 8)
sol.checkResults(17, result)



