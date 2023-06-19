# object-detection-gui-app
This was a task project for [The Sparks Foundation](https://www.linkedin.com/company/the-sparks-foundation) Summer Internship Program Batch September 2022.
A GUI object detection application based on [yolov3](https://pjreddie.com/darknet/yolo/) deep learning model which is a pretrained deep learning model trained on COCO data set of 80 objects. The application detects objects from the user webcam, where the user has the option to enable or disable the object detection feature. The user can log data about currently detected objects to be sent to a webserver through tcp socket. 


## Usage and Installation
1. Clone the github repo.
2. run ```pip install opencv-python``` to install opencv library.
3. run ```pip install PySimpleGUI``` to install PySimpleGUI library for GUI.
4. run ```python3 socket_server.py``` to start the socket server.
5. run ```python3 main.py``` to run the application.

Demo preview:

![Demo preview](https://im.ezgif.com/tmp/ezgif-1-bcb9c631a5.gif)

The application has an IOT feature where the user can log detected data to a socket server 
![image](https://user-images.githubusercontent.com/51798396/191473244-054cd984-d0fd-440c-b314-d7ed232fd7f7.png)


## File Structure
1. **socket_client.py**: script file for tcp client (Sends log data).
2. **socket_server.py**: script file for tcp socket server.
3. **main.py**: main application script where it init GUI, detects objects and send log of detected objects to a socket server. 
4. **yolo**: yolo directory that contains the yolov3 parameters data


