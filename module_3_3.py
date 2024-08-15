def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)  # Результат: '1 25 True'
print_params(c=[1, 2, 3])  # Результат: '1 строка [1, 2, 3]'
print('--------------------')

values_list = [25, 'Мустанг', 2.5]
values_dict = {'a': 'RAM 1500', 'b': 2012, 'c': False}

print_params(*values_list)
print_params(**values_dict)
print('--------------------')

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)