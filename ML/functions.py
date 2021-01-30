import numpy as np 
import math


def basic_sigmoid(x):
    return (1/(1+(1/math.exp(x))))

def sigmoid(x):
    return (1/(1+(1/np.exp(x))))

def sigmoid_grad(x):
    s = sigmoid(x)
    return (s*(1 - s))

def normaliseRows(x):
    x_norm = np.linalg.norm(x,axis=1, keepdims=True)
    return (x/x_norm)

def image2vector(image):
    v = np.array(image)
    return (v.reshape(v.shape[0]*v.shape[1]*v.shape[2], 1))

def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x,axis=1, keepdims= True)
    return x_exp/x_sum

def l2(yhat,y):
    loss = yhat - y
    return np.dot(loss, loss)

def l1(yhat,y):
    loss = yhat - y
    loss = np.absolute(loss)
    return np.sum(loss)


