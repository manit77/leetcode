"""

https://leetcode.com/problems/sort-characters-by-frequency/?envType=daily-question&envId=2024-07-05

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        print("input", s)
        dic = {}

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        # sort by the value using the lamda
        sorted_chars = sorted(
            dic.items(), key=lambda item: item[1], reverse=True)

        # for c in sorted_chars:
        #     print(c[0], c[1])

        # generate the return string

        # rv = ""
        # for (key, value) in sorted_chars:
        #     print (key, value)
        #     rv = rv + (key * value)

        # simplified from above
        rv = "".join((key * value) for (key, value) in sorted_chars)

        print(rv)

        return rv

    def checkResults(self, expected, result):
        if expected == result:
            print("Passed expected ", expected, " and got ", result)
            return True
        print("Failed expected ", expected, " and got ", result)
        return False


sol = Solution()


result = sol.frequencySort("tree")
expected = "eetr"
sol.checkResults(expected, result)

result = sol.frequencySort("cccaaa")
expected = "cccaaa"
sol.checkResults(expected, result)

result = sol.frequencySort("Aabb")
expected = "bbAa"
sol.checkResults(expected, result)
