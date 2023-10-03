import argparse
from multiprocessing import Process
import os
import time
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


processes = []
start_time = time.time()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in image_urls:
        process = Process(target=img_saver, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')