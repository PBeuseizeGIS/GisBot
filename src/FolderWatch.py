# print("JESUS IS LORD")
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
from typing import IO, TextIO, BinaryIO
##############
import asyncio
import myBDK
from myBDK import UtilsMethods

class FileEventHandler(FileSystemEventHandler):
    def __init__(self,streamId:str) -> None:
        self.streamId = streamId
        #super().__init__()
    def on_created(self, event):
        if event.is_directory:
            return
        event_path = event.src_path
        if event_path.endswith('.txt'):          
            time.sleep(1)
            with open(event_path, 'r') as file:
                content = file.read()
                #content = content.decode() # convert bytes content to string
                #file.seek(0) #to set the pointer to the start of the file
                um = UtilsMethods()
                try:
                    content_tosend = um.text_parser(content)
                    send_to_symphony(content_tosend,self.streamId)
                except Exception as err:
                    print("Problem sending message to Symphony")
                    print(err)
            print(event_path)
        elif event_path.endswith(('.csv','xlsx')):
            time.sleep(1)
            with open(event_path, 'rb') as file:
                #content = file.read()
                #content = content.decode() # convert bytes content to string
                #file.seek(0) #to set the pointer to the start of the file
                #um = UtilsMethods()
                #asyncio.run(myBDK.run_bdk(content))
                try:
                    content_tosend = "" #um.text_parser(content)
                    send_to_symphony(content_tosend,self.streamId,file)
                except Exception as err:
                    print("Problem sending message to Symphony")
                    print(err)
        else:
            pass
            

def send_to_symphony(message:str,streamId:str,file_to_send:IO=None):
    asyncio.run(myBDK.run_bdk(message,streamId,file_to_send))
#     if response.status_code == 200:
#         print('Message sent to Symphony successfully')
#     else:
#         print('Failed to send message to Symphony')


# def send_to_symphony(message):
#     symphony_api_url = 'https://symphony.com/api/messages'
#     headers = {'Authorization': 'Bearer your_access_token'}
#     data = {'message': message}
#     response = requests.post(symphony_api_url, headers=headers, json=data)
#     if response.status_code == 200:
#         print('Message sent to Symphony successfully')
#     else:
#         print('Failed to send message to Symphony')


def start_file_watcher():
    folder_roomID_path = r'X:\GIS Tools\GISBot\DataBank\FolderWatched_SymphonyChatRoomID.txt'
    with open(folder_roomID_path,'r') as file:
        strRepDict  = file.read()

    # Converting the string representation of the dictionary into an actual dict
    dictFolderStreamId = eval(strRepDict)
    # dictFolderStreamId = {
    #     "X:\GIS Tools\SymphonyFileWatcher":"wsXxwGntMFd87PnnKbcbu3___nCDx_PodA",
    # "X:\GIS Tools\GISBot\AU_Placement":"C8gUler01SJ209dG3ciit3___nJ5i4ZkdA",
    # "X:\GIS Tools\XtraBot":"wsXxwGntMFd87PnnKbcbu3___nCDx_PodA"}
    for wd,sid in dictFolderStreamId.items():
        watchDirectory = wd
        streamId = sid
        time.sleep(1)
        event_handler = FileEventHandler(streamId)
        observer = Observer()
        observer.schedule(event_handler, path=watchDirectory, recursive=False)
        observer.start()
    try: 
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    print("File watcher running now")
    start_file_watcher()
