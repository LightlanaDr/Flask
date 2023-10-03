import argparse
from threading import Thread
import time
import os
import requests

image_urls = []
with open('images.txt', 'r') as images:
    for image in images.readlines():
        image_urls.append(image.strip())

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


def img_saver(url):
    response = requests.get(url)
    filename = f'{url.split("/")[-1]}'
    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


threads = []
start_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


# for url in create_parser():   # for args via cmd
for url in image_urls:
    thread = Thread(target=img_saver, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')