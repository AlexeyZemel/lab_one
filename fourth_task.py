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
    rows = []
    headings = ['Absolute way', 'Relative way', 'Class']
    with open(csv_path, 'r', encoding = 'utf8') as file:
            read = csv.DictReader(file, fieldnames = headings, delimiter = ';')
            for row in read:
                if row['Class'] == class_name:
                    rows.append([row['Absolute way'], row['Relative way'], row['Class']])
    if count + 1 < len(rows):
        row_dict = {headings[k]:rows[count + 1][k] for k in range(0, len(headings))}
        return row_dict['Absolute way']
    else: return None

if __name__ == '__main__':
    for i in range(0,1050):
        item = get_item('brownbears', 'another_dataset.csv', i)
        print(item)
        