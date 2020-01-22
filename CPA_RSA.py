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


if __name__ == "__main__":
    read_curve(0)
