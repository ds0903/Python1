import time
import requests
import os
import threading
from pathlib import Path
import multiprocessing

start_time = time.perf_counter()
image_url = "https://picsum.photos/1000/1000"
download_counter = 0
encryption_counter = 0


# CPU-bound task (heavy computation)
def encrypt_file(path: Path):
    print(f"Processing file from {path} in process {os.getpid()}")
    # Just simulate a heavy computation
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    # Процеси
    process = multiprocessing.Process(
        target=encrypt_file, args=(Path("rockyou.txt"),)
    )
    process.start()
    process.join()
    encryption_counter += 1
    #

    # Потоки
    thread = threading.Thread(target=download_image, args=(image_url,))
    thread.start()
    thread.join()
    download_counter += 1
    #

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Взагалом витрачено часу на виконання {total_time}")


# try:

#     encrypt_file("rockyou.txt")
#     download_image(image_url)
#     print(f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total_time} seconds")
# except Exception as e:
#     print(f"Error occurred: {e}")
