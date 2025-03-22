def change_data_file(start, stop, id, ch_title, ch_note, ch_time): 
# функция изменения данных в файле data.csv
    # start начальная строка файла, с которой начинается замена данных
    # stop конечная строка файла, на которой заканчивается замена данных
    
    with open('data.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        data_list_left = []    # часть файла слева от изменяемой записи
        data_list_right = []   # часть файла справа от изменяемой записи
        data_list_middle = []  # список с новой записью

        for i in range(start):
            data_list_left.append(data[i])
        for j in range(stop, len(data)):
            data_list_right.append(data[j])
        for k in range(1, 5):
            if k == 1:
                data_list_middle.append(f'{id}\n')
            elif k == 2:
                data_list_middle.append(f'{ch_title}\n')
            elif k == 3:  
                data_list_middle.append(f'{ch_note}\n')
            elif k == 4:
                data_list_middle.append(f'{ch_time}\n\n')
            
        # сшивка заметок и запись в файл
        data = data_list_left + data_list_middle + data_list_right
                
        with open('data.csv', 'w', encoding='utf-8') as f:
            for o in range(len(data)):
                f.write(f'{data[o]}')
