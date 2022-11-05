import csv
import os
from tqdm import tqdm

def write_annotation (dataset_path: str, csv_path: str) -> None:
    headings = ['Absolute way', 'Relative way', 'Class']
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writeheader() 

    class_name = 'polarbears'
    path_to_pbear = dataset_path + '/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_pbear) if os.path.isfile(os.path.join(path_to_pbear, fl))])

    for i in tqdm(range(0, sum_files), colour='green'):
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            write_in_file = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
            path = f'E:/dataset/{class_name}/{str(i).zfill(4)}.jpg'
            if os.path.isfile(path):
                write_in_file.writerow({'Absolute way': dataset_path + f'/{class_name}/{str(i).zfill(4)}.jpg',
                                        'Relative way': f'dataset/{class_name}/{str(i).zfill(4)}.jpg',
                                        'Class': class_name})                                    

    class_name = 'brownbears'
    path_to_pbear = dataset_path + '/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_pbear) if os.path.isfile(os.path.join(path_to_pbear, fl))])

    for i in tqdm(range(0, sum_files), colour='green'):
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            write_in_file = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
            path = f'E:/dataset/{class_name}/{str(i).zfill(4)}.jpg'
            if os.path.isfile(path):
                write_in_file.writerow({'Absolute way': dataset_path + f'/{class_name}/{str(i).zfill(4)}.jpg',
                                        'Relative way': f'dataset/{class_name}/{str(i).zfill(4)}.jpg',
                                        'Class': class_name})

path_to_dataset = 'E:\dataset'
csv_path = 'dataset.csv'
write_annotation(path_to_dataset, csv_path)