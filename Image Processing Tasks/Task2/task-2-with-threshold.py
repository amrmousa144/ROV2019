import numpy as np
import cv2
from PIL import ImageGrab
import math
import time

###################name the windows for the track bar
sqr,line,tri,cir = 0,0,0,0
cv2.namedWindow("RGB")
img = np.zeros((300,512,3), np.uint8)
###################to creat the track bar in thr while loop
################### save the prevoius data ...
app = 0
prev_app = 1
###################change the dimn of the ROI
d_h,d_w,i_h,i_w,x_k=0,0,0,0,0
def nothing(x):
  pass
###################creat the trackbar in RGB 
cv2.createTrackbar("upper", "RGB",0,250,nothing)
cv2.createTrackbar("lower", "RGB",0,250,nothing)
##########################################################################
while(True):
#####################creat the track bar once
    if app != prev_app :
        ##()
        prev_app = app
    ###############get the value of the trackbar    
    upper_thr=cv2.getTrackbarPos("upper", "RGB")
    lower_thr=cv2.getTrackbarPos("lower", "RGB")
    
    print (upper_thr,lower_thr)
    ################ take the frame by frame 
    img = ImageGrab.grab(bbox=(0, 0, 666, 768)) #x, y, w, h
    img_np = np.array(img)
    RGB=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    #################convert it to gray and threshold
##    gray = cv2.cvtColor(RGB ,cv2.COLOR_BGR2GRAY)
##    ret,thresh = cv2.threshold(gray,85,170,cv2.THRESH_BINARY)
    #################draw rect for the Roi 
    ##cv2.rectangle(RGB,(0,150),(700,700),(0,0,225),1)
    ##################move the ROI (ASCI)
    key = cv2.waitKey(1)

    if key == 52: 
       d_w=d_w-10
       
    if key == 54:
      d_w=d_w+10
      
    if key == 50:
      d_h=d_h+10
       
    if key == 56:
       d_h=d_h-10
       
    if key == 43:
       x_k=x_k+20

    if key == 45:
       x_k=x_k-20

    ###################draw rect in the RGB to determine the ROI

    cv2.rectangle(RGB,(d_w,d_h),(d_w+100+x_k,d_h+100+x_k),(255,0,10),1)
    ##################determine the ROI regoin
    ROI = RGB[d_h:d_h+100+x_k,d_w:d_w+100+x_k]
    Roi_gray = cv2.cvtColor(ROI ,cv2.COLOR_BGR2GRAY)
    Roi_ret,Roi_thresh = cv2.threshold(Roi_gray,lower_thr,upper_thr,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(Roi_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    if key ==ord("u") :           
        if  contours  :                            
            cnt = contours[0]
            font = cv2.FONT_HERSHEY_SIMPLEX
            count = 1
            #######################approxmate the point of the countoues########
            for cnt in contours:

                approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
                x=approx.ravel()[0]
                y=approx.ravel()[1]
                print (len(approx))
                (x,y,w,h)=cv2.boundingRect(approx)
                if h*w>255:
                    if len(approx)>6:
                        print ("circle")
                        cv2.drawContours(ROI,[cnt],-1,(0,0,255),2)
                        cv2.putText(ROI,"circle",(x,y), font, 1,(0))
                        key = cv2.waitKey(1)
                        #if key == ord("f"):
                        print (x,y,w,h,"000000000000000000000000000000")
                            #if h*w>255:
                            
                            #ar=w/float(h)
                        cir = cir+1
                                
                    if len(approx)==3:
                        cv2.drawContours(ROI,[cnt],-1,(0,0,255),3)
                        cv2.putText(ROI,"triangle",(x,y), font, 1,(0))
                    
                        tri =  tri+1
                        
                    if len(approx)==4:
                        (x,y,w,h)=cv2.boundingRect(approx)
                       # print (x,y,w,h,"000000000000000000000000000000")
                        #if h*w>225:
                        print (x,y,w,h)
                        ar=w/float(h)
                        if h>w*2 or w>h*2:
                            print ("line")
                            cv2.putText(ROI,"line",(x,y),font, 1,(255))
                            line = line+1
                            cv2.drawContours(ROI,[cnt],-1,(0,0,255),1)
                        else:
                            print (x,y,w,h,"000000000000000000000000000000")
                                # "square"
                            cv2.putText(ROI,"square",(x,y),font, 1,(255))
                            cv2.drawContours(ROI,[cnt],-1,(0,0,255),1)

                            sqr = sqr+1

                #############################determine the position of outputWindow ^_^####
                #********** drawing_square ###### num of sqr**********
                print ("square= ",sqr-1)
                print ("line= ",line)
                print ("circle= ",cir)
                print ("triangle= ",tri)
                third = np.zeros((250,200,3), np.uint8)
                
                cv2.rectangle(third,(126,170),(167,209),(0,0,225),-1)
                cv2.putText(third,str(sqr-1),(40,190), font, 1,(0,0,225),0)
                
                #********** drawing_line ###### num of lines**********
                cv2.line(third,(125,143), (168,143), (0,0,225), 4)
                cv2.putText(third,str(line),(40,143), font, 1,(0,0,225),1)
                #**********drawing_circle ######num of circles**********
                cv2.circle(third,(150,50), 20, (0,0,255), -1)
                cv2.putText(third,str(cir),(40,50), font, 1,(0,0,225),1)
                #**********drawing_triangle ###### num of triangles********
                cv2.line(third,(161,111), (123,111), (0,0,225), 4)
                cv2.line(third,(161,111), (143,78), (0,0,225), 4)
                cv2.line(third,(123,111), (143,78), (0,0,225), 4)
                cv2.putText(third,str(tri),(40,95), font, 1,(0,0,225),1)
                file=open("#shapes.txt","a")
                file.write(str(cir))
                file.write(str(tri))
                file.write(str(line))
                file.close()
                cv2.namedWindow("ROI")
                cv2.moveWindow("ROI",300,200)
                cv2.namedWindow("num")
                cv2.moveWindow("num",100,600)
                cv2.imshow("num",third)
                cv2.imshow("ROI",ROI)


    ########################## if we find coutour
    cv2.imshow("RGB",RGB)
    cv2.imshow("Gray ROI",Roi_gray)
    cv2.imshow("Thresh ROI",Roi_thresh)


    if key == 27:
      cv2. destroyAllWindows()
