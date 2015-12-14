import cv2
import numpy as np

#Start of Maze Solving
#Initiates webcam
cap = cv2.VideoCapture(0)

#Sets camera_capture to image attained from webcam and saves it as Maze1.png
def get_image():
        retval, im = cap.read()
        return im
camera_capture = get_image()
cap.release()
cv2.imwrite("Maze1.png", camera_capture)

#Auto Crop Filtering
kernel1 = np.ones((5,5), np.uint8)
img = cv2.imread("Maze1.png")
gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur2 = cv2.medianBlur(gray1,15)
th2 = cv2.adaptiveThreshold(blur2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
ret, thresh3 = cv2.threshold(th2,0,255,cv2.THRESH_BINARY_INV)
closing = cv2.morphologyEx(th2,cv2.MORPH_CLOSE,kernel1)
ret, thresh3 = cv2.threshold(closing,0,255,cv2.THRESH_BINARY_INV)
closing1 = cv2.morphologyEx(thresh3,cv2.MORPH_CLOSE,kernel1)

#cv2.imshow('closing1',closing1)
#cv2.waitKey(0)
_,contours1,_ = cv2.findContours(closing1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours1[-1]
x,y,w,h = cv2.boundingRect(cnt)
print x,y,w,h

#Crops the image to the border of the maze
cropped = img[y:y+h-15,x+15:x+w-12]
cv2.imwrite('cropped.png',cropped)

kernel = np.ones((70,70), np.uint8)

#Changes image properties of cropped to a black and white binary image
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,100,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ret, thresh2 = cv2.threshold(thresh,0,100,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#cv2.imshow('gray',thresh2)
#cv2.waitKey(0)
#Finds contours of the maze
_,contours,_ = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#Sets values to the cropped image pixels
path = np.zeros(cropped.shape, np.uint8)
path2 = np.zeros(cropped.shape, np.uint8)

#Draws the wall contours to path and path2
cv2.drawContours(path, contours, 1,(255,255,255), 1)
cv2.drawContours(path2, contours, 0,(255,255,255), 60)

#Dilates the walls and subtracts them to yield single path through the maze
dlate = cv2.dilate(path, kernel, iterations =1)
dlate2 = cv2.dilate(path2, kernel, iterations =1)
solution = cv2.absdiff(dlate,dlate2)

cv2.imwrite("Solution3.png", solution)

#Start separate image into grid of nine blocks
image = cv2.imread("Solution3.png")
Row1 = image.shape[0]/3
Col1 = image.shape[1]/3
Row2 = Row1*2
Row3 = Row1*3
Col2 = Col1*2
Col3 = Col1*3

#Looks for black pixels in each block
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
k=0
pixs = []
for i in range(Row1):
        for j in range(Col1):
                x1 = image[i,j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,255,0]
                        a+=1
for i in range(Row1, Row2):
        for j in range(Col1):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        b+=1
for i in range(Row2, Row3):
        for j in range(Col1):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        c+=1
for i in range(Row2, Row3):
        for j in range(Col1, Col2):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        d+=1
for i in range(Row1, Row2):
        for j in range(Col1, Col2):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,255,0]
                        e+=1
for i in range(Row1):
        for j in range(Col1, Col2):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        f+=1
for i in range(Row1):
        for j in range(Col2, Col3):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        g+=1
for i in range(Row1, Row2):
        for j in range(Col2, Col3):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        h+=1
for i in range(Row2, Row3):
        for j in range(Col2, Col3):
                x1 = image[i, j]
                if (x1[0] == 0)&(x1[1] == 0)&(x1[2] == 0):
                        #image[i,j] = [0,0,255]
                        k+=1
pixs.append(a)
pixs.append(b)
pixs.append(c)
pixs.append(d)
pixs.append(e)
pixs.append(f)
pixs.append(g)
pixs.append(h)
pixs.append(k)
#Compares each block for percentage of black pixels
#Connects each block with connected black pixels "path"
#Sents commands to get to each block for the robot to array commands
Position = []
Commands = []
for i in range(9):
        if i == 0:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        spot = 'One'
                        Position.append(spot)
        elif i == 1:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row1-1, Row1):
                                for j in range(Col1):
                                        x2 = image[i, j]
                                        for n in range(Row1,Row1+1):
                                                for m in range(Col1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[0]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Two'
                                                                        toGetHere = 'Right'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Position.append(spot)
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
        elif i == 2:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row2-1, Row2):
                                for j in range(Col1):
                                        x2 = image[i, j]
                                        for n in range(Row2,Row2+1):
                                                for m in range(Col1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[1]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Three'
                                                                        toGetHere = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Position.append(spot)
        elif i == 3:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row2, Row3):
                                for j in range(Col1-1, Col1):
                                        x2 = image[i, j]
                                        for n in range(Row2, Row3):
                                                for m in range(Col1, Col1+1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[2]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Four'
                                                                        toGetHere = 'Left'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
                        Position.append(spot)
        elif i == 4:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row1, Row2):
                                for j in range(Col1-1,Col1):
                                        x2 = image[i, j]
                                        for n in range(Row1, Row2):
                                                for m in range(Col1, Col1+1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[1]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Five'
                                                                        toGetHere = 'Left'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        for i in range(Row2-1, Row2):
                                for j in range(Col1,Col2):
                                        x2 = image[i, j]
                                        for n in range(Row2, Row2+1):
                                                for m in range(Col1, Col2):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[3]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Five'
                                                                        toGetHere = 'Left'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
                        Position.append(spot)
        elif i == 5:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row1-1, Row1):
                                for j in range(Col1,Col2):
                                        x2 = image[i, j]
                                        for n in range(Row1, Row1+1):
                                                for m in range(Col1, Col2):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[4]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Six'
                                                                        toGetHere = 'Left'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        for i in range(Row1):
                                for j in range(Col1-1,Col1):
                                        x2 = image[i, j]
                                        for n in range(Row1):
                                                for m in range(Col1,Col1+1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[0]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Two'
                                                                        toGetHere = 'Right'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
                        Position.append(spot)
        elif i == 6:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row1):
                                for j in range(Col2-1,Col2):
                                        x2 = image[i, j]
                                        for n in range(Row1):
                                                for m in range(Col2, Col2+1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[5]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Seven'
                                                                        toGetHere = 'Right'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
                        Position.append(spot)
        elif i == 7:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row1-1,Row1):
                                for j in range(Col2,Col3):
                                        x2 = image[i, j]
                                        for n in range(Row1, Row1+1):
                                                for m in range(Col2, Col3):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[6]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Eight'
                                                                        toGetHere = 'Right'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        for i in range(Row2):
                                for j in range(Col2-1,Col2):
                                        x2 = image[i, j]
                                        for n in range(Row2):
                                                for m in range(Col2, Col2+1):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[4]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Eight'
                                                                        toGetHere = 'Right'
                                                                        toGetHere1 = 'Forward'
                                                                        break
                        Commands.append(toGetHere)
                        Commands.append(toGetHere1)
                        Position.append(spot)
        elif i == 8:
                if((pixs[i]/float(Row1*Col1))*100) > 10:
                        for i in range(Row2-1,Row2):
                                for j in range(Col2,Col3):
                                        x2 = image[i, j]
                                        for n in range(Row2, Row2+1):
                                                for m in range(Col2, Col3):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[7]/float(Row1*Col1))*100) > 10:
                                                                        spot = 'Nine'
                                                                        toGetHere = 'Forward'
                                                                        Exit = 'Left'
                                                                        break
                        for i in range(Row2-1,Row2):
                                for j in range(Col2,Col3):
                                        x2 = image[i, j]
                                        for n in range(Row2, Row2+1):
                                                for m in range(Col2, Col3):
                                                        x3 = image[n, m]
                                                        if ((x2[0]==0)&(x3[0]==0)):
                                                                if((pixs[7]/float(Row1*Col1))*100) > 10:
                                                                        if(Commands[8] is 'Forward'):
                                                                                spot = 'Nine!'
                                                                                toGetHere = 'Right'
                                                                                toGetHere1 = 'Forward'                                                                                
                                                                                Exit = 'Left'
                                                                        break
                        Commands.append(toGetHere)
                        Position.append(spot)
                        if(Position[6] is 'Nine!'):
                                Commands.append(toGetHere1)
                        Commands.append(Exit)
print Position
#Saves commands for robot to text file
f = open("commands.txt","w")
for m in range(0, 6):
        if m==0:
                f.write(Commands[0])
                f.write('\n')
                f.write(Commands[1])
                f.write('\n')
        if m==1:
                f.write(Commands[2])
                f.write('\n')
                f.write(Commands[3])
                f.write('\n')
        if m==2:
                f.write(Commands[4])
                f.write('\n')
                f.write(Commands[5])
                f.write('\n')
        if m==3:
                f.write(Commands[6])
                f.write('\n')
                f.write(Commands[7])
                f.write('\n')
        if m==4:
                f.write(Commands[8])
                f.write('\n')
                f.write(Commands[9])
                f.write('\n')
        if m==5:
                f.write(Commands[10])
                f.write('\n')
                f.write(Commands[11])
                f.write('\n')
                f.close()



