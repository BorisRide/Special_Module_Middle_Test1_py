def delete_data_file(start, stop):
# функция удаления данных заметки из файла data
    # start начальная строка файла, с которой начинается удаление данных
    # stop  конечная строка файла, на которой заканчивается удаление данных
    
    with open('data.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        data_list_left = []    # часть файла слева от удаляемой записи
        data_list_right = []   # часть файла справа от удаляемой записи
        data_list_middle = []  # список с новой записью
        
        for i in range(start):
            data_list_left.append(data[i])
        for j in range(stop, len(data)):
            data_list_right.append(data[j])
                    
        # сшивка заметок и запись в файл
        data = data_list_left + data_list_middle + data_list_right
                
        with open('data.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data)):
                f.write(f'{data[o]}')
    