def Word(a):
    if a[::-1] == a[::]:
        return 'Yes'
    else:
        return 'No'


print(Word(a=input('Введите слово:')))