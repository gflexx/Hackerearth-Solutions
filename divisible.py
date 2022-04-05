def solve (A, N):
    arr_list = list(A)
    half = int(N / 2)
    f_half = arr_list[:half]
    l_half = arr_list[-half:]
    f = ''
    l = ''
    for num in f_half:
        str_num = str(num)
        f += str_num[0]
    for num in l_half:
        str_num = str(num)
        l += str_num[-1:]
    final = f + l
    if int(final) % 11 == 0:
        return "OUI"
    else:
        return "NON"
    
N = int(input())
A = map(int, input().split())

out_ = solve(A,N)
print(out_)