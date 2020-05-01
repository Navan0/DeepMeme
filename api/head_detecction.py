import cv2
from api import app
import numpy as np

font = cv2.FONT_HERSHEY_PLAIN
font_scale = 1.7
rectangle_bgr = (0, 255, 0)
fontScale = 1
color = (128, 2550)
thickness = 2
face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')

def water_mark(image):
    oH,oW = image.shape[:2]
    image = np.dstack([image, np.ones((oH,oW), dtype="uint8") * 255])

    lgo_img = cv2.imread('logo.png',cv2.IMREAD_UNCHANGED)

    scl = 10
    w = int(lgo_img.shape[1] * scl / 30)
    h = int(lgo_img.shape[0] * scl / 30)
    dim = (w,h)
    lgo = cv2.resize(lgo_img, dim, interpolation = cv2.INTER_AREA)
    lH,lW = lgo.shape[:2]
    ovr = np.zeros((oH,oW,4), dtype="uint8")
    ovr[oH - lH - 60:oH - 60, oW - lW - 10:oW - 10] = lgo
    final = image.copy()
    final = cv2.addWeighted(ovr,0.5,final,1.0,0,final)
    cv2.imwrite("api/kids_detected.jpg", final)



def detect_head(image,text):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray)
    if len(faces) == 1:
        (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
        for x, y, width, height in faces:
            text_offset_x = x
            text_offset_y = y
            box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
            cv2.rectangle(image, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
            cv2.putText(image, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0), thickness=2)
            cv2.rectangle(image, (x, y), (x + width, y + height), color=(0, 255, 0), thickness=2)
        water_mark(image)
    else:
        return "Multiple faces in the image"
    # cv2.imwrite("api/kids_detected.jpg", image)
    # print("ok")
