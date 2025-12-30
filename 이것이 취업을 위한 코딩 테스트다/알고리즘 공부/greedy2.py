# 숫자 카드 게임
def card_greedy():
    n, m = map(int, input().split())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, input().split())))
    result = 0
    for row in cards:
        min_val = min(row)
        if min_val > result:
            result = min_val
    return result

# 1이 될 때까지
def until_one_greedy():
    n, k = map(int, input().split())
    count = 0
    while True:
        if n == 1:
            break
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1
    return count

if __name__=="__main__":
    print(until_one_greedy())