class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queues,xy_sum,xy_dif):
            p = len(queues)
            if p == n:
                results.append(queues)
                return
            for q in range(n):
                if q not in queues and (p + q) not in xy_sum and (p - q) not in xy_dif:
                    dfs(queues + [q], xy_sum + [p + q], xy_dif + [p - q])
        results = []
        dfs([],[],[])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in results]