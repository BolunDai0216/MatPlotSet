import numpy as np
import pickle


def generate_shape(basesize, mean=1.0, std=0.5, low=1, high=6, size=10, nums=1000):
    rhos = size * basesize

    phis = np.linspace(1e-4, 2 * np.pi, nums)
    amps = np.random.normal(mean, std, size)
    Ts = np.random.randint(low, high=high, size=size)

    for i in range(size):
        if i % 3 == 0:
            rhos += amps[i] * np.cos(Ts[i] * phis)
        else:
            rhos += amps[i] * np.sin(Ts[i] * phis)

    cart_xs = rhos * np.cos(phis)
    cart_ys = rhos * np.sin(phis)

    return cart_xs, cart_ys


def save_shape(xs, ys, filename, folder="./"):
    data = {"xs": xs, "ys": ys}

    with open(f"{folder}{filename}.pickle", "wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"saved at {folder}{filename}.pickle")


def read_shape(filename):
    with open("filename", "rb") as handle:
        data = pickle.load(handle)

    xs = data["xs"]
    ys = data["ys"]

    return xs, ys
