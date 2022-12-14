import os
import csv
import random
import shutil
from tqdm import tqdm


def write_copy(class_name: str, random_path: str, csv_path: str = "") -> None:

    """
    Записывает аннотации о копии в csv файл

    Ключевые аргументы:
        class_name (str): имя класса
        random_path (str): путь до другой директории
        csv_path(str, optional): путь до csv файла
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        write_in_file = csv.DictWriter(
            f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        write_in_file.writerow(
            {
                "Absolute way": random_path,
                "Relative way": os.path.relpath(random_path),
                "Class": class_name,
            }
        )


def copy_to_random(dataset_path: str, random_path: str, csv_path: str = "") -> str or None:

    """
    Копирует файлы из dataset в новую директорию с именем файла из рандомных чисел
    и записывает аннотации в csv файл

    Ключевые аргументы:
        dataset_path(str): путь до dataset
        random_path(str): путь до директории, куда копируются файлы
        csv_path(str, optional): путь до csv файла
    """
    if not csv_path.find(".csv"):
        if not os.path.exists(random_path):
            os.mkdir(random_path)

        headings = ["Absolute way", "Relative way", "Class"]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
            )
            writer.writeheader()

        random_numbers = list(range(0, 10001))
        random.shuffle(random_numbers)
        random_num1 = random_numbers[: len(random_numbers) // 2]
        random_num2 = random_numbers[len(random_numbers) // 2 :]

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
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = random_path + f"/{str(random_num1[i]).zfill(5)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(class_name, new_path, csv_path)

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
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = random_path + f"/{str(random_num2[i]).zfill(5)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(class_name, new_path, csv_path)

    else:
        if not os.path.exists(random_path):
            os.mkdir(random_path)

        headings = ["Absolute way", "Relative way", "Class"]
        with open(os.path.join(path_to_random, "_random_dataset.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
            )
            writer.writeheader()

        random_numbers = list(range(0, 10001))
        random.shuffle(random_numbers)
        random_num1 = random_numbers[: len(random_numbers) // 2]
        random_num2 = random_numbers[len(random_numbers) // 2 :]

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
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = random_path + f"/{str(random_num1[i]).zfill(5)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(class_name, new_path, os.path.join(path_to_random, "_random_dataset.csv"))

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
            path = path_to_pbear + f"/{str(i).zfill(4)}.jpg"
            new_path = random_path + f"/{str(random_num2[i]).zfill(5)}.jpg"
            if os.path.isfile(path):
                shutil.copyfile(path, new_path)
                write_copy(class_name, new_path, os.path.join(path_to_random, "_random_dataset.csv"))

        return os.path.join(path_to_random, "_random_dataset.csv")

if __name__ == "__main__":
    path_to_dataset = "E:/dataset"
    path_to_random = "E:/dataset/random_dataset"
    copy_to_random(path_to_dataset, path_to_random)
