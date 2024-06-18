class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs_difficulty_profit = list(zip(difficulty, profit))
        jobs_difficulty_profit.sort()
        worker.sort()

        max_profit_so_far = 0

        for i in range(len(jobs_difficulty_profit)):
            max_profit_so_far = max(max_profit_so_far, jobs_difficulty_profit[i][1])
            jobs_difficulty_profit[i] = (jobs_difficulty_profit[i][0], max_profit_so_far)

        total_profit = 0
        i = 0
        for w in worker:

            while i < len(jobs_difficulty_profit) and w >= jobs_difficulty_profit[i][0]:
                i += 1
            if i > 0:
                total_profit += jobs_difficulty_profit[i - 1][1]

        return total_profit

sol = Solution()

# Example 1 -> Output: 100
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

print(sol.maxProfitAssignment(difficulty, profit, worker))


# Example 2 -> Output: 0
difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]

print(sol.maxProfitAssignment(difficulty, profit, worker))
