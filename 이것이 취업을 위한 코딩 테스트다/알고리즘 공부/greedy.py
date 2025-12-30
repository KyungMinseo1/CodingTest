# 거스름돈 greedy 알고리즘
def greedy_charge(n):
    coins = [500, 100, 50, 10]
    used = []
    for coin in coins:
        num_coin = n // coin
        n %= coin
        used.append(num_coin)
    return used

# 큰 수의 법칙 greedy 알고리즘
def greedy_big():
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    data_sorted = sorted(data)
    biggest_1 = data_sorted[N-1]
    biggest_2 = data_sorted[N-2]
    result = 0

    while True:
        for _ in range(K):
            if M == 0:
                break
            result += biggest_1
            M -= 1
        if M == 0:
            break
        result += biggest_2
        M -= 1
    return result

if __name__ == "__main__":
    result = greedy_big()
    print(result)

