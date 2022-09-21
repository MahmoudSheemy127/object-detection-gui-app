import PySimpleGUI as sg
import cv2 as cv
import numpy as np
import os
from socket_client import Client_Socket
from object_detection import Yolo


#initialize some stuff
IP="192.168.1.20"
PORT=8000

#initialize yolov3
yolo = Yolo()
yolo.yolov3_model_init()

#initialize client_socket
client = Client_Socket()

#build GUI
row1 = [[sg.Text("Object detection software",font=50,justification='center')]]
col1_row2 = [[sg.Image(filename="",size=(500,500),key="-STREAM-")]]
col2_row2 = [[sg.Radio("Activate model",'Radio', key="-MODEL-ENABLE-")],[sg.Radio("Deactivate model",'Radio',True, key="-MODEL-DISABLE-")],[sg.Button("Log data",enable_events=True,key="-LOG-DATA-")]] 
row2 = [[sg.Col(col1_row2),sg.VSeparator(),sg.Col(col2_row2)]]
layout = [[row1],[row2]]

window = sg.Window("Object detection app", layout=layout)
#enter the loop

#start webcam video
vid = cv.VideoCapture(0)

client.initialize_socket(IP,PORT)
while 1:
    event,values = window.read(timeout=20)
    #print(values)
    ret,frame = vid.read()  

    if(values["-MODEL-ENABLE-"]):
        #print("Showing object detection")
        frame = yolo.yolov3_object_detect(frame)
    
    elif(not values["-MODEL-ENABLE-"]):
        print("Showing normal video")

    if(event == "-LOG-DATA-"):
        print("sending log")
        for obj in yolo.objects:
            client.send_data(obj)
        
        #print(yolo.objects)

    imgbytes = cv.imencode(".png",frame)[1].tobytes()
    window["-STREAM-"].update(data=imgbytes)
    if event == sg.WIN_CLOSED:
        break

client.close_connection()
vid.release()
window.close()

