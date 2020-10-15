import torch as t
from torch.autograd.variable import Variable as v

a = v(t.ones(3, 4))
print(a)
b = v(t.zeros(3, 4))
print(b)


def f(x):
    y = x ** 2 * t.exp(x)
    return y


def gradf(x):
    dx = 2 * x * t.exp(x) + x ** 2 * t.exp(x)
    return dx


x = v(t.randn(3, 4), requires_grad=True)
print("x",x)
y = f(x)
print(y)
y.backward(t.ones(y.size()))
print("--")
print(x.grad)
print(gradf(x))