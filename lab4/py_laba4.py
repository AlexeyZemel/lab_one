import cv2
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


def filter_by_mark(df: pd.core.frame.DataFrame, mark: int) -> pd.core.frame.DataFrame:
    """
    Создание нового датафрейма, отфильтрованного по метке
    Ключевые аргуметы:
        df(pd.core.frame.DataFrame): исходный датафрейм
        mark(int): метка
    """
    return df[df.Mark == mark]


def filter_by_shape(
    df: pd.core.frame.DataFrame, mark: int, max_height: int, max_width: int
) -> pd.core.frame.DataFrame:
    """
    Создаёт новый датафрейм, отфильтрованный по метке и размерам
    Ключевые аргументы:
        df(pd.core.frame.DataFrame): исходный датафрейм
        mark(int): метка
        max_height(int): максимальный предел фильтрации по высоте
        max_width(int): максимальный предел фильтрации по ширине
    """
    return df[(df.Mark == mark) & (df.Height <= max_height) & (df.Width <= max_width)]


def grouping_df(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Группировка датафрейма по метке класса с вычислением максимального, минимального и среднего значения по количеству пикселей
    Ключевые аргументы:
        df(pd.core.frame.DataFrame): исходный датафрейм
    """
    rdf = df.loc[:, ["Mark", "Size"]]
    res_df = rdf.groupby("Mark").count()
    res_df["Min_Size"] = rdf["Size"].min()
    res_df["Min_Size"][0] = rdf[rdf.Mark == 0]["Size"].min()
    res_df["Min_Size"][1] = rdf[rdf.Mark == 1]["Size"].min()
    res_df["Average_Size"] = rdf["Size"].mean()
    res_df["Average_Size"][0] = rdf[rdf.Mark == 0]["Size"].mean()
    res_df["Average_Size"][1] = rdf[rdf.Mark == 1]["Size"].mean()
    res_df["Max_Size"] = rdf["Size"].max()
    res_df["Max_Size"][0] = rdf[rdf.Mark == 0]["Size"].max()
    res_df["Max_Size"][1] = rdf[rdf.Mark == 1]["Size"].max()
    res_df.drop(["Size"], axis=1, inplace=True)
    return res_df


def hist(
    df: pd.core.frame.DataFrame, mark: int
) -> np.ndarray[int, np.dtype[np.generic]]:
    """
    Строит гистограмму для случайного изображения из датафрейма с меткой mark
    Ключевые агрументы:
        df(pd.core.frame.DataFrame): исходный датафрейм
        mark(int): метка класса
    """
    random_numbers = list(range(0, 1050))
    random.shuffle(random_numbers)
    num = random.choice(random_numbers)
    n_df = df[df.Mark == mark]["Absolute_way"]
    img_path = n_df.iloc[num]
    image = cv2.imread(img_path)
    blue = []
    green = []
    red = []
    colors = (blue, green, red)
    for i in range(len(colors)):
        histg = cv2.calcHist([image], [i], None, [256], [0, 256])
        if i == 0:
            blue = histg
        if i == 1:
            green = histg
        if i == 2:
            red = histg
    return blue, green, red


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv", sep=" ")

    list1 = [0 for item in df.Class if item == "polarbears"]
    list2 = [1 for item in df.Class if item == "brownbears"]
    res = list1 + list2
    df["Mark"] = res

    height = []
    width = []
    depth = []

    for image in df.Absolute_way:
        img = cv2.imread(image)
        heig, wid, dep = img.shape
        height.append(heig)
        width.append(wid)
        depth.append(dep)

    df["Height"] = height
    df["Width"] = width
    df["Depth"] = depth

    df.describe()

    filtered_df = filter_by_mark(df, 1)

    filtered_df2 = filter_by_shape(df, 1, 320, 450)

    df["Size"] = df["Height"] * df["Width"]

    gr_df = grouping_df(df)

    bl, gr, rd = hist(df, 1)

    colors = {"b": bl, "g": gr, "r": rd}
    color = ("b", "g", "r")
    for i, col in enumerate(color):
        plt.plot(colors[col], color=col)
        plt.xlim([0, 256])
    plt.title("Image Histogram")
    plt.ylabel("Number of Pixels")
    plt.xlabel("Pixel Value")
    plt.show()
