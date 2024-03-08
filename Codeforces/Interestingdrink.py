def binarySearch(low, high, coin):
    while low <= high:
        mid = (low + high) // 2
        if coin < prices[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low


n = int(input())
prices = list(map(int, input().split()))
prices.sort()
days = int(input())

for _ in range(days):
    coin = int(input())
    val = binarySearch(0, len(prices) - 1, coin)
    print(val)