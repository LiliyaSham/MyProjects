list = input().split()

def num_shift(s):
    res = 0
    if s.isalpha():
        res = len(s)
    else:
        for el in s:
            if el.isalpha():
                res += 1
    return res

def shift(s, n):
    new_s = ""
    for el in s:
        if el.isalpha() and el.islower():
            new_s += chr(((ord(el)) - 97 + n) % 26 + 97)
        elif el.isalpha() and el.isupper():
            new_s += chr(((ord(el)) - 65 + n) % 26 + 65)
        else:
            new_s += el
    return new_s

#print(list)
list2 = []
for el in list:
    num = num_shift(el)
    list2.append(shift(el, num))

print(*list2)

# for i in range(len(list)):
#    num = num_shift(list[i])
#    print(shift(list[i], num))
