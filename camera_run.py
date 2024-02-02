import cv2
import keyboard
from light_track_system import Light_Tracking
import string
import time
def take_photo(image,img_no):
    cv2.imwrite("captured_photo" + str(img_no) + ".jpg", image)

cap = cv2.VideoCapture(0)
i = 0
while True:
    
    ret, frame = cap.read()
    
    if keyboard.is_pressed('t'):
        take_photo(frame,i)
        i += 1
        # Add a delay to prevent multiple captures for a single key press
        time.sleep(2)
    elif cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the program
        break
    else:
        image = Light_Tracking.process_image(frame)
        cv2.imshow('esd', image)
cap.release()
cv2.destroyAllWindows()