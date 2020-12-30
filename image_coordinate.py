#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import numpy as np
#from PIL import Image
img =mpimg.imread("C:\\Users\\Priyanka Shahasane\\Desktop\\Automatic_Certifications\\Template.jpg")
print(img)
imgplot = plt.imshow(img)
plt.show()
