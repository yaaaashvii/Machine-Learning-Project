import cv2
import imutils
import pytesseract

# Set the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read the image file
image = cv2.imread('aaa.jpg')


# Resize the image
image = imutils.resize(image, width=500)

# Display the original image
cv2.imshow("Original Image", image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# coverting image to gray scale bcz it will reduce the dimension , complexity and some algos like canny only works on gray img 
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image", gray)
cv2.waitKey(0)

#now reduce nosie 
gray = cv2.bilateralFilter(gray , 11,17,17)
cv2.imshow("smotther image", gray)
cv2.waitKey(0)

# finding edges

edged = cv2.Canny(gray , 170 , 170 )
cv2.imshow("Canny Edge", edged)
cv2.waitKey(0)

#now find contours 
cnts , new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# cnts is contour, curve joining all the contours points
#new is hierachy- relationship 
#RETR_LIST : retrives all the contour but doesnot create any parent child relationship 
#CHAIN_APPROX_SIMPLE : removes all redundant points and compress the contour by saving memory 

#create copy of original image to draw all contours
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0,255,0),3)  #these values are fixed
cv2.imshow("Canny After Contour", image1)
cv2.waitKey(0)

# intrestedin number plate not all contour , cannot locate directly , sort on the basis of areas
#select areas which are maximum so will select top 30 areas
#sorted list will be from min to max , so reverse the order of sorting 

cnts = sorted(cnts , key = cv2.contourArea, reverse= True)[:30]
NumberPlateCount = None

image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0,255,0),3)
cv2.imshow("top 30 Contours", image2)
cv2.waitKey(0) 

#now run a loop on contour to find best possible contour 
count =0
name = 1 
for i in cnts:
    perimeter = cv2.arcLength(i , True)
    #perimeter = arclength , calculated directly 
    approx = cv2.approxPolyDP(i, 0.02*perimeter, True)
    #approxpolydp used to approximate the curve of polygon with precision 
    if(len(approx) == 4): # 4 means 4 corners 
        NumberPlateCount = approx
        #crop rectanlge part
        x, y, w, h = cv2.boundingRect(i)
        crp_image = image[y : y+h , x: x+w]
        cv2.imwrite(str(name) + '.png', crp_image)
        name+=1

        break
#draw contour in image identified as number plate
cv2.drawContours(image,[NumberPlateCount], -1, (0,255,0),3)
cv2.imshow("Final Image", image)
cv2.waitKey(0)

#crop only part of number plate 
crop_img_loc = '1.png'
cv2.imshow("cropped image", cv2.imread(crop_img_loc))

text = pytesseract.image_to_string(crop_img_loc, lang='eng')
print("Number is :", text)
cv2.waitKey(0)
