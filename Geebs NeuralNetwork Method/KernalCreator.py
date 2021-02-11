import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from BaseFunctions import *

info1 = load_stocks_1h("GBPUSD", dt.datetime.strptime("01/01/2018 0:00:00", "%d/%m/%Y %H:%M:%S"), ())
info2 = load_stocks_1h("EURUSD", dt.datetime.strptime("01/01/2018 0:00:00", "%d/%m/%Y %H:%M:%S"), ())
info3 = load_stocks_1h("EURJPY", dt.datetime.strptime("01/01/2018 0:00:00", "%d/%m/%Y %H:%M:%S"), ())
info4 = load_stocks_1h("AUDCHF", dt.datetime.strptime("01/01/2018 0:00:00", "%d/%m/%Y %H:%M:%S"), ())
info5 = load_stocks_1h("GBPCAD", dt.datetime.strptime("01/01/2015 0:00:00", "%d/%m/%Y %H:%M:%S"), ())

def extract(info):
    x = np.array([info[key]["CLOSE"] for key in sorted(info.keys())])
    return (x-np.mean(x))/np.std(x)
stock_data = np.concatenate([extract(info1), extract(info2), extract(info3), extract(info4), extract(info5)])
print(stock_data.shape)
del info1, info2, info3, info4, info5,
label_data = np.divide(np.roll(stock_data.copy(), -1), stock_data.copy())# + \
             #np.divide(np.roll(stock_data.copy(), -2), stock_data.copy()) + \
             #np.divide(np.roll(stock_data.copy(), -3), stock_data.copy()) + \
             #np.divide(np.roll(stock_data.copy(), -4), stock_data.copy()) + \
             #np.divide(np.roll(stock_data.copy(), -5), stock_data.copy())
label_data *= 0.2
label_data = (label_data-np.mean(label_data))/np.std(label_data)


label_data = 0.2*(np.roll(stock_data, -11)+np.roll(stock_data, -12)+np.roll(stock_data, -13)+np.roll(stock_data, -14)+np.roll(stock_data, -15))
labels = label_data / np.std(label_data)
label_data = np.zeros_like(labels)
label_data[np.where(labels <= -1)] = -1
label_data[np.where(labels >= 1)] = 1

length = stock_data.shape[0]
print(length)
def training():

    r_input_batch = tf.placeholder("float", (1, length, 1))
    r_label_batch = tf.placeholder("float", (1, length, 1))

    with tf.variable_scope("TEST", reuse=tf.AUTO_REUSE):
        weight1 = tf.get_variable("weights1", [21, 1, 1], initializer=tf.random_normal_initializer)
        nc = tf.nn.conv1d(r_input_batch, filters=weight1, stride=1, padding="SAME")

    cost_function = tf.math.reduce_sum(tf.square(tf.subtract(nc, r_label_batch)))
    backprop = tf.train.AdamOptimizer().minimize(cost_function)

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        epoch = 0

        while True:
            epoch += 1
            _, cost, kernal = sess.run([backprop, cost_function, weight1], feed_dict={
                r_input_batch: stock_data.copy().reshape([1, length, 1]),
                r_label_batch: label_data.copy().reshape([1, length, 1])
            })

            if epoch == 1:
                kernal1 = kernal[:, 0, 0]
            if epoch % 100 == 0:
                print(epoch, cost, list(np.round(kernal[:, 0, 0], 4)))
                plt.clf()
                plt.plot(kernal1)
                plt.plot(kernal[:, 0, 0])
                plt.pause(0.001)

training()