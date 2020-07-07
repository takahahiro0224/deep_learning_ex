import numpy as np

'''
intelliJのScientificモードについて
https://pleiades.io/help/idea/matplotlib-support.html
'''


# 引数にpythonのlistをとる
x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)

# %%
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)


# %%
x = np.array([1.0, 2.0, 3.0])
x / 2.0

# %%
A = np.array([[1,2], [3,4]])
print(A)
A.shape
A.dtype

# %%
# 行列計算
B = np.array([[3,0],[0,6]])
print(A + B)
print(A * B)

# %%
# ブロードキャストの例
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20]) #[[10, 20], [10, 20]]と同じ
print(A * B)

# %%
# 要素へのアクセス

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
X[0]
X[0][1]

# %%
for row in X:
    print(row)

# %%
X = X.flatten()
print(X)
print(X[np.array([0, 2, 4])])
print(X > 15)
print(X[X>15])