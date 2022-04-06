def count_divisors(num_set):
    l, r, k = list(num_set)
    divisible = []
    for num in range(l, (r + 1)):
        if num % k == 0:
            divisible.append(num)
    return divisible.__len__()

num_set = map(int, input().split())
x = count_divisors(num_set)
print(x)