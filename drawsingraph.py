import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")


def drawsingraph(angle):
    A = 0.5 * angle  # 振幅を角度に応じて調整します
    f = 1.0  # 周波数 Hz
    sec = 3.0  # 信号の長さ s
    sf = 44100  # サンプリング周波数 Hz

    t = np.arange(0, sec, 1 / sf)  # サンプリング点の生成
    y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

    plt.plot(t, y)
    plt.savefig("GeneratedData/sin.png")
