import os
import multiprocessing
import threading
import requests
import asyncio
import time
import aiohttp


URLS = [
    "https://w.forfun.com/fetch/91/9169909f3e45e394aafe6ea01c974ccd.jpeg",
    "https://img.razrisyika.ru/kart/32/1200/125975-peyzazhi-prirody-23.jpg",
    "https://74foto.ru/800/600/https/img-fotki.yandex.ru/get/97201/127908635.1418/0_1ac2f7_fa876a0_orig.jpg",
    "https://w.forfun.com/fetch/f1/f13df778bc8ba462ffc43d9eee4651bb.jpeg",
    "https://vsegda-pomnim.com/uploads/posts/2022-04/1650916178_25-vsegda-pomnim-com-p-krasivie-peizazhi-gor-foto-32.jpg",
]


def download_image(url):
    response = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Загружено  {filename}")


if __name__ == "__main__":
    start_time = time.time()
    for url in URLS:
        download_image(url)
    print(f"Обычная функция работала:{time.time()- start_time} секунд")

    start_time = time.time()

    threads = []
    for url in URLS:
        t = threading.Thread(target=download_image, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print(f"Многопоточный вариант работал: {end_time - start_time} секунд")

    start_time = time.time()

    processes = []
    for url in URLS:
        p = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    print(f"Многопроцессорный вариант работал: {end_time - start_time} секунд")

    async def download_image(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                filename = os.path.basename(url)
                with open(filename, "wb") as f:
                    f.write(await response.read())
                    print(f"Загружено {filename}")

    start_time = time.time()

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(download_image(url)) for url in URLS]
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.time()

    print(f"Ассинхроная функция работала: {end_time - start_time} секунд")