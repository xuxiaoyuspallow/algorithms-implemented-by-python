class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0
        grid_len = len(grid[0])
        for i,li in enumerate(grid):
            for j,k in enumerate(li):
                temp = 4
                if k == 0:
                    continue
                else:
                    if i > 0:
                        if grid[i-1][j]:
                            temp -= 1
                    if i < grid_len-1:
                        if grid[i+1][j]:
                            temp -= 1
                    if j > 0:
                        if grid[i][j-1]:
                            temp -= 1
                    if j < grid_len-1:
                        if grid[i][j+1]:
                            temp -= 1
            r += temp
        return r


if __name__ == '__main__':
    print(Solution().islandPerimeter([[1,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))