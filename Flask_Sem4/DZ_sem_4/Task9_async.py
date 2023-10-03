import asyncio
import aiohttp
import time
import argparse
import os

image_urls = []
with open('images.txt', 'r') as images:
    for image in images.readlines():
        image_urls.append(image.strip())

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


async def img_saver(url):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        async with session.get(url) as response:
            cont = await response.read()
            filename = f'{url.split("/")[-1]}'
            with open(f'images/{filename}', 'wb') as f:
                f.write(cont)
                print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


async def main():
    tasks = []
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in image_urls:
        task = asyncio.ensure_future(img_saver(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')