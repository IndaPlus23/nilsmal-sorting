import matplotlib.pyplot as plt
import numpy as np
ax  = plt.gca()

def visualize(bars, array):
    for bar, height in zip(bars, array):
        bar.set_height(height)

    plt.draw()
    plt.pause(0.000001)


def run_frontend(arr):
    ax.clear()  # Clear the current axes
    visualize(ax.bar([e for e in range(len(arr))], arr), arr)

def run_frontend_final(arr):
    ax.clear()  # Clear the current axes
    for bar, height in zip(ax.bar([e for e in range(len(arr))], arr), arr):
        bar.set_height(height)
    plt.draw()
    plt.pause(10000)

if __name__ == '__main__':
    amount_of_elements = 1000

    bars = ax.bar([e for e in range(amount_of_elements)], np.random.rand(amount_of_elements))
    for _ in range(10):
        arr = np.random.rand(amount_of_elements)
        visualize(bars, arr)
