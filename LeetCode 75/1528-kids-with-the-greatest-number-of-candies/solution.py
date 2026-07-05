class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        extra = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                extra.append(True)
            else:
                extra.append(False)
        return extra
