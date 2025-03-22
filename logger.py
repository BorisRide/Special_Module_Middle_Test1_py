from data_create import note_id_data, title_data, note_data, note_time_data
from data_change import change_data_file
from data_delete import delete_data_file
from data_date import true_date, compare


def input_data():
# функция ввода и записи данных в файл
    
    note_id = note_id_data()
    title = title_data()
    note = note_data()
    time = note_time_data()
    var = int(input(f"\nБудут записаны следующие данные:\n\n"       
    f"{note_id}\n{title}\n{note}\n{time}\n\n"
    f"Выберите: 1 - записать, 2 - отменить запись заметки: ")) 

    while var != 1 and var != 2: 
        # проверка правильности ввода даннных 
        print("Неправильный ввод.\n")
        var = int(input('Повторите ввод: 1 - записать, 2 - отменить запись заметки :'))

    if var == 1:
        with open('data.csv', 'a', encoding='utf-8') as f:
            f.write(f"{note_id}\n{title}\n{note}\n{time}\n\n")
        print('Даные записаны в файл data.csv')
    elif var == 2:
        print('Даные не сохранены')
    

def print_data():
# функция вывода на консоль всех заметок

    print('Вывожу все заметки списком: \n')
    with open('data.csv', 'r', encoding='utf-8') as f:
        data_note = f.readlines()
        data_note_list = []
        j = 4 # запись в массив файл с пятой строки, без инициирующей заметки
        for i in range(4, len(data_note)): # запись в массив файл с пятой строки, без инициирующей заметки
            if data_note[i] == '\n' or i == len(data_note) - 1:
                data_note_list.append(''.join(data_note[j:i+1]))
                j = i
        print(''.join(data_note_list)) # вывод на печать файла


def print_data_by_number():
# функция вывода данных на консоль заметок по ID
    
    id = False
    switch = True
    while id == False:
        if switch == True:
            # первый вывод запроса ID
            print("Введите ID заметки, которую необходимо найти: ")
        else:
            # повторный вывод запроса ID, в том случае если введённый ID невалидный
            print("Заметки с таким ID нет в файле с заметками,\nпроверьте и повторите ввод ID: ")
        prn_id = int(input())
        while prn_id == 0:
            print("Ошибка ввода, ID не может быть нулевым")
            prn_id = int(input('Заново введите ID заметки, которую необходимо найти: '))
        
        with open('data.csv', 'r', encoding='utf-8') as f:
            data_note = f.readlines()
            data_note_list = []
            data_id = []
            prn_str = 0
            
            # выборка ID в список data_id
            j = 0
            for i in range(0, len(data_note), 5):
                data_id.append(int(data_note[i]))
                j +=1
            
            # поиск ID в списке data_id
            for i in range(len(data_id)):                
                if data_id[i] == prn_id:
                    id = True
                    prn_str = i * 5

                    # вывод на печать заметки с заданным ID
                    print('Вывожу данные заметки: \n')
                    start = prn_str        # начальная строка файла, с которой начинается вывод данных
                    stop = prn_str + 5     # конечная строка файла, на которой заканчивается вывод данных
                    for i in range(start, stop):
                        data_note_list.append(''.join(data_note[i]))
                    print(''.join(data_note_list))

                else:
                    switch = False


