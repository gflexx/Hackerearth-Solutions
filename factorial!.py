def find_factorials(num):
    n = num
    if n == 0:
        return n
    factors = []
    initial = 1
    while (n > 0):
        n -= initial
        factors.append(n)
    factors.remove(0)
    factors.append(num)
    result = 1
    for x in factors:
        result = result * x
    return result

num = int(input())
x = find_factorials(num)
print(x)