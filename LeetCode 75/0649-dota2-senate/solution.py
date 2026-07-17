class Solution:
    def predictPartyVictory(self, senate):
        senate_queue = list(senate)
        n = len(senate_queue)
        radiant = []
        dire = []
        for i in range(n):
            if senate_queue[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.pop(0)
                radiant.append(radiant.pop(0) + n)
            else:
                radiant.pop(0)
                dire.append(dire.pop(0) + n)
        if radiant:
            return "Radiant"
        else:
            return "Dire"
