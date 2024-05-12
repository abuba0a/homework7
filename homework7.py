# Вариант 1

def print_params():
    print('Params - 1')
    print('Params - 2')


print_params()
print_params()
print_params()

print('Конец')
print()


# Вариант 2

def print_params():
    for i in ['Params - 1', 'Params - 2']:
        print(i)


print_params()
print_params()
print_params()

print('Конец')