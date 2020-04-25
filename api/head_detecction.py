import cv2
from api import app

font = cv2.FONT_HERSHEY_PLAIN
font_scale = 1.7
rectangle_bgr = (0, 255, 0)
fontScale = 1
color = (128, 2550)
thickness = 2
face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')


def detect_head(image,text):
    image = cv2.imread(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray)
    print(f"{len(faces)} faces detected in the image.")
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
    for x, y, width, height in faces:
        text_offset_x = x
        text_offset_y = y
        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
        cv2.rectangle(image, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
        cv2.putText(image, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0), thickness=2)
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(0, 255, 0), thickness=2)
    cv2.imwrite("api/kids_detected.jpg", image)
    print("ok")
