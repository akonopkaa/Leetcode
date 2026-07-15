class Solution:
    def equalPairs(self, grid):
        rows = cols = len(grid)
        transposed = []
        m_dict = {}

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = str(grid[i][j])

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(grid[j][i])
            transposed.append(row)
        
        for i in range(rows):
            a = ",".join(grid[i])
            if a in m_dict:
                m_dict[a] += 1
            else:
                m_dict[a] = 1

        ans = 0
        for i in range(rows):
            a = ",".join(transposed[i])
            ans += m_dict.get(a, 0)

        return(ans)
