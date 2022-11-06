import csv
import os

class Iterator:
    def __init__(self, class_name: str, path: str) -> None:
        
        '''
            Инициализирует объект класса итератор

            Ключевые аргументы:
                class_name(str): имя класса
                path(str): путь до csv файла
        '''

        self.class_name = class_name
        self.path = path
        self.counter = 0
        self.list = []

        if os.path.exists(self.path):
            headings = ['Absolute way', 'Relative way', 'Class']
            with open(self.path, 'r', encoding = 'utf8') as f:
                read = csv.DictReader(f, fieldnames = headings, delimiter = ';')
                for row in read:
                    if row['Class'] == class_name:
                        self.list.append([row['Absolute way'], row['Relative way'], row['Class']])
        else: 
            raise FileNotFoundError
        
    def __iter__(self):
        return self

    def __next__(self) -> None:
        
        '''
            Функция переключения на следующий экземпляр в списке, возвращает
            путь до этого экземпляра
        '''

        if self.counter < len(self.list):
            self.counter +=1
            return self.list[self.counter][0]
        elif self.counter == len(self.list):
            raise StopIteration

if __name__ == '__main__':
    iter = Iterator ('polarbears', 'dataset.csv')
    for j in iter:
        print (j)