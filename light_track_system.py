import time
import cv2
import numpy as np
import math
import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def process_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    ret, thresh = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    corona_distance = 5
    #print(contours[1][0][0][1])
    i = 0
    points = []
    for contour in contours:
        # finding the centers of the contours
        #print(str(i) + " contor")
        i += 1
        x_sum = 0
        y_sum = 0
        for point_value in range(0,len(contour)): 
            point = contour[point_value][0]

            x_sum += point[0]
            y_sum += point[1]
        x_center = x_sum/len(contour)
        y_center = y_sum/len(contour)
        points.append((x_center,y_center))
        i = 0
    corona_values = []
    height,width, _ = image.shape
    for contour in contours:
        #finding the corona of the lights
        corona_values.append([])
        #print(str(i) + " contor")
    
        x_center = points[i][0]
        
        y_center = points[i][1]
        
        for point_value in range(0,len(contour)): 
            point = contour[point_value][0]


            x_point = point[0]
            y_point = point[1]
            x_d = x_point - x_center
            y_d = y_point - y_center
            h = math.sqrt(math.pow(y_d,2) + math.pow(x_d,2))
            x_new = corona_distance*(x_d/h) + x_point
            y_new = corona_distance*(y_d/h) + y_point
            if 0 < x_new < width and 0 < y_new < height: 
                corona_val = (x_new,y_new)
                corona_values[i].append(corona_val)
        i += 1 



    

    # Draw contours around lights

    cv2.drawContours(image, contours, -1, (250, 140, 0), 2)
    color = (0,0,255)
    color2 = (252,3,252)

    #print(corona_values)
    r_vals = []
    g_vals = []
    b_vals = []
    i = 0
    color_array = []
    color_decision_array = []
    for corona_set in corona_values:
        color_pick = [0,0,0,0,0]
        # blue,yellow,green,red
        for point in corona_set:
            x = int(point[0])
            y = int(point[1])
            
            pixel_rgb = image[y,x]
            b = pixel_rgb[0]
            g = pixel_rgb[1]
            r = pixel_rgb[2]
            b_vals.append(b)
            g_vals.append(g)
            r_vals.append(r)
            #if pixel_rgb[0] == 252 and pixel_rgb[1] == 3 and pixel_rgb[2] == 252:
               # print(str(x) + " " + str(y))
            #set_array.append()
            #cv2.circle(image, (x,y), 1, color2, -1)
            
            if i == 4 or i == 5:
                color_array.append(0)
            elif i == 7 or i == 6:
                color_array.append(1)
            elif i == 0 or i == 3:
                color_array.append(2)
            elif i == 1 or i == 2:
                color_array.append(3)
            sample_color_dec = choose_color(r,g,b)
            if(sample_color_dec == -1):
                color_pick[0] += 1
            else:
                color_pick[sample_color_dec + 1] += 1
            
        c_arr = np.array(color_pick)
        color_decision = np.argmax(c_arr)
        if color_decision == 1:
            color_char = 'b'
        elif color_decision == 2:
            color_char = 'y'
        elif color_decision == 3:
            color_char = 'g'
        elif color_decision == 4:
            color_char = 'r'
        else:
            color_char = 'u'
        color_decision_array.append(color_char)
        i += 1
    end = time.time()
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # White color in RGB
    thickness = 2

    # Display the image with identified lights
    i = 0
    for point in points:
        cv2.circle(image, (int(point[0]),int(point[1])), 1, color, -1)
        cv2.putText(image, color_decision_array[i], (int(point[0]),int(point[1])), font, font_scale, font_color, thickness) 
        i += 1
    return image
def choose_color(r,g,b):
    """takes in a list of rgb values, and determines what color the light is. """
    if b > 200 and g < 75 and r < 75:
        # blue
        return 0
    elif r > 75 and r < 225 and g > 50 and g < 175:
        # yellow
        return 1
    elif r < 75 and g > 100:
        # green
        return 2
    elif r > 200 and g < 100:
        # red
        return 3
    return -1


# Read the image
start = time.time()


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image = process_image(frame)
   
    cv2.imshow('esd', frame)
    if cv2.waitKey(1) == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()


