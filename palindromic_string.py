def check_palindrome(string):
    s_list = []
    s_list[:0] = string
    r_list = [x for x in reversed(s_list)]
    r_string = ''
    for i in r_list:
        r_string += i
    if string == r_string:
        return 'YES'
    else:
        return 'NO'

string = input()
x = check_palindrome(string)
print(x)