# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import zipfile
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#     sess = tf.compat.v1.Session()

    # a = tf.constant(10)
    # b = tf.constant(12)
    # sess.run(a+b)
    #
    # #建立词典
    # def read_data(filename):
    #     with zipfile.ZipFile(filename) as f:
    #      data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    #     return data


    # t = tf.add(8, 9)
    # print(t)  # 输出 Tensor("Add_1:0", shape=(), dtype=int32)
    # 创建图
    a = tf.constant([1.0, 2.0])
    b = tf.constant([3.0, 4.0])
    c = a * b
    # 创建会话
    sess = tf.compat.v1.Session()
    # 计算c
    print (sess.run(c) ) # 进行矩阵乘法，输出[3., 8.]
    sess.close()
