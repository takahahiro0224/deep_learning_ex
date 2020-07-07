import numpy as np
import matplotlib.pyplot as plt

# %%
# 0から6まで0.1刻みで作成
x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# %%

# ラベルなどを設定してグラフ表示
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle ="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

# %%
# 画像の表示 matplotlib.image.imread()を使う

import matplotlib.pyplot as plt
from matplotlib.image import imread

# プロジェクトのルートから実行する場合の相対パス,　別の場所から実行する場合は適宜書き換える
img = imread('data/images/british-shorthair.jpeg')
plt.imshow(img)
plt.show()