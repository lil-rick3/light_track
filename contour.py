import math
import numpy as np
class Contour:
    def __init__(self, contour_info,img):
        """
        contour info is the array of contours, w is image width, and h is image height
        
        """
        self.is_legit = True
        self.image = img
        self.raw_contour = contour_info
        self.color_decision = [0,0,0,0,0]
        # blue,yellow,green,red, unidentified
        self.height = None
        self.width = None
        self.height, self.width, _= self.image.shape
        
        self.x_center = None
        self.y_center = None
        self.loc = None
        self.color = None
        self.numContours = None
        self.contourPoints = []
        
        self.setContours(contour_info)
        self.corona_values = []
        self.findCenter()
        self.findCorona()
        self.find_color()

        if self.numContours < 10:
            self.is_legit = False
        if self.color == 'u':
            self.is_legit = False
    
    def setContours(self, contour_info):
        for point_value in range(0,len(contour_info)): 
            point = contour_info[point_value][0]

            x = point[0]
            y = point[1]
            self.contourPoints.append((x,y))
        self.numContours = len(self.contourPoints)
    def findCenter(self):
        x_sum = 0
        y_sum = 0
       
        for point in self.contourPoints: 
            
            

            x_sum += point[0]
            y_sum += point[1]
        self.x_center = x_sum/len(self.contourPoints)
        self.y_center = y_sum/len(self.contourPoints)
        self.loc = (int(self.x_center),int(self.y_center))
        
    def findCorona(self):
        corona_distance = 5
        for point in self.contourPoints: 


            x_point = point[0]
            y_point = point[1]
            x_d = x_point - self.x_center
            y_d = y_point - self.y_center
            h = math.sqrt(math.pow(y_d,2) + math.pow(x_d,2))
            x_new = corona_distance*(x_d/h) + x_point
            y_new = corona_distance*(y_d/h) + y_point
            if 0 < x_new < self.width and 0 < y_new < self.height: 
                corona_val = (x_new,y_new)
                self.corona_values.append(corona_val)
    def find_color(self):
        
        
        
        for point in self.corona_values:
            x = int(point[0])
            y = int(point[1])
            
            pixel_rgb = self.image[y,x]
            b = pixel_rgb[0]
            g = pixel_rgb[1]
            r = pixel_rgb[2]
            color_val = self.choose_color(r,g,b)
            if color_val == -1:
                self.color_decision[4] += 1
            else:
                self.color_decision[color_val] += 1
        c_arr = np.array(self.color_decision)
        contour_color = np.argmax(c_arr)
        if contour_color == 1:
            self.color = 'b'
        elif contour_color == 2:
            self.color = 'y'
        elif contour_color == 3:
            self.color = 'g'
        elif contour_color == 4:
            self.color = 'r'
        else:
            self.color = 'u'
        


    def choose_color(self,r,g,b):
        """takes in a list of rgb values, and determines what color the light is. """
        if b > 200 and g < 75 and r < 75:
            # blue
            return 0
        elif r > 75 and r < 225 and g > 50 and g < 175 and b < 100:
            # yellow
            return 1
        elif r < 75 and g > 100:
            # green
            return 2
        elif r > 200 and g < 100:
            # red
            return 3
        return -1
            
