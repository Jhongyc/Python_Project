# Author:GaoYuCai
import heapq
nums=[1,3,2,4,6,0,90]
print(heapq.nlargest(1,nums))
print(heapq.nsmallest(2,nums))
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap=heapq.nsmallest(1,portfolio,key=lambda s:s["price"])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(cheap,expensive)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)