import cv2
import numpy as np
import pandas as pd

cv2.namedWindow("image")

index = ["Colour", "Colour_name", "Hex", "R", "G", "B"]
data = pd.read_csv("colors.csv", names=index, header=None)


def nothing(x):
    pass


cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

def colour_name(R, G, B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G - int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            colourname = data.loc[i, "Colour_name"]
    return colourname


while (1):
    img = np.zeros([550, 550, 3], np.uint8)
    jppg = np.zeros([55, 550, 3], np.uint8)
    R = cv2.getTrackbarPos("R", "image")
    G = cv2.getTrackbarPos("G", "image")
    B = cv2.getTrackbarPos("B", "image")
    jppg[:] = [B, G, R]
    img[:] = [B, G, R]
    line_type = cv2.LINE_AA
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = colour_name(R, G, B) + ' R=' + str(R) + ' G=' + str(G) + ' B=' + str(B)
    cv2.putText(img, text, (28, 20), font, 0.7, (255, 255, 255), 1,  cv2.LINE_AA)
    if (R+G+B >= 600):
        cv2.putText(img, text, (28, 20), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    cv2.imshow("image", img)

cv2.destroyAllWindows()
