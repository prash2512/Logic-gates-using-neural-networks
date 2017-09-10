import numpy as np;
x = np.array(([0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]))
x = x.T
y = np.array(([1,1,1,1,0],[0,0,0,0,1]))
w = np.random.rand(3,2)
def sigmoid(x,derivative=False):
    if derivative==True:
        return x*(1-x)
    y = 1/(1+np.exp(x))
    return y
for i in range(10000):
    output = sigmoid(np.dot(w.T,x))
    e = y-output
    delta =e*sigmoid(output,True)
    w =w + np.dot(x,delta.T)
    loss = np.mean((np.abs(e)))
    print loss
print y.shape
print x.shape