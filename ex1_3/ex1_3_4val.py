def valid_br(string1):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    for i in range(len(brackets_open)):
        valid = string1.count(brackets_open[i])-string1.count(brackets_closed[i])==0
        if not(valid): break
    return valid

x = ('[{}({})]','{]','{')

for i in range(len(x)):
    print ("Пример {i+1}:")
    print (f"Ввод: x = {x[i]}")
    print ("Вывод:",valid_br(x[i]))
    print()