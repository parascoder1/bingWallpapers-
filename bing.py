import requests
import shutil
import os
import subprocess
import threading
import time
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=7"
req_obj = requests.get(url)
wallpapers = []
if req_obj.status_code == 200:
    json = req_obj.json()
    json = json['images']
    for i,values in enumerate(json):
        img_url = "http://www.bing.com" + values['url']
        image = requests.get(img_url, stream=True)
        # name = values['copyright'].replace(' ', '_') + ".jpg"
        with open("image" + str(i) + ".jpg", 'wb') as f:
            shutil.copyfileobj(image.raw, f)
        del image
        address = os.path.dirname(os.path.realpath(__file__)) + "/image" + str(i) + ".jpg"
        wallpapers.append(address)
    index = 0
    while (1):
        file_path = wallpapers[index]
        index = (index + 1)%len(wallpapers)
        command = "gconftool-2 --set \
                /desktop/gnome/background/picture_filename \
                --type string '%s'" % file_path
        subprocess.call(command,shell=True)
        print(file_path)
        time.sleep(10)

else:
    print("not giving a proper response")
