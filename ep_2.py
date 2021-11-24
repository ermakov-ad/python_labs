import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "flights.csv"

data = pd.read_csv(path, sep=',')

data_sum = data.groupby('CARGO').sum()

data_sum.iloc[:, 0] = data_sum.iloc[:, 0].apply(lambda x: ((x*8.0 + 1)**0.5)/2.0 - 0.5)
print(data_sum)

bar_numbers = range(len(data_sum))

labels = list(data_sum.index)

y_label = ['counts', 'prices', 'weights']

for i in range(3):
    fig, ax = plt.subplots()
    ax.bar(bar_numbers, data_sum.iloc[:, i])
    ax.set_xticks(bar_numbers)
    ax.set_xticklabels(labels)
    ax.set_xlabel('CARGO')
    ax.set_ylabel(y_label[i])
    plt.savefig(y_label[i] + ".png", dpi=500)
    print('graph ' + y_label[i] + ' saved')
