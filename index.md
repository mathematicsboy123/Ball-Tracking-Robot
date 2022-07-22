# Ball Tracking Robot
  This robot uses OpenCV and picamera to track a ball and then the robot will travel to the ball. It also is capable of detecting human gestures and moving in the appropriate ways. 

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Shreyans D | Stamford Highschool | Computer Science & Mechanical Engineering | Incoming Sophmore

![Headstone Image](https://raw.githubusercontent.com/BlueStampEng/BSE_Template_Portfolio/de8633f62b5da2234992a0178a6a72fd6df7e7e1/branding/BlueStamp-Logo.svg)
[Documentation](./Documentation.pdf)
 
# First Milestone

  My first milestone was to get my Raspberry Pi setup properly with all of the packages and libraries and complete a basic contour detection program. First we tried to set up the Raspberry Pi on the 64 bit OS. We tried to set up the camera with the Raspberry Pi but it didn’t work because there was new camera software installed. When we disabled the libcamera, the VNC would not work. Hence we re-setup the raspberry pi with the 32-bit os and this worked. Then we tried to reinstall opencv but it would not work. Hence we installed a new camera module named picamera to get the output from the camera since the Open-CV video capture does not work. After doing all of this we were able to get the camera output working. We then moved onto working on the software. First we tried to detect all of the contours, or blobs of color, in the image. This attempt failed because we were unable to filter out our ball from the image. 

<iframe width="650" height="365.625" src="https://www.youtube.com/embed/g0bbrq72xtk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Second Milestone

  For my second milestone we wanted to be able to filter out a ball from the image. This time we just used a different way to create the binary image which would allow for more accurate contour detection. We first applied a Gaussian blur which would improve the average color of a block in the image. Then we would create a different cutoff value for each 601-601 box which would allow for more accurate binary image generation. This is called Adaptive Binary image generation. However, this failed because we just weren’t able to filter out the ball reliably enough. For the third and final iteration of the software, we decided to use image masking to create the binary image. To do this, we first changed the camera configuration from stream_configuration to still_configuration. This allowed us to easily convert the image to HSV. We then filtered out the color of the ball through image masking. We then generated a binary image and counted the number of white pixels to detect if the ball was actually in the image and then we took the average location of all the white pixels to compute the center of the ball. We also finished the hardware assembly of the project and wired everything up. We also set up the circuit for the bluetooth module, Arduino, and the accelerometer. The accelerometer would detect tilt, the Arduino would process it, and the bluetooth module would send it to the Raspberry Pi. However we still need to connect the bluetooth module to the Raspberry Pi. 

<iframe width="650" height="365.625" src="https://www.youtube.com/embed/CSiML7SuItQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Third Milestone

  For my third and final milestone we finished my project. We started off by connecting the H-bridge to the Raspberry Pi’s GPIO pins and the motors. We then wrote software that the robot could use to move towards the ball. The software included different functions that could be used to move in different directions and the software would come up with a sequence of movements that would move it closer to the ball. Once we had the ball detection robot working, we moved onto connecting the bluetooth module to the Raspberry Pi. Once we paired the two devices together, we wrote software that would allow the accelerometer to detect tilt and for the Arduino to process it and tell the bluetooth module to send a unique command to the Raspberry Pi. Upon receiving the command the Raspberry Pi would make the robot move in the appropriate direction. Plus, we made it so that if the accelerometer were to be flat, then the robot would automatically go into ball detection mode. 

<iframe width="650" height="365.625" src="https://www.youtube.com/embed/OHF286y9-uI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
