class Solution:
    def largestAltitude(self, gain):
        current = 0
        max_gain = 0
        for g in gain:
            current = current + g
            max_gain = max(max_gain, current)
        return max_gain
