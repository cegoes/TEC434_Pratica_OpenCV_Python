# Written by Kyle Hounslow, December 2013
# Ported to Python by Cláudio Eduardo Góes, October 2022
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software")
# , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import cv2 as cv
from pathlib import Path
import numpy as np

# our sensitivity value to be used in the absdiff() function
SENSITIVITY_VALUE = 20
# size of blur used to smooth the intensity image output from absdiff() function
BLUR_SIZE = 10

def searchForMovement(thresholdImage:np.ndarray, cameraFeed:np.ndarray):
    # we'll have just one object to search for
    # and keep track of its position.
    theObject = (0,0)    
    # bounding rectangle of the object, we will use the center of this as its position.
    objectBoundingRectangle = (0,0,0,0)    
    # notice cameraFeed ins't copy(). This is because we wish to take the values passed
    # into the function and manipulate them, rather than just working with a copy.
    # eg. we draw to the cameraFeed to be displayed in the main() function.
    objectDetected = False
    temp = thresholdImage.copy()
    # these two vectors needed for output of findContours
    # find contours of filtered image using openCV findContours function
    # findContours(temp,contours,hierarchy,CV_RETR_CCOMP,CV_CHAIN_APPROX_SIMPLE ) # retrieves all contours
    contours, hierarchy = cv.findContours(temp, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) # retrieves external contours
    # if contours vector is not empty, we have found some objects
    if len(contours) > 0:
        objectDetected = True
    else:
        objectDetected = False
    if(objectDetected):
        # the largest contour is found at the end of the contours vector
        # we will simply assume that the biggest contour is the object we are looking for.
        largestContourVec = []
        largestContourVec.append(contours[len(contours)-1])
        # make a bounding rectangle around the largest contour then find its centroid
        # this will be the object's final estimated position.
        objectBoundingRectangle = cv.boundingRect(largestContourVec[0])
        xb,yb,wb,hb = objectBoundingRectangle
        # update the objects positions by changing the 'theObject' array values
        theObject = int(xb+wb/2),int(yb+hb/2)
    
    # make some temp x and y variables so we dont have to type out so much
    x,y = theObject
    
    #draw some crosshairs around the object
    cv.circle(cameraFeed,(x,y),20,(0,255,0),2)
    cv.line(cameraFeed,(x,y),(x,y-25),(0,255,0),2)
    cv.line(cameraFeed,(x,y),(x,y+25),(0,255,0),2)
    cv.line(cameraFeed,(x,y),(x-25,y),(0,255,0),2)
    cv.line(cameraFeed,(x,y),(x+25,y),(0,255,0),2)

    # write the position of the object to the screen
    cv.putText(cameraFeed,"Tracking object at (" + str(x)+","+str(y)+")",(x,y),1,1,(255,0,0),2)

def finaliza(mostraVideo):        
    cv.destroyAllWindows()
    mostraVideo.release()

if __name__ == '__main__':
    cv.namedWindow('Difference Image',cv.WINDOW_FREERATIO)
    cv.namedWindow('Threshold Image',cv.WINDOW_FREERATIO)
    cv.namedWindow('Final Threshold Image',cv.WINDOW_FREERATIO)
    caminhoImagem = Path('Anexos, Imagens e Videos/bouncingBall.avi')
    mostraVideo = cv.VideoCapture(str(caminhoImagem))
    # Guarda os frames por segundo do vídeo
    fps = int(1000 / mostraVideo.get(cv.CAP_PROP_FPS))
    frame_counter = 0
    # some boolean variables for added functionality
    objectDetected = False
    # these two can be toggled by pressing 'd' or 't'
    debugMode = True
    trackingEnabled = False
    # pause and resume code
    pausar = False
    # set up the matrices that we will need
    # the two frames we will be comparing
    frame1:np.ndarray;frame2:np.ndarray
    # their grayscale images (needed for absdiff() function)
    grayImage1:np.ndarray;grayImage2:np.ndarray
    #resulting difference image
    differenceImage:np.ndarray
    # thresholded difference image (for use in findContours() function)
    thresholdImage:np.ndarray
    # video capture object.    
    frame = np.ndarray
    while mostraVideo.isOpened():
        frame_counter += 2

        if (frame_counter == (mostraVideo.get(cv.CAP_PROP_FRAME_COUNT)-1)):
            frame_counter = 0
            mostraVideo.set(cv.CAP_PROP_POS_FRAMES, 0) # Set de video frame back to 0
        else:
            #read first frame
            sucess1, frame1 = mostraVideo.read()
            #convert frame1 to gray scale for frame differencing
            grayImage1 = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
            #copy second frame
            sucess2, frame2 = mostraVideo.read()
            #convert frame2 to gray scale for frame differencing
            grayImage2 = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
            #perform frame differencing with the sequential images. This will output an "intensity image"
            #do not confuse this with a threshold image, we will need to perform thresholding afterwards.
            differenceImage=cv.absdiff(grayImage1,grayImage2)
            #threshold intensity image at a given sensitivity value
            _, thresholdImage = cv.threshold(differenceImage,SENSITIVITY_VALUE,255,cv.THRESH_BINARY)
            if(debugMode==True):
                #show the difference image and threshold image
                cv.imshow("Difference Image",differenceImage)
                cv.imshow("Threshold Image", thresholdImage)
            else:
                #if not in debug mode, destroy the windows so we don't see them anymore
                cv.destroyWindow("Difference Image")
                cv.destroyWindow("Threshold Image")
            
            #blur the image to get rid of the noise. This will output an intensity image
            thresholdImage= cv.blur(thresholdImage,(BLUR_SIZE,BLUR_SIZE))
            #threshold again to obtain binary image from blur output
            _, thresholdImage = cv.threshold(thresholdImage,SENSITIVITY_VALUE,255,cv.THRESH_BINARY)
            if(debugMode==True):
                #show the threshold image after it's been "blurred"
                cv.imshow("Final Threshold Image",thresholdImage)
            
            else:
                #if not in debug mode, destroy the windows so we don't see them anymore
                cv.destroyWindow("Final Threshold Image")

            #if tracking enabled, search for contours in our thresholded image
            if(trackingEnabled):
                searchForMovement(thresholdImage,frame1)

            #show our captured frame
            cv.imshow("Output",frame1)
            #check to see if a button has been pressed.
            #this 10ms delay is necessary for proper operation of this program
            #if removed, frames will not have enough time to referesh and a blank 
            #image will appear.
            tecla = cv.waitKey(fps)
            #print(tecla)
            if tecla == 27: #'esc' key has been pressed, exit program.
                finaliza(mostraVideo)
            elif tecla == 116: #'t' has been pressed. this will toggle tracking
                trackingEnabled = not trackingEnabled
                if(trackingEnabled == False):
                    print("Tracking disabled.")
                else:
                    print("Tracking enabled.")
            elif tecla == 100: #'d' has been pressed. this will debug. mode
                debugMode = not debugMode
                if(debugMode == False):
                    print("Debug mode disabled.")
                else:
                    print("Debug mode enabled.")
            elif tecla == 112: #'p' has been pressed. this will pause/resume the code.
                pausar = not pausar
                if(pausar == True):
                    print("Code paused, press 'p' again to resume")
                    while (pausar == True):
                        #stay in this loop until
                        valor = cv.waitKey()
                        if valor==112:
                            #change pause back to false
                            pausar = False
                            print("Code Resumed")