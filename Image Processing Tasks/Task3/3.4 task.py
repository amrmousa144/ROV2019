import numpy as np
import cv2
from PIL import ImageGrab
import math
############################################################intial values 
rect = (0,0,0,0)
dimsofref= [0,0,0,0,0,0,0,0,0,0]
startPoint = False
endPoint = False
click=3
flag_million,flag=6,0
true_lenght1=0

a = [0.840,1.050,1.315,1.660,1.900,2.375,2.875,3.500,4.00,4.5,5.563,6.625,8.625,10.750,12.750]#10 dim sch 40
##########################################function let us take the mouse X and Y when click
def on_mouse(event,x,y,flags,params):
    global rect,startPoint,endPoint,click
    ############# get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        click=0
        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            rect = (0, 0, 0, 0)
        if startPoint == False:
            rect = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True
    if event == cv2.EVENT_RBUTTONDOWN:
        click=1
        if startPoint == True and endPoint == True:
            startPoint= False
            endPoint = False
            rect = (0, 0, 0, 0)
        if startPoint == False:
            rect = (x,y, 0, 0)
            startPoint = True
        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True                    
            endPoint = True                  
################################################################################
#######################every thing happen here
while(True):
    flag_million=3
    #################################make fram and make it fixed
    winname="frame"
    cv2.namedWindow(winname)
    cv2.moveWindow(winname,700,0)
    if flag!= 1:
    ########################################take the frame from scren with w,h
        img = ImageGrab.grab(bbox=(0, 0, 666, 768)) #x, y, w, h
    ########################################turn it to numby array (color are  not reall)
        img_np = np.array(img)
    ################################turn the numby array to reall color (fatema idea 3a4 :V)
        RGB=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    ##################################wait time
    waitTime = 8
    cv2.setMouseCallback(winname, on_mouse)    
        #drawing circle
    if click==0:
        if startPoint == True :
            cv2.circle(RGB,(rect[0],rect[1]), 2, (0,255,0), -1)
        if endPoint == True:
            cv2.circle(RGB,(rect[2],rect[3]), 2, (0,255,0), -1)
            cv2.line(RGB,(rect[0],rect[1]),(rect[2],rect[3]),(255,0,0),2)
    if click==1:
            if startPoint == True :
                cv2.circle(RGB,(rect[0],rect[1]), 2, (0,0,255), -1)
            if endPoint == True:
                cv2.circle(RGB,(rect[2],rect[3]), 2, (0,0,255), -1)
                cv2.line(RGB,(rect[0],rect[1]),(rect[2],rect[3]),(0,0,255),2)

        ##################################################################################
        #********************************************************************************#
        ##################################################################################
    k= cv2.waitKey(1)
    if k == 27: ## if preese esc 
        break
        ##################################################################################
        #***********************************Taking screenshot(k=s) ************************#
    elif k == ord('s'):
        flag=1
        ##################################################################################
        #***********************************return to multi frames(k=b)  *********************************#
    elif k == ord('b'):
         flag=0
########################################################################################################################
################################The lenght of ref (x , y , z)##########################################
########################################################################################################################                  
    elif k == ord('n'):
         Truelenghtof_reff = input("Enter the true lenght of reff: ")
         print("determine the reff object in photo and press (a) small ")
########################################################################################################################
################################Calculate the num of pixdr between two point and get the pixel lenght###################
########################################################################################################################         
    elif k == ord('a'):##if press a        
        dimsofref[0] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
        print ("you determine a reff =",dimsofref[0] , "pixel")
        print ("determine the lenght u want to measure in your reff plan and press (b)")
        pix_brick =float( Truelenghtof_reff) / dimsofref[0] 
########################################################################################################################
########################################################################################################################
########################################################################################################################
    elif k == ord('o'):
        dimsofref[4] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
        diameter = ( pix_brick *  dimsofref[4] ) 
        print("the lenght u measuered =",diameter,"CM")
        for i in range(len(a)) :
            if diameter > a[i]*2.54 and diameter < a[i+1]*2.54 :
                print ("the true diametar =",a[i+1]*2.54, "CM")
               # print ("D1 = ""{:.1f}".format(((a[i+1]*2.54)))

                print ("the true radius  =",(a[i+1]*2.54) /2, "CM")
                #print ("R1 = ""{:.1f}".format(((a[i+1]*2.54) /2)))


                true_diameter= a[i+1]*2.54           ### true_diameter from list 
                pixel_diameter = true_diameter / dimsofref[4] ### pixel of the diameter
                Truelenghtof_reff = true_diameter
                break
#######################################################################################################################
########################################################################################################################
########################################################################################################################
    elif k == ord('i'):
        
        dimsofref[5] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
##        diameter = ( pix_brick *  dimsofref[5] ) 
##        print("the lenght u measuered =",diameter,"CM")
        outter = true_diameter+ 0.8
        #print ("D1 =",outter, "CM")
        print ("D1 = ""{:.1f}".format(((outter))))
        #print ("r1 =",outter/2, "CM")
        print ("r1 = ""{:.1f}".format(((outter/2))))


             
#######################################################################################################################
########################################################################################################################
########################################################################################################################
    elif k == ord('h'):
        dimsofref[6] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
        inner = (outter /dimsofref[7]) *dimsofref[6]
        #print ("D2 =",inner, "CM")
        print ("D2 = ""{:.1f}".format(((inner))))

        print ("r2 =",inner /2, "CM")

        print ("r2 = ""{:.1f}".format(((inner/2))))
#######################################################################################################################
########################################################################################################################
########################################################################################################################
    elif k == ord('j'):
        dimsofref[7] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )


             
#######################################################################################################################
########################################################################################################################
########################################################################################################################           
    elif k == ord('c'):
        ##if press a
            dimsofref[2] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
            true_lenght2 =( pixel_diameter * dimsofref[2] )
            #print ("d3 =",true_lenght2 + 0.8 ,"CM")
            print ("D3 = ""{:.1f}".format(((true_lenght2 + 0.8))))
               
            #print ("r3 =",(true_lenght2 + 0.8)/2 ,"CM")
            print ("R3 = ""{:.1f}".format(((true_lenght2 + 0.8)/2)))



    elif k == ord('d'):##if press a
                dimsofref[3] = math.sqrt( ((rect[0]-rect[2])**2)+((rect[1]-rect[3])**2) )
                lenght = ( float(Truelenghtof_reff) *  dimsofref[3] ) /  dimsofref[0]
                print (lenght)
        


########################################################################################################################
########################################################################################################################
########################################################################################################################
    cv2.imshow(winname,RGB)
########################################################################################################################
########################################################################################################################
########################################################################################################################


cv2.destroyAllWindows()

######################################################################################################################
########################################################################################################################3
