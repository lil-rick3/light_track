import argparse
import cv2
import keyboard
from light_track_system import Light_Tracking
import string
import time


def take_photo(image,img_no):
    cv2.imwrite("captured_photo" + str(img_no) + ".jpg", image)
def run(
        source = 0,
        delay = 0
    ):
    print(source)
    cap = cv2.VideoCapture(source)
    i = 0
    while True:
        start = time.time()
        ret, frame = cap.read()
        
        """if keyboard.is_pressed('t'):
            take_photo(frame,i)
            i += 1
            # Add a delay to prevent multiple captures for a single key press
            time.sleep(2)
        elif cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the program
            break"""
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the program
            break
        else:
            image,lightArr = Light_Tracking.process_image(frame)
            cv2.imshow('esd', image)
            #print(lightArr)
            while(time.time() - start < delay):
                continue

    cap.release()
    cv2.destroyAllWindows()

def parse_opt():
    parser = argparse.ArgumentParser()
   
   
    parser.add_argument('--source', type=int, default=0)
    parser.add_argument('--delay', type=float, default=0)
    opt = parser.parse_args()
    #opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    
    return opt

def main(opt):
    
    run(**vars(opt))


if __name__ == '__main__':
    opt = parse_opt()
    main(opt)