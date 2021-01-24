import numpy as np
x = np.random.normal(size=(20,20))
temp = np.matmul(x,x.transpose())
temp = np.linalg.inv(temp)
y = np.empty([20,1], dtype= 'int32')
temp2 = np.matmul(x.transpose(), y)
thita = np.matmul(temp, temp2)
#print(thita)
#print(y.dtype)