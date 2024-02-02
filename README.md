Hello, this is the readme file for my implementation of light tracking, to run it, you use the camera_run.py script.  
Here the light tracking algorithm processes images and then outputs a marked up image, and a lightArr
```image,lightArr = Light_Tracking.process_image(frame)```  
This is the light arr and has the format of  
```[((543.5, 9.5), 3), ((249.0, 319.5), 0)]```  
This is an array of tuples. In each tuple, there is a number and another tuple. The tuple is the xy coordinate starting in top left corner.  
The other int value is from 0 to 4, and corresponds to the color, which is goes as 0:r, 1:b, 2:g, y:3  

To run the program, type this into the command line:  
```python camera_run.py --source[camera source, either 0 or 1] --delay[in seconds]```  

