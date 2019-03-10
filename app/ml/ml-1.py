from __future__ import print_function
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# -------------------创建数据---------------------
# 神经网络也就是学着把 Weights 变成 0.1, biases 变成 0.3
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3
# -------------------创建数据---------------------



# -------------------搭建模型---------------------
### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = Weights*x_data + biases
#-------------------搭建模型---------------------



#-------------------计算误差---------------------
loss = tf.reduce_mean(tf.square(y-y_data))
#-------------------计算误差---------------------


#-------------------传播误差---------------------
# 反向传递误差的工作就教给optimizer了, 我们使用的误差传递方法是梯度下降法:
# Gradient Descent 让后我们使用 optimizer 来进行参数的更新
optimizer = tf.train.GradientDescentOptimizer(0.5)   #优化器, 学习效率为0.5
train = optimizer.minimize(loss)
### create tensorflow structure end ###
#-------------------传播误差---------------------



#-------------------训练---------------------
# 创建会话 Session
sess = tf.Session()
# 用 Session 来执行 init 初始化步骤, 先初始化所有之前定义的Variable
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess.run(init)

# 用 Session 来 run 每一次 training 的数据. 逐步提升神经网络的预测准确性, 训练201步
for step in range(201):
    sess.run(train)
    if step % 10 == 0:   # 每训练10步，打印一次
        print(step, sess.run(Weights), sess.run(biases))
#-------------------训练---------------------
