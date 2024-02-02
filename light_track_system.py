import time
import cv2
import numpy as np
import math
import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from contour import Contour
class Light_Tracking:
    def process_image(image):
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        ret, thresh = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #print(contours[1][0][0][1])
        i = 0
        

        
        i = 0
    
        height,width, _ = image.shape
        contour_array = []
        for contour in contours:
            #finding the corona of the lights
            temp_contour = Contour(contour, image)
            contour_array.append(temp_contour)
            



        

        # Draw contours around lights

        
        color = (0,0,255)
        color2 = (252,3,252)

        #print(corona_values)
        
        end = time.time()
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # White color in RGB
        thickness = 2

        # Display the image with identified lights
        i = 0
        lightArr = []
        for itercontour in contour_array:
            if itercontour.is_legit:
                lightArr.append((itercontour.loc,mapcolor_num(itercontour.contour_color)))
                cv2.drawContours(image, [itercontour.raw_contour], -1, (250, 140, 0), 2)
                cv2.circle(image, itercontour.loc, 1, color, -1)
                for corona_point in itercontour.corona_values:
                    
                    cv2.circle(image, corona_point, 1, color2, -1)
                cv2.putText(image, itercontour.color, itercontour.loc, font, font_scale, font_color, thickness) 
                
        return image,lightArr
def mapcolor_num(input):
    if(input == 0):
        return 1
    elif(input == 1):
        return 3
    elif(input == 2):
        return 2
    elif(input == 3):
        return 0
    
# Read the image
#start = time.time()

"""
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image = process_image(frame)
   
    cv2.imshow('esd', frame)
    if cv2.waitKey(1) == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()
"""
"""pre_image = cv2.imread('light_track_test_2.jpg')
process_image = process_image(pre_image)
cv2.imshow('eds',process_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""