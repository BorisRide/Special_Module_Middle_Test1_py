from datetime import datetime

def note_id_data():
    # присвоение ID заметке
    with open('data.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        num_last_id = len(data) - 5
        note_id = int(data[num_last_id]) + 1
    return note_id

def title_data():
    title = input('Введите заголовок заметки: ')
    return title

def note_data():
    note = input('Введите заметку: ')
    return note

def note_time_data():
    note_time = datetime.now().strftime("%Y-%m-%d")
    return note_time
