from datetime import date 
from datetime import datetime

# проверка валидности даты
def is_valid_date(yyyy, mm, dd):
    try: 
            dd = date(yyyy, mm, dd)
    except: 
            return False
    return True



def list_to_num(date_insert): # запись года, месяца, дня по отдельным переменным
    # извлекаем год, как число
    y = []
    for i in range(0, 4):
        y.append(date_insert[i])
    y = ''.join(y)
    y = int(y)
            
    # извлекаем месяц, как число
    m = []
    for i in range(5, 7):
        m.append(date_insert[i])
    m = ''.join(m)
    m = int(m)
                        
    # извлекаем день, как число
    d = []
    for i in range(8, 10):
        d.append(date_insert[i])
    d = ''.join(d)
    d = int(d)

    return y, m, d


def true_date(date_of_note): # проверка валидности даты
    date_is_rihgt = True
    y = int
    m = int
    d = int
    y, m, d = list_to_num(date_of_note)

    if len(date_of_note) == 10: # проверка валидности даты по длине ввода даты (ввод даты по паттерну)
        if date_of_note[4] == "-" and date_of_note[7] == "-": # проверка валидности даты по паттерну
            date_is_rihgt = is_valid_date(y, m, d)
        else:
            date_is_rihgt = False
    else:
        date_is_rihgt = False
        
    return date_is_rihgt

def compare(date_one, date_two): # сравнение дат, какая больше
    date1 = datetime.strptime(date_one, '%Y-%m-%d')
    date2 = datetime.strptime(date_two, '%Y-%m-%d')
    if date1 < date2:
        return True
    else: 
        return False
