def Card(a):
    a1 = a[:-4]
    a2 = a[-4:]
    return '*'*len(a1)+a2


print(Card(a=input('Введите число:')))