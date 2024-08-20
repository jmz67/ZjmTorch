from step01 import *
import numpy as np

class Function:
    # 注意这里的 __call__ 方法，需要在 f = Square() 之后再调用 f(x)
    # 如果使用 __init__ 方法，则需要在 f = Square() 的时候输入参数
    def __call__(self, input):
        x = input.data
        y = self.forward(x) # 具体的计算在 forward 函数中实现
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()
    
class Square(Function):
	def forward(self, x):
		return x ** 2
      
x = Variable(np.array(2.0))
f = Square()
y = f(x)
print(y.data) # 输出 4.0

