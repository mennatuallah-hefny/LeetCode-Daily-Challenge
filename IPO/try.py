# Output: 4
import heapq


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

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

print(w)