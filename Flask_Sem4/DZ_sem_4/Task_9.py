# Задание
#
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.


import argparse
import os
import time
from pathlib import Path
import requests

PATH = 'images'
count_time = 0

image_urls = []
with open('images.txt', 'r') as images:
    for image in images.readlines():
        image_urls.append(image.strip())

if not os.path.isdir("images"):
    os.mkdir("images")


def download_image_response(images: list):
    global count_time
    for url in images:
        image_path = Path('images')
        start_time = time.time()

        response = requests.get(url, stream=True).content
        filename = image_path.joinpath(os.path.basename(url))

        f = open(filename, 'wb')
        f.write(response)
        f.close()
        end_time = time.time() - start_time
        count_time += end_time
        print(f"Downloaded {filename} in {end_time:.2f} seconds")
    print(f'Всего на скачивание затрачено {count_time}')


if __name__ == "__main__":
    download_image_response(image_urls)

