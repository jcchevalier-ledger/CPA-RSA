def read_curve(i):
    f = open("data/curve_" + str(i) + ".txt", "r")
    data = str.split(f.read())
    data = [float(i) for i in data]
    return data


def read_message(i):
    f = open("data/msg_" + str(i) + ".txt", "r")
    data = int(f.read())
    return data


def get_n():
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
    :return: List of Hamming weights. Can of len 1 or 2 depending on the last value of the key
    """
    result = [0]
    T = M
    for i in range(len(d) - 2, -1, -1):
        T = (T ** 2) % N
        result[0] = hamming_weight(T)
        if d[i] == 1:
            T = (T * M) % N
            if i == 0:
                result.append(hamming_weight(T))
        return result


def bitfield(n):
    """
    transform a int into a list of bit 0 or 1
    :param n:
    :return:
    """
    return [int(digit) for digit in bin(n)[2:]].reverse()


def hamming_weight(n):
    """
    Return the Hamming weight of an int
    :param n: The int to return the hamming weight of
    :return:
    """
    return sum(bitfield(n))


if __name__ == "__main__":
    # Variable global pour N
    N = get_n()
    read_curve(0)
