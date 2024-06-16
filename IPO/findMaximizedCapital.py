import heapq


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        pq = []
        maxProfit = []
        for i in range(len(profits)):
            if capital[i] <= w:
                heapq.heappush(maxProfit, -profits[i])
            else:
                heapq.heappush(pq, (capital[i], -profits[i]))

        while k:
            if not maxProfit: break
            w += -heapq.heappop(maxProfit)
            while pq and pq[0][0] <= w:
                heapq.heappush(maxProfit, heapq.heappop(pq)[1])
            k -= 1

        return w
        