import cv2 as cv
import numpy as np
import os


class Yolo:
    def __init__(self):
        self.yolo_weight_path = os.path.join(os.getcwd(),"yolo","yolov3.weights")
        self.yolo_config_path = os.path.join(os.getcwd(),"yolo","yolo_config.cfg")
        self.yolo_class_path = os.path.join(os.getcwd(),"yolo","yolo.txt")
        self.classes = []
        self.confidences = []
        objects = []

    #start the model
    def yolov3_model_init(self):
        #initialize classes list
        f = open(self.yolo_class_path,"r")
        self.classes = [word for word in f.read().split('\n')]
        self.yolo = cv.dnn.readNet(self.yolo_weight_path,self.yolo_config_path)
        self.COLORS = np.random.uniform(0,255,size=(len(self.classes),3))

    def get_output_layers(self,net):    
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers

    def draw_bounding_box(self,x,y,w,h,class_id,img):
        label = self.classes[class_id]
        self.objects.append(label)
        color = self.COLORS[class_id]
        cv.rectangle(img,(x,y),(x+w,y+h),color,1)
        cv.putText(img,label,(x+10,y+10),cv.FONT_HERSHEY_SIMPLEX,0.5,color,2)

    def yolov3_object_detect(self,frame):
        
        img = frame
        WIDTH=img.shape[1]
        HEIGHT=img.shape[0]
        SCALE=0.00392

        #we convert the img to a blob file which is easier for the model to fed on
        blob = cv.dnn.blobFromImage(img,SCALE, (416,416), (0,0,0), True, crop=False)

        self.yolo.setInput(blob)

        #get_output_layers(yolo_model)
        res = self.yolo.forward(self.get_output_layers(self.yolo))


        conf_threshold = 0.5
        nms_threshold = 0.4

        confidences = []
        boxes = []
        class_ids = []

        for layer in res:
            for grid in layer:
                scores = grid[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if(confidence > 0.5):
                    #get the bounding box dimensions
                    center_x = int(grid[0] * WIDTH)
                    center_y = int(grid[1] * HEIGHT)
                    width = int(grid[2] * WIDTH)
                    height = int(grid[3] * HEIGHT)
                    x = int(center_x - width / 2)
                    y = int(center_y - height / 2)
                    confidences.append(confidence)
                    class_ids.append(class_id)
                    boxes.append([x,y,width,height])
            

    
        #apply NMS
        indices = cv.dnn.NMSBoxes(boxes,confidences,conf_threshold,nms_threshold)

        self.objects = []
        #get indices after NMS
        for i in indices:
            self.draw_bounding_box(*boxes[i],class_ids[i],img)
        
        return img

#object_detection script