def print_data_by_date():
# функция вывода данных на консоль по дате заметки

    # ввод даты начала выборки заметок по дате 
    print("Введите начальную дату выборки заметок в формате ГГГГ-ММ-ДД: ")
    first_date = input()
    date_is = true_date(first_date) # проверка даты на правильность
    while date_is == False:
        print("Ошибка ввода, такой даты не существует\nили формат ввода даты неправильный.")
        first_date = input('Заново введите дату начала выборки заметок: ')
        date_is = true_date(first_date) # проверка даты на правильность

    # ввод даты окончания выборки заметок по дате 
    print("Введите конечную дату выборки заметок в формате ГГГГ-ММ-ДД: ")
    second_date = input()
    date_is = true_date(second_date) # проверка даты на правильность
    while date_is == False:
        print("Ошибка ввода, такой даты не существует\nили формат ввода даты неправильный.")
        second_date = input('Заново введите дату начала выборки заметок: ')
        date_is = true_date(second_date) # проверка даты на правильность

    # сравнение дат начала и конца выборки
    compare_is = compare(first_date, second_date)
    if compare_is == True:
        start_date = first_date
        stop_date = second_date
    else:
        start_date = second_date
        stop_date = first_date

    # подбор заметок для печати
    with open('data.csv', 'r', encoding='utf-8') as f:
        data_note = f.readlines()
        data_note_list = []
        data_note_point = []
                
        # отбор номеров строк для печати заметок по интервалу выборки дат
        for i in range(3, len(data_note), 5):
            str_data_note_i = data_note[i].strip()
            
            if compare(str_data_note_i, start_date) == False and compare(str_data_note_i, stop_date) == True:
                # выборка в массив номера строки по дате, если она равна или больше начальной и меньше конечной
                a = int(i)
                data_note_point.append(a)
            elif str_data_note_i == stop_date: # выборка в массив номера строки по дате, если она равна конечной
                a = int(i)
                data_note_point.append(a)
            else:
                i = i + 5
        
        # вывод на печать заметки по номеру строки
        print('Вывожу данные по заданному интервалу: \n')
        
        for l in range(0, len(data_note_point)):
            start = data_note_point[l] - 3      # начальная строка файла, с которой начинается вывод данных
            stop = start + 5                    # конечная строка файла, на которой заканчивается вывод данных
            for m in range(start, stop):
                data_note_list.append(''.join(data_note[m]))
        print(''.join(data_note_list))
        
            
def change_data():
# функция корректировки данных в файле заметок по ID
         
    id = False
    switch = True
    while id == False:
        if switch == True:
            # первый вывод запроса ID
            print("Введите ID заметки, которую необходимо изменить: ")
        else:
            # повторный вывод запроса ID, в том случае если введённый ID невалидный
            print("Заметки с таким ID нет в файле с заметками,\nпроверьте и повторите ввод ID: ")
        change_id = int(input())
        while change_id == 0:
            print("Ошибка ввода, ID не может быть нулевым")
            change_id = int(input('Заново введите ID заметки, которую необходимо изменить: '))
        
        with open('data.csv', 'r', encoding='utf-8') as f:
            data_note = f.readlines()
            data_id = []
            change_str = 0
            
            # выборка ID в список data_id
            j = 0
            for i in range(0, len(data_note), 5):
                data_id.append(int(data_note[i]))
                j +=1
            
            # поиск ID в списке data_id
            for i in range(len(data_id)):
                
                if data_id[i] == change_id:
                    id = True
                    change_str = i * 5
                    change_start = change_str        # начальная строка файла, с которой начинается заметка
                    change_stop = change_str + 5     # конечная строка файла, на которой заканчивается заетка
                    
                    # ввод новых данных заметки
                    print('Введите данные для обновления заметки: ')
                    title = title_data()
                    note = note_data()
                    time = note_time_data()

                    # замена данных в выбранном файле
                    change_data_file(change_start, change_stop, change_id, title, note, time)
                    print('\nЗаметка изменена.')
                                        
                else:
                    switch = False


def delete_data():
# функция удадения данных из файла заметок по ID (ЗВЕРШЕНО)
         
    id = False
    switch = True
    while id == False:
        if switch == True:
            # первый вывод запроса ID
            print("Введите ID заметки, которую необходимо удалить: ")
        else:
            # повторный вывод запроса ID, в том случае если введённый ID невалидный
            print("Заметки с таким ID нет в файле с заметками,\nпроверьте и повторите ввод ID: ")
        prn_id = int(input())
        while prn_id == 0:
            print("Ошибка ввода, ID не может быть нулевым")
            prn_id = int(input('Заново введите ID заметки, которую необходимо удалить: '))
        
        with open('data.csv', 'r', encoding='utf-8') as f:
            data_note = f.readlines()
            data_id = []
            prn_str = 0
            
            # выборка ID в список data_id
            j = 0
            for i in range(0, len(data_note), 5):
                data_id.append(int(data_note[i]))
                j +=1
            
            # поиск ID в списке data_id
            for i in range(len(data_id)):
                
                if data_id[i] == prn_id:
                    id = True
                    prn_str = i * 5
                    del_start = prn_str        # начальная строка файла, с которой начинается удаление данных
                    del_stop = prn_str + 5     # конечная строка файла, на которой заканчивается удаление данных
                    
                    # удаление данных в выбранном файле
                    delete_data_file(del_start, del_stop)
                    print('Заметка удалена.')

                else:
                    switch = False
