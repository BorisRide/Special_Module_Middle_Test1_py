from logger import input_data, print_data, print_data_by_number, change_data, print_data_by_date, delete_data

def interface():
    print("\nПривет! Программа Заметки готова к работе, \nперечень доступных режимов:")
    print("\n1 - запись заметки \n2 - вывод списка заметок \n3 - вывод заметки по ID")
    print("4 - выборка заметок по дате создания заметки \n5 - редактирование заметки \n6 - удаление заметки")
    command = int(input('Выберите нужный режим работы: '))

    while command != 1 and command != 2 and command != 3 and command != 4 and command !=5 and command !=6:
        # проверка правильности ввода данных пользователем
        print("Неправильный ввод, такого режима нет.\nПовторите ввод: ")
        command = int(input('Выберите нужный режим работы: '))

    if command == 1:
        input_data() # вызов функции ввода заметки и записи данных в файл
    elif command == 2:
        print_data() # вызов функции вывода всего списка заметок
    elif command == 3:
        print_data_by_number() # вызов функции вывода заметки по ID
    elif command == 4:
        print_data_by_date() # вызов функции выборки заметок по дате создания
    elif command == 5:
        change_data() # вызов функции перезаписи заметки
    elif command == 6:
        delete_data() # вызов функции удаления заметки
    