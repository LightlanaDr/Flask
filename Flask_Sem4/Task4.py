# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.
import os

import requests
import threading
import time

PATH = 'file'
count = 0


def get_amount_worlds(filename: str) -> None:
    global count
    with open(filename, encoding='utf-8') as f:
        count += len(f.read().split())
        print(f'tekuchee{count}')


if __name__ == '__main__':
    threads = []

    for root, dirs, files in os.walk(PATH):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            thread = threading.Thread(target=get_amount_worlds, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f'count={count}')
