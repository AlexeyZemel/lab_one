import os
import csv

def get_item(i: int, class_name: str, csv_path:str) -> str or None:
    rows = []
    headings = ['Absolute way', 'Relative way', 'Class']
    with open(csv_path, 'r', encoding = 'utf8') as file:
            read = csv.DictReader(file, fieldnames = headings, delimiter = ';')
            for row in read:
                if row['Class'] == class_name:
                    rows.append([row['Absolute way'], row['Relative way'], row['Class']])
    row_dict = {headings[k]:rows[i][k] for k in range(0, len(headings))}
    print (row_dict['Absolute way'])
    


if __name__ == '__main__':
    class_name = 'polarbears'
    csv_path = 'dataset.csv'
    path_to_class = 'E:/dataset/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_class) if os.path.isfile(os.path.join(path_to_class, fl))])
    count = [i for i in range(0, sum_files)]
    get_item(count[45], class_name, csv_path)