import requests
import shutil

FOLDER_DIR = "imgs/"

def download_imgs(url, name):
    file_name = FOLDER_DIR + name

    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(file_name, "wb") as f:
            shutil.copyfileobj(res.raw, f)
        print("Image downloaded successfully!")
    else:
        print("Status Code: {};".format(res.status_code))
        print("Couldn't get image!")