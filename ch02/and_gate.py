# coding: utf-8
"""ANDゲートの実装"""
import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])  #[0 0]
    w = np.array([0.5, 0.5]) #[0.5 0.5]
    b = -0.7  #バイアス -1<b<0の値のみ可
    tmp = np.sum(w*x) + b
    #sum(w*x) : wとxの要素ごとの積を計算してその和を出力

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
# 出力
# (0, 0) -> 0
# (1, 0) -> 0
# (0, 1) -> 0
# (1, 1) -> 1


"""
-*- ポイント -*-
リストをnp.arrayにすることで要素ごとの計算ができるようになる
numpyは行列計算を行うときに使うと便利
(0, 1)などのタプルもstr()を使ってstr型に変換できる
"""
