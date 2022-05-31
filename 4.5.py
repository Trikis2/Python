list1 = ["Санкт-Петербург", "Москва", "Казань"]
list2= ["Воронеж", "Санкт-Петербург", "Иваново"]
list3 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list3.append(i)
        list2.remove(i)
print(f'Города, которые есть только в одном списке: {list2}')
print(f'Города, которые есть в обоих списках: {list3}')
