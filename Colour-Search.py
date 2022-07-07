import cv2
import numpy as np
import pandas as pd

# Creating a window and naming it "image"
cv2.namedWindow("image")

# Reading colors.csv and assigning indexes to it
index = ["Colour", "Colour_name", "Hex", "R", "G", "B"]
data = pd.read_csv("colors.csv", names=index, header=None)


def nothing(x):
    pass


# Creates trackbars for R G B values in the image window
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
# Trackbar for user to choose to display RGB value or Hex Value
cv2.createTrackbar("Hex = 0, \n RGB = 1", "image", 0, 1, nothing)


# Function to get colour name
def colour_name(R, G, B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G - int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            colourname = data.loc[i, "Colour_name"]
    return colourname


# Function to get Hex Value
def hex_value(R, G, B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G - int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            hexvalue = data.loc[i, "Hex"]
    return hexvalue


while (1):
    # Creates a blank image
    img = np.zeros([550, 550, 3], np.uint8)
    # Gets values from our treackbar
    R = cv2.getTrackbarPos("R", "image")
    G = cv2.getTrackbarPos("G", "image")
    B = cv2.getTrackbarPos("B", "image")
    switch = cv2.getTrackbarPos("Hex = 0, \n RGB = 1", "image")

    # Assigns RGB values to the image img colour
    img[:] = [B, G, R]
    line_type = cv2.LINE_AA
    font = cv2.FONT_HERSHEY_SIMPLEX
    if switch == 0:
        text = colour_name(R, G, B) + ' Hex = ' + hex_value(R, G, B)
    else:
        text = colour_name(R, G, B) + ' R=' + str(R) + ' G=' + str(G) + ' B=' + str(B)
    # Put texts on the image
    cv2.putText(img, text, (28, 20), font, 0.7, (255, 255, 255), 1,  cv2.LINE_AA)
    if (R+G+B >= 550):
        cv2.putText(img, text, (28, 20), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    # Display image img in windows "image
    cv2.imshow("image", img)

cv2.destroyAllWindows()
