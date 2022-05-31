list = []
print('Введите несколько строк')
while True:
    text = input()
    if text == 'q':
        break
    else:
        list.append(text)
print(list)
