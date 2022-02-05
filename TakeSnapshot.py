from tkinter import Frame, image_names
from tracemalloc import take_snapshot
from unicodedata import name
from unittest import result
import cv2
import random
import time
import dropbox

StartTime=time.time()

def TakeSnapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,Frame=videoCaptureObject.read()
        num=random.randint(1,99)
        image_name="picture"+str(num)+".jpg"
        cv2.imwrite(image_name,Frame)
        StartTime=time.time()
        result=False
        

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return image_name


def upload_file(img_name):
    access_token = 'BPDs8wNmarMAAAAAAAAAASqvGLZDqTylp2ZiOnO6xtk92e6vhIq4nqWsiANT7x77'
    
    file_from = img_name
    file_to = '/C102/'+img_name  # The full path to upload the file to, including the file name

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if (time.time()-StartTime>5):
            name=TakeSnapshot()
            upload_file(name)
            

  


main()
