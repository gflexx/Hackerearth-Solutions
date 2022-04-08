def check_divisibility(data):
    l_nums = ''
    for x in data:
        n_str = str(x)
        l_nums += n_str[-1]
    if int(l_nums) % 10 == 0:
        return 'Yes'
    else:
        return 'No'

N = int(input())
data = [int(x) for x in input().split()]

ans = check_divisibility(data)
print(ans)