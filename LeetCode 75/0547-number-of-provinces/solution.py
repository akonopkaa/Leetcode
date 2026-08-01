class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(self, i, isConnected):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(self, j, isConnected)
        for i in range(n):
            if i in visited:
                continue
            provinces += 1
            dfs(self, i, isConnected)
        return provinces
