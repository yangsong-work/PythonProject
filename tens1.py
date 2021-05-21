import tensorflow as tf

if __name__=="__main__":

    # 创建一个常量运算操作，产生一个 1×2 矩阵
    matrix1 = tf.constant([[3., 3.]])
    # 创建另外一个常量运算操作，产生一个 2×1 矩阵
    matrix2 = tf.constant([[2.],[2.]])
    # 创建一个矩阵乘法运算 ，把matrix1和matrix2作为输入
    # 返回值product代表矩阵乘法的结果
    product = tf.matmul(matrix1, matrix2)

    with tf.compat.v1.Session() as sess:
        with tf.device("/gpu:1"):
         result = sess.run([product])
    print (result)
