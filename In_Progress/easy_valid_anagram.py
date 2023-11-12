class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        CountS, CountT = {}, {}

        if len(s) != len(t):
            return False

        # for i in range(len(s)):
        #    countS[z] =


        # first solution: doesn't handle case for duploicate characters
        # hashset = set()
        # for n in s:
        #     hashset.add(n)
        #
        # for m in t:
        #     if m not in hashset:
        #         return False
        #     return True
        #
