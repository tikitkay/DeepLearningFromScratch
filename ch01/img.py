import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('cat.jpg') #이미지 읽어오기(적절한 경로를 설정하세요!)

plt.imshow(img)
plt.show()