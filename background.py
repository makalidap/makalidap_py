import ctypes
import requests
from io import BytesIO
from PIL import Image
import os
import time

url = "https://picsum.photos/1920/1080"

while True:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    path = os.getcwd() + "\\background.jpg"
    img.save(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    time.sleep(5)
