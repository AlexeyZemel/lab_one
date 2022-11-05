import os
import csv
from tqdm import tqdm

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

    for i in tqdm(range(0, sum_files)):
            path = path_to_pbear + f'/{str(i).zfill(4)}.jpg'
            new_path = path_to_another + f'/{class_name}_{str(i).zfill(4)}.jpg'
                

path_to_dataset = 'E:/dataset'
path_to_another_dataset = 'E:/dataset/another_dataset'
copy_to_another(path_to_dataset, path_to_another_dataset)