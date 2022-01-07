import pandas as pd
import numpy as np
import cv2

b = g = r = xpos = ypos = 0


def mouse_click_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:  # left button double click
        global b, g, r, xpos, ypos, mouseClick
        mouseClick = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


mouseClick = False

img_path = "C://Users//dsaum//Downloads//colours.jpg"
img = cv2.imread(img_path)

index = ["color", "hex", "R", "G", "B"]
#data = pd.read_csv("colors.csv", names=index, header=None)

cv2.namedWindow("Color Detect")
cv2.setMouseCallback("Color Detect", mouse_click_function)

while (1):

    cv2.imshow("Color Detect", img)
    if mouseClick:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # cv2.putText(img,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
