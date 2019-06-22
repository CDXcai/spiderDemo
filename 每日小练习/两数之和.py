# coding:utf8

# cbefg
string = 'abcbefgf'
str_list = []
str_len = 0
str_index = 0
for i in  range(len(string)-1):
    str_list.append([])
    for j in string[i:]:
        if j in str_list[i]:
            if len(str_list[i])>str_len:
                str_len,str_index  = len(str_list[i]),i
            break
        str_list[i].append(j)
print ''.join(str_list[str_index])
