import numpy as np
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self, n_features, learning_rate=0.1):
        # 初始化权重和偏置
        self.w = np.random.randn(n_features) * 0.01
        self.b = 0
        self.learning_rate=learning_rate
        self.dim=n_features

    def activation(self, x):
        # 阶跃激活函数
        if x >= 0:
            return 1
        else:return -1

    def predict(self, x):
        # 预测单个样本
        return self.activation(self.w.dot(x)+self.b)

    def train(self, X, y, epochs=100):
        # 训练感知机
        #由于数据集较小，这里采用更为熟悉的BGD策略;给出代码似乎希望train函数返回errors，大概是训练错误分类数。
        errors=[]
        for i in range(epochs):
            error=0
            sum_grad_w=np.zeros(self.dim)
            sum_grad_b=0
            for j in range(len(X)):
                if self.predict(X[j])!=y[j]:
                    sum_grad_w += X[j]*y[j]
                    sum_grad_b += y[j]
                    error+=1
            
            if error==0:
                break

            self.w += self.learning_rate*sum_grad_w
            self.b += self.learning_rate*sum_grad_b

            errors.append(error)
        
        return errors


# 测试代码
if __name__ == "__main__":
    # 生成数据集
    np.random.seed(42)
    X1 = [[x, y] for x, y in zip(np.random.normal(2, 0.5, 50), np.random.normal(2, 0.5, 50))]
    X2 = [[x, y] for x, y in zip(np.random.normal(-2, 0.5, 50), np.random.normal(-2, 0.5, 50))]
    X = X1 + X2
    y = [1] * 50 + [-1] * 50

    # 训练感知机
    p = Perceptron(n_features=2, learning_rate=0.1)
    errors = p.train(X, y, epochs=100)
    plt.rcParams['font.family'] = 'SimHei'

    # 绘制错误率变化
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
    plt.xlabel('训练轮数')
    plt.ylabel('错误分类数')
    plt.title('训练过程中的错误率')

    # 绘制决策边界和数据点
    plt.subplot(1, 2, 2)
    x_min, x_max = -4, 4
    y_min, y_max = -4, 4
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    Z = np.array([p.predict([x, y]) for x, y in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter([x[0] for x in X1], [x[1] for x in X1], c='b', marker='o', label='类别 +1')
    plt.scatter([x[0] for x in X2], [x[1] for x in X2], c='r', marker='x', label='类别 -1')
    plt.xlabel('特征1')
    plt.ylabel('特征2')
    plt.title('决策边界与数据分布')
    plt.legend()
    plt.tight_layout()
    plt.show()