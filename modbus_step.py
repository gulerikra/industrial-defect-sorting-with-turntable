# pip3 install pyModbusTCP==v0.1.10

import time
from pyModbusTCP.client import ModbusClient
import datetime
import cv2
from ultralytics import YOLO # YOLOv8 modeli için ultralytics kütüphanesini kullanıyoruz

cap = cv2.VideoCapture(1)
# Video çözünürlüğünü ayarlama
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

model = YOLO("model.pt")
server_host="192.168.3.250"
server_port=502
plc=ModbusClient()
plc.host(server_host)
plc.port(server_port)

while True:
    if not plc.open():
        print("unable to connect to"+server_host+":"+str(server_port))
        time.sleep(2)

    if plc.is_open():
        # Kameradan görüntüyü al
        ret, frame = cap.read()
        # Görüntüyü yeniden boyutlandırma
        resized_frame = cv2.resize(frame, (640,640), interpolation=cv2.INTER_CUBIC)
        # Nesne tespiti işlemini gerçekleştirmek için görüntüyü model kullanarak işleme sokuyoruz
        de_out=model.predict(source=resized_frame, conf=0.3, show=True, device='cpu')
        # Nesne tespiti sonucunda en az bir nesne tespit edilmişse
        if len(de_out) != 0:
            isCompress = 0
            img_copy = resized_frame.copy()

            # Tüm tespit edilen nesneler için
            for i in range(len(de_out[0])):
                boxes = de_out[0].boxes
                box = boxes[i]
                clsID = boxes.cls.numpy()[0]
                conf = box.conf.numpy()[0]
                bb = box.xyxy.numpy()[0]
                print(datetime.datetime.now()) # Tespit anını yazdır
                print(clsID) # Tespit edilen nesnenin sınıfını yazdır
                cv2.rectangle(img_copy, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), (0, 255, 0), 2)
                
                if clsID == 0:
                    plc.write_multiple_coils(5,[1])
                    print("eksik nesne tespit edildi")
                   
                elif clsID == 1:
                    plc.write_multiple_coils(6,[1]) 
                    print("dogru nesne tespit edildi")
                
