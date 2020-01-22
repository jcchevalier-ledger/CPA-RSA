import numpy as np


def read_curve(curve_index):
    """
    This function reads the .txt files containing the consumption' curves
    :param curve_index: the index of the curve
    :return: a list containing the curve's data
    """
    f = open("data/curve_" + str(curve_index) + ".txt", "r")
    data = str.split(f.read())
    data = [float(data[j]) for j in range(28)]
    return data


def read_message(message_index):
    """
    This function reads the .txt files containing the messages
    :param message_index: the index of the message
    :return: an integer (the message)
    """
    f = open("data/msg_" + str(message_index) + ".txt", "r")
    data = int(f.read())
    return data


def get_n():
    """
    This function reads the .txt file containing the prime number necessary to communicate with a RSA algorithm
    :return: a integer (the prime number)
    """
    f = open("data/N.txt", "r")
    data = int(f.read())
    return data


def M_d_modN(M, d, N):
    """
    Compute the RSA exponentiation and return the Hamming weight of T (operation square) and
     T (T*M) the fot last bit of the key
    :param M: Message (int)
    :param d: Key a list of 0 or 1 representing the binary
    :param N: Primary used for the algorithm
    :return: List of Hamming weights.
    """
    result = [0]
    T = M
    for i in range(len(d) - 2, -1, -1):
        T = (T ** 2) % N
        if d[i] == 1:
            T = (T * M) % N
            if i == 0:
                result[0] = hamming_weight(T)
        else:
            if i == 0:
                T = (T ** 2) % N
                result[0] = hamming_weight(T)
    return result


def bitfield(n):
    """
    transform a int into a list of bit 0 or 1
    :param n:
    :return:
    """
    bit_array = [int(digit) for digit in bin(n)[2:]]
    bit_array.reverse()
    return bit_array


def hamming_weight(n):
    """
    Return the Hamming weight of an int
    :param n: The int to return the hamming weight of
    :return:
    """
    return sum(bitfield(n))


def hack(N, curves, messages):
    """

    :param N:
    :param curves:
    :param messages:
    :return:
    """
    d = [1]  # initialize d
    count = 1
    while count < 28:  # TODO : Check comparison value
        array_hamming_weight_zero = np.zeros((1000, 1))
        array_hamming_weight_one = np.zeros((1000, 1))
        for index, message in enumerate(messages):
            temp_d = [0] + d
            hamming_weights = M_d_modN(message, temp_d, N)
            array_hamming_weight_zero[index] = hamming_weights
            temp_d = [1] + d
            hamming_weights = M_d_modN(message, temp_d, N)
            array_hamming_weight_one[index] = hamming_weights
        cor0 = np.corrcoef(array_hamming_weight_zero, curves[:, count:count + 1], False)
        cor1 = np.corrcoef(array_hamming_weight_one, curves[:, count:count + 1], False)
        cor0_val = cor0[0][1]
        cor1_val = cor1[0][1]
        if abs(cor1_val) > abs(cor0_val):
            d = [1] + d
            count += 2
        else:
            d = [0] + d
            count += 1
        print(d)


if __name__ == "__main__":
    # Variable global pour N
    N = get_n()
    array_curves = np.zeros((1000, 28))
    array_messages = []
    for i in range(1000):
        array_curves[i] = read_curve(i)
        array_messages.append(read_message(i))
    hack(N, array_curves, array_messages)
