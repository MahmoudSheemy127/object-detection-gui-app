# object-detection-gui-app
object detection GUI app


This is a simple object detection application based on yolov3 deep learning model which is a pretrained deep learning model trained on COCO data set of 80 objects

yolov3 https://pjreddie.com/darknet/yolo/

the application is simply a GUI application where it shows the users web cam. The user has the option to enable or disable the object detection feature


![image](https://user-images.githubusercontent.com/51798396/191471755-30ddc84a-b98d-435e-95e9-1a26502c90be.png)


The GUI has been developed using PySimpleGUI library https://www.pysimplegui.org/en/latest/ 



The application has an IOT feature where the user can log detected data to a socket server 
![image](https://user-images.githubusercontent.com/51798396/191473244-054cd984-d0fd-440c-b314-d7ed232fd7f7.png)

The python socket programming has been developed using python socket library


This makes it a practical IOT application for users who don't have access to the monitoring feature where they can just access the server to fetch information about the detection
objects in the monitoring area.
