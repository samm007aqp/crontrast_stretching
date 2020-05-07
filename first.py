import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('woman.jpg')
row,cols,channels = img.shape
smallest = np.amin(img)
biggest = np.amax(img)


output = img.copy()
lista = []
for i in range (row):
    for j in range (cols):        
        lista.append(img[i][j][0])
        output[i][j] =  (img[i][j]-smallest)*(255/(biggest-smallest))

print("min value %s max value %s" % (smallest , biggest))

cv2.imwrite('outputcell.png',output)
smallest = np.amin(output)
biggest = np.amax(output)
print( "maximo:" + str(biggest)+"minimo"+str(smallest))

cv2.imshow('input',img)
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
