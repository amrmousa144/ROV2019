import numpy as np
import cv2
from PIL import ImageGrab
import math
import time



while(True):
    ##############take screen and turn it to numpy array > > color is not real
    img = ImageGrab.grab(bbox=(0, 0, 666, 768)) #x, y, w, h
    img_np = np.array(img)
    #################################convert the numpy array img to real color
    RGB=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    ##########################################################################
    ###################your code here#######################################


    ##img = cv2.imread('shapes3.png')
    hsv = cv2.cvtColor(RGB, cv2.COLOR_BGR2HSV)

    lower_rangeblue = np.array([110, 50, 50], dtype=np.uint8)
    upper_rangeblue =  np.array([130, 255, 255], dtype=np.uint8)
    mask_blue = cv2.inRange(hsv, lower_rangeblue, upper_rangeblue)
     
    #######################convert image to gray  + threshold #########
    ##gray = cv2.cvtColor(RGB,cv2.COLOR_BGR2GRAY)
    ##ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ########################find countores#############################


    contours, _ = cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    if  contours  :
        

        cnt = contours[0]
        font = cv2.FONT_HERSHEY_SIMPLEX
        count = 1
        #######################approxmate the point of the countoues########
        for cnt in contours:
                
            approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            x=approx.ravel()[0]
            y=approx.ravel()[1]

        ########################################################################
            if len(approx)==4:
                (x, y, w, h) = cv2.boundingRect(approx)
                rect = cv2.minAreaRect(approx)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                ((x1,y1),(w1,h1),seta) = cv2.minAreaRect(approx)
                h_semi =float( "{:.1f}".format(((h1))))
                w_semi = float("{:.1f}".format(((w1))))


                if ((w_semi * h_semi) > 100 ) :###if area big = m00 > 0
                    M = cv2.moments(cnt)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.circle(RGB, (cX, cY), 7, (255, 255, 255), -1)
                    if w_semi > h_semi :
                        pixel = 2.3 / h_semi
                        true_lengh =  float( "{:.1f}".format(((pixel * w_semi)))) 
                        print("hight =",true_lengh ,"cm")
                        ##cv2.putText(RGB,str(h_semi) ,(int(x-50),int(y+20)),font, 1,(0,0,255))
                        ##cv2.putText(RGB,str(w_semi) ,(int(x+70),int(y+80)),font, 1,(0,0,255))
                        cv2.putText(RGB,str(true_lengh ) ,(int(x-100),int(y+100)),font, 1,(100,255,100))

                        cv2.drawContours(RGB,[box],0,(0,255,0),2)

                    elif h_semi > w_semi :
                        pixel = 1.85 / w_semi
                        true_lengh =  float( "{:.1f}".format(((pixel * h_semi)))) 
                        print ("hight =",true_lengh , "cm")
                        ##cv2.putText(RGB,str(h_semi) ,(int(x+50),int(y+100)),font, 1,(0,0,255))
                        ##cv2.putText(RGB,str(w_semi) ,(int(x),int(y-10)),font, 1,(0,0,255))
                        cv2.putText(RGB,str(true_lengh ) ,(int(x-100),int(y+100)),font, 1,(100,255,100))
                        cv2.drawContours(RGB,[box],0,(0,255,0),2)

                else :
                    continue 
        



        
    #############################determine the position of outputWindow ^_^####
    cv2.namedWindow("frame")
    cv2.moveWindow("frame",700,0)
    cv2.imshow("frame",RGB)
    ###cv2.imshow('mask',mask_blue) ### only blue
    
    ################################break the loop and end the code
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2. destroyAllWindows()
