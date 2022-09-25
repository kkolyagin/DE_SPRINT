def palindrom(a):
    return (a.replace(' ', '') ==a.replace(' ', '')[::-1])

x = ('taco cat','rotator','black cat')

for i in range(0,len(x)):
    print (f"Пример {i+1}:")
    print (f"Ввод: {x[i]}")
    print (f"Вывод: {palindrom(x[i])}")
    print()