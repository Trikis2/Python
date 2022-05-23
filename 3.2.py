Password = "QWERTY12345"
while True:
    Entered_password = input("Введите пароль: ")
    if Entered_password == Password or Entered_password == 'q':
        break
    else:
        print('Пароль введен неверно')