import csv
import os
from tqdm import tqdm


def write_i_annotation(i: int, class_name: str, dataset_path: str) -> None:

    """
    Записывает аннотацию i-ого файла в csv файл
    Ключевые аргументы:
        i(int): номер файла, для которого пишется аннотация
        class_name(str): имя класса
        dataset_path(str): путь до директории с данными
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        write_in_file = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        path = f"E:/dataset/{class_name}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(path):
            write_in_file.writerow(
                {
                    "Absolute way": dataset_path
                    + f"/{class_name}/{str(i).zfill(4)}.jpg",
                    "Relative way": f"dataset/{class_name}/{str(i).zfill(4)}.jpg",
                    "Class": class_name,
                }
            )


def write_annotation(dataset_path: str, csv_path: str) -> None:

    """
    Записывает аннотации dataset в csv файл
    Ключевые аргументы:
        dataset_path(str): путь до данных, для которых пишутся аннотации
        csv_path(str): путь до csv файла, куда записываются аннотации
    """
    
    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        writer.writeheader()

    class_name = "polarbears"
    path_to_pbear = dataset_path + "/" + class_name
    sum_files = len(
        [
            fl
            for fl in os.listdir(path_to_pbear)
            if os.path.isfile(os.path.join(path_to_pbear, fl))
        ]
    )

    for i in tqdm(range(0, sum_files), colour="green"):
        write_i_annotation(i, class_name, dataset_path)

    class_name = "brownbears"
    path_to_pbear = dataset_path + "/" + class_name
    sum_files = len(
        [
            fl
            for fl in os.listdir(path_to_pbear)
            if os.path.isfile(os.path.join(path_to_pbear, fl))
        ]
    )

    for i in tqdm(range(0, sum_files), colour="green"):
        write_i_annotation(i, class_name, dataset_path)


if __name__ == "__main__":
    path_to_dataset = "E:\dataset"
    csv_path = "dataset.csv"
    write_annotation(path_to_dataset, csv_path)
    