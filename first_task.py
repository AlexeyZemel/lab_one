import csv
import os

def write_annotation (dataset_path: str, csv_path: str) -> None:
    headings = ['Absolute way', 'Relative way', 'Class']
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headings, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writeheader()


path_to_dataset = 'E:\dataset'
csv_path = 'dataset.csv'
write_annotation(path_to_dataset, csv_path)