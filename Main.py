import pytesseract
import cv2
from pytesseract import Output
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img1 = cv2.imread('3642684.jpg')

def Pan_num(img1):
    data1 = pytesseract.image_to_data(img1, output_type=Output.DICT)
    keys = list(data1.keys())
    pattern= '[A-Za-z]{5}\d{4}[A-Za-z]{1}'
    n_boxes = len(data1['text'])
    for i in range(n_boxes):
        if int(data1['conf'][i]) > 60:
            if re.match(pattern, data1['text'][i]):
                (x1, y1, w1, h1) = (data1['left'][i], data1['top'][i], data1['width'][i], data1['height'][i])
                img = cv2.rectangle(img1, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)




def dob(img1):
    data = pytesseract.image_to_data(img1, output_type=Output.DICT)
    keys = list(data.keys())
    date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:
            if re.match(date_pattern, data['text'][i]):
                (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                img = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)


Pan_num(img1)
dob(img1)
cv2.imshow('Result', img1)
cv2.waitKey(0)
