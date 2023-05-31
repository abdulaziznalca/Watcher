import cv2
import time
import os
import datetime

cameraId = 0
path = ''  # Yakalanan görüntünün kaydedileceği yol
naming = '%Y-%m-%d--%H-%M-%S'
extension = '.jpg'  # Yakalanan görüntünün hangi dosya uzantısı ile kaydedileceği belirlendi.
interval = 5  # Görüntülerin kaç saniye aralıklarla alınacağı belirtildi.


def capture_image() -> None:
    cap = cv2.VideoCapture(cameraId)
    ret, frame = cap.read()
    cap.release()

    if ret and frame is not None:
        image_name = datetime.datetime.today().strftime(naming) + extension
        cv2.imwrite(os.path.join(path, image_name), frame)


while True:
    capture_image()
    time.sleep(interval)
