import os
import string
import time
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
import cv2
import urllib.request
import random
import numpy as np
from tqdm import tqdm

if not os.path.isdir("E:\dataset"):
    os.mkdir("E:\dataset")

if not os.path.isdir("E:\dataset\\brownbears"):
    os.mkdir("E:\dataset\\brownbears")

if not os.path.isdir("E:\dataset\polarbears"):
    os.mkdir("E:\dataset\polarbears")

pbear_path = "E:\dataset\polarbears"
bbear_path = "E:\dataset\\brownbears"


def get_images(count_imgs, path, name):

    count = 0

    for i in tqdm(range(3, 999), desc="Страница ", colour="green"):

        letters = string.ascii_lowercase
        rand_string = "".join(random.sample(letters, 10)) 
        _headers = {"User-Agent": rand_string}

        url = f"https://yandex.ru/images/search?p={i}&text={name}&"  # формируем ссылку запроса
        html_page = requests.get(url, headers=_headers)  # получаем хтмл страницы

        soup = BeautifulSoup(
            html_page.text, "html.parser"
        )  # данная переменная содержит весь код страницы

        src_list = []

        for link in soup.find_all(
            "img", class_="serp-item__thumb justifier__thumb"
        ):  # находим все элементы с нужным тегом и классом и добавляем его "соурс" в список
            src_list.append(link.get("src"))

        for img_url in tqdm(src_list, desc="Скчивание картинок ", colour="green"):
            if img_url.find("n=13") != -1:
                try:
                    source = "https:" + img_url
                    picture = requests.get(source)  # извлекаем данные по ссылке

                    name_file = str(count)

                    fpicture = open(path + "/" + name_file.zfill(4) + ".jpg", "wb")
                    fpicture.write(
                        picture.content
                    )  # записываем в файл контент в байтах
                    fpicture.close()

                    time.sleep(0.25)

                    count += 1
                    if count == count_imgs:
                        return

                except Exception:
                    print("Error in: ", count)

count_find = 1050

get_images(count_find, pbear_path, "polar bear")

print("Пауза")
for sec in range(1, 61):
    print("Осталось ", 61 - sec)
    time.sleep(1)

get_images(count_find, bbear_path, "brown bear")

