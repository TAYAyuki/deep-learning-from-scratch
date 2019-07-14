# coding: utf-8
"""グラフのタイトル,軸名の記載方法"""
import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
y1 = np.sin(x)
y2 = np.cos(x)

# グラフの描画
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")
# plot(x軸名,y軸名,linestyle = グラフの線を指定, label = グラフが何を表すかの説明(凡例))

plt.xlabel("x") # x軸のラベル
plt.ylabel("y") # y軸のラベル
#xlabel,ylabel : グラフの外に軸の名前をつける

plt.title('sin & cos')
#title :グラフの上にタイトルをつける

plt.legend()
#legend : label(凡例)を右上に表示する

plt.show()

"""
-*-  ポイント -*-
plt.plot(linesyle = ,label = )
plt.xlabel(" ")
plt.ylabel(" ")
plt.title(" ")
plt.legend()
"""
