def bin2dec(s):
    n = 1
    out = 0
    for i in s[::-1]:
        if i == '1': out += n
        n <<=1
    return out

def dec2bin(s):
    out=''
    while s > 0:
        out = str(s % 2) + out
        s = s // 2
    return out

x1 = "111"
x2 = "101"

print ("Пример 1:")
print (f"Ввод: x1 = {x1} и x2 = {x2}")
print ("Вывод:",dec2bin(bin2dec(x1)*bin2dec(x2)))
print()