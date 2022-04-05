str_input = input()
str_list = list(str_input) 
z_count = str_list.count('z')
o_count = str_list.count('o')
if (z_count * 2) == o_count:
    print('Yes')
else:
    print('No')
