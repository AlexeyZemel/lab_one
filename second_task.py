import os
import csv
from tqdm import tqdm
import shutil

def write_copy(number: int, class_name: str, another_path: str) -> None:
    headings = ['Absolute way', 'Relative way', 'Class']
    with open('another_dataset.csv', 'a', newline='', encoding='utf-8') as f:
        write_in_file = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
        write_in_file.writerow({'Absolute way': another_path,
                                'Relative way': f'dataset/another_dataset/{class_name}_{str(i).zfill(4)}.jpg',
                                        'Class': class_name})     

def copy_to_another(path_to_another: str, path_to_dataset: str) -> None:
    if not os.path.exists(path_to_another):
        os.mkdir(path_to_another)

    headings = ['Absolute way', 'Relative way', 'Class']
    with open('another_dataset.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writeheader() 

    class_name = 'polarbears'
    path_to_pbear = path_to_dataset + '/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_pbear) if os.path.isfile(os.path.join(path_to_pbear, fl))])

    for i in tqdm(range(0, sum_files), colour= 'green'):
            path = path_to_pbear + f'/{str(i).zfill(4)}.jpg'
            new_path = path_to_another + f'/{class_name}_{str(i).zfill(4)}.jpg'
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path)
    
    class_name = 'brownbears'
    path_to_pbear = path_to_dataset + '/' + class_name
    sum_files = len([fl for fl in os.listdir(path_to_pbear) if os.path.isfile(os.path.join(path_to_pbear, fl))])

    for i in tqdm(range(0, sum_files), colour= 'green'):
            path = path_to_pbear + f'/{str(i).zfill(4)}.jpg'
            new_path = path_to_another + f'/{class_name}_{str(i).zfill(4)}.jpg'
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path)

path_to_dataset = 'E:/dataset'
path_to_another_dataset = 'E:/dataset/another_dataset'
copy_to_another(path_to_dataset, path_to_another_dataset)