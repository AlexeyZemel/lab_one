import os
import csv

def get_item(class_name: str, csv_path: str, count: int) -> str or None:
    
    '''
        Функция возвращает путь элемента следующего за count, если элемента нет
        возвращает None

        Ключевые аргументы:
            class_name(str): метка класса
            csv_path(str): путь csv файла
            count(int): номер элемента
    '''
    
    path_to_class = 'E:/dataset/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_class) if os.path.isfile(os.path.join(path_to_class, fl))])
    if count + 1 < sum_files:
        rows = []
        headings = ['Absolute way', 'Relative way', 'Class']
        with open(csv_path, 'r', encoding = 'utf8') as file:
                read = csv.DictReader(file, fieldnames = headings, delimiter = ';')
                for row in read:
                    if row['Class'] == class_name:
                        rows.append([row['Absolute way'], row['Relative way'], row['Class']])
        row_dict = {headings[k]:rows[count + 1][k] for k in range(0, len(headings))}
        return row_dict['Absolute way']
    else: return None
