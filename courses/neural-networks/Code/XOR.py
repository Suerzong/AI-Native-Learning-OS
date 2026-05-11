import numpy as np

# ---- XOR 数据 ----

X = np.array([[1,1,0,1,0],
              [1,0,1,0,1]])
y = np.array([0,1,1,1,1])
m = X.shape[1]

#---- 初始化 ----
np.random.seed(114514)
W1 = np.random.randn(5, 2) * 0.5
b1 = np.zeros((5, 1))
W2 = np.random.randn(1, 5) * 0.5
b2 = np.zeros((1, 1))
lr = 1.0

#---- 训练 ----
for epoch in range(500):
    # 前向传播
    z1 = W1 @ X + b1
    a1 = np.maximum(z1, 0)
    z2 = W2 @ a1 + b2
    a2 = 1 / (1 + np.exp(-z2))

    output = a2
    #compute loss
    loss = -np.mean(y * np.log(output + 1e-8) + (1 - y) * np.log(1 - output + 1e-8))

    #reverse 
    dz2 = a2 - y
    dW2 = (1 / m) * dz2 @ a1.T
    db2 = (1 / m) * np.sum(dz2, axis = 1, keepdims = True)

    da1 = W2.T @ dz2
    dz1 = da1 * (z1 > 0)
    dW1 = (1 / m) * dz1 @ X.T
    db1 = (1 / m) * np.sum(dz1, axis = 1, keepdims= True)

    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

    if epoch % 50 == 0:
        print(f"epoch:{epoch}:loss:{loss:.3f}, a2 = {np.round(a2, 3)}")

# ---- 最终结果 ----
print(f"\n最终预测: {np.round(a2, 3)}")
print(f"真实标签: {y}")
print(f"预测是否接近: {np.allclose(np.round(a2), y)}")
