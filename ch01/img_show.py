# coding: utf-8
"""画像の表示"""
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/lena.png') # 画像の読み込み
plt.imshow(img)
#画像表示のためのメソッド

plt.show()

"""
-*- ポイント -*-
from matplotlib.image import imread
imread('画像の情報')
plt.imshow(画像)
"""
