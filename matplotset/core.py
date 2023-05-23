import numpy as np
import pickle


def generate_shape(
    basesize,
    mean=1.0,
    std=0.5,
    low=1,
    high=6,
    size=10,
    nums=1000,
    alt_freq=3,
    scale=1.0,
    x_offset=0.0,
    y_offset=0.0,
    seed=None,
    return_polar=False,
):
    if seed is not None:
        np.random.seed(seed)

    rhos = size * basesize
    phis = np.linspace(0.0, 2 * np.pi, nums)
    amps = np.random.normal(mean, std, size)
    Ts = np.random.randint(low, high=high, size=size)

    for i in range(size):
        if i % alt_freq == 0:
            rhos += amps[i] * np.cos(Ts[i] * phis)
        else:
            rhos += amps[i] * np.sin(Ts[i] * phis)

    cart_xs = scale * rhos * np.cos(phis) + x_offset
    cart_ys = scale * rhos * np.sin(phis) + y_offset

    if return_polar:
        return cart_xs, cart_ys, scale * rhos, phis
    else:
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
