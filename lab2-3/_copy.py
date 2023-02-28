import os
import csv
from tqdm import tqdm
import shutil


def write_copy(number: int, class_name: str, another_path: str, csv_path: str = "") -> None:

    """
    Записывает аннотации о копии в csv файл

    Ключевые аргументы:
        number (int): номер копии
        class_name (str): имя класса
        another_path (str): путь до другой директории
        csv_path(str, optional): путь до csv файла
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        write_in_file = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        write_in_file.writerow(
            {
                "Absolute way": another_path,
                "Relative way": f"dataset/another_dataset/{class_name}_{str(number).zfill(4)}.jpg",
                "Class": class_name,
            }
        )


def copy_to_another(path_to_another: str, path_to_dataset: str, csv_path: str = "") -> str or None:

    """
    Копирует данные из dataset в другую директорию

    Ключевые аргументы:
        path_to_another(str): путь до другой директории
        path_to_dataset(str): путь до dataset
        csv_path(str, optional): путь до csv файла
    """
    if not csv_path.find(".csv"):
        if not os.path.exists(path_to_another):
            os.mkdir(path_to_another)

        headings = ["Absolute way", "Relative way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
            )
            writer.writeheader()

        class_name = "polarbears"
        path_to_pbear = path_to_dataset + "/" + class_name
        sum_files = len(
            [
                fl
                for fl in os.listdir(path_to_pbear)
                if os.path.isfile(os.path.join(path_to_pbear, fl))
            ]
        )

        for i in tqdm(range(0, sum_files), colour="green"):
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another + f"/{class_name}_{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path, csv_path)

        class_name = "brownbears"
        path_to_pbear = path_to_dataset + "/" + class_name
        sum_files = len(
            [
                fl
                for fl in os.listdir(path_to_pbear)
                if os.path.isfile(os.path.join(path_to_pbear, fl))
            ]
        )

        for i in tqdm(range(0, sum_files), colour="green"):
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another + f"/{class_name}_{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path, csv_path)
    else:
        if not os.path.exists(path_to_another):
            os.mkdir(path_to_another)

        headings = ["Absolute way", "Relative way", "Class"]
        with open(os.path.join(path_to_another, "_another_dataset.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
            )
            writer.writeheader()

        class_name = "polarbears"
        path_to_pbear = path_to_dataset + "/" + class_name
        sum_files = len(
            [
                fl
                for fl in os.listdir(path_to_pbear)
                if os.path.isfile(os.path.join(path_to_pbear, fl))
            ]
        )

        for i in tqdm(range(0, sum_files), colour="green"):
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another + f"/{class_name}_{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path, os.path.join(path_to_another, "_another_dataset.csv"))

        class_name = "brownbears"
        path_to_pbear = path_to_dataset + "/" + class_name
        sum_files = len(
            [
                fl
                for fl in os.listdir(path_to_pbear)
                if os.path.isfile(os.path.join(path_to_pbear, fl))
            ]
        )

        for i in tqdm(range(0, sum_files), colour="green"):
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = path_to_another + f"/{class_name}_{str(i).zfill(4)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(i, class_name, new_path,os.path.join(path_to_another, "_another_dataset.csv"))

        return os.path.join(path_to_another, "_another_dataset.csv")

if __name__ == "__main__":
    path_to_dataset = "E:/dataset"
    path_to_another_dataset = "E:/dataset/another_dataset"
    copy_to_another(path_to_another_dataset, path_to_dataset)
