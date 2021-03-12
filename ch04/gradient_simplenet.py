# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.functions import softmax, cross_entropy_error
# from common.gradient import numerical_gradient


def numerical_gradient(f, w):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(w)

    # weight 값 하나씩 접근
    it = np.nditer(w, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        weight_value = w[idx]
        w[idx] = float(weight_value) + h
        fxh1 = f(w)  # f(x+h)

        w[idx] = weight_value - h
        fxh2 = f(w)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        w[idx] = weight_value  # 값 복원
        it.iternext()

    return grad



class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()
print('weight 값')
print(net.W)

# lambda 인자: 함수
# 클래스인 경우 매개변수를 입력값으로 넣어 줄수 있나보다
# lambda 매개변수: 클래스
f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print('weight 기울기 값')
print(dW)
