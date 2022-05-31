def arithmetic_mean(*args):
    sum = 0
    amount = 0
    for arg in args:
        sum += arg
        amount += 1
    return sum/amount

print(f'Cреднеарифметическое: {arithmetic_mean(1, 2, 3, 4, 5)}')

