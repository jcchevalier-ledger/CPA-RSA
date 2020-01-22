import numpy as np


def read_curve(curve_index):
    f = open("data/curve_" + str(curve_index) + ".txt", "r")
    data = str.split(f.read())
    data = [float(data[j]) for j in range(28)]
    return data


def read_message(message_index):
    f = open("data/msg_" + str(message_index) + ".txt", "r")
    data = int(f.read())
    return data


def get_n():
    f = open("data/N.txt", "r")
    data = int(f.read())
    return data


if __name__ == "__main__":
    prime = get_n()
    array_curves = np.zeros((1000, 28))
    array_messages = []
    for i in range(1000):
        array_curves[i] = read_curve(i)
        array_messages.append(read_message(i))
