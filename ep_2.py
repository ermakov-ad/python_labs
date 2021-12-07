import numpy as np
import matplotlib.pyplot as plt

file_path = 'signals\\signal0'
file_format = '.dat'
for i in range(1, 4):
    data = np.loadtxt(file_path + str(i) + file_format,unpack=True)
    T = np.linspace(0, len(data-1), len(data))
    data_changed = np.zeros(len(data))
    for j in range(0, 9):
        data_changed[j] = data[0:j+1].mean()
    for j in range(9, len(data)):
        data_changed[j] = data[j-9:j+1].mean()

    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].plot(T, data)
    axs[1].plot(T, data_changed)
    axs[0].set_title("signal")
    axs[1].set_title("changed signal")
    fig.tight_layout()
    #plt.show()
    plt.savefig("changed signal0" + str(i) + ".png")
    print('signal ' + str(i) + ' saved')