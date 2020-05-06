import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('woman2.jpg')
row,cols,channels = img.shape
numTotal= row*cols
bound = int((numTotal * 0.15))

output = img.copy()
lista = []
for i in range (row):
    for j in range (cols):        
        lista.append(img[i][j][0])

lista.sort()
smallest= int(lista[bound])
biggest = int(lista[len(lista)-bound])

for i in range (row):
    for j in range (cols):
        if (img[i][j][0] - smallest) < 0 :
            output[i][j] = 0
        elif int(img[i][j][0]- smallest)*(255/int(biggest-smallest)) > 255 :
            output[i][j] = 255
        else:
            output[i][j] =  (img[i][j]-smallest)*(255/(biggest-smallest))
        
cv2.imwrite('img_out_limits.png',output)
cv2.imshow('img',img)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
histr = cv2.calcHist( [img],[0],None,[256],[0,256])
histr2 = cv2.calcHist( [output],[0],None,[256],[0,256])
plt.plot(histr)
plt.plot(histr2)
plt.show()
#plt.hist(output.ravel(),256,[0,256]); plt.show()
#plt.hist(img.ravel(),256,[0,256]); plt.show()
