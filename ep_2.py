import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

path = "flights.csv"

data = pd.read_csv(path, sep=',')

data_count = data.groupby('CARGO').count()
data_sum = data.groupby('CARGO').sum()
data_sum.iloc[:, 0] = data_count.iloc[:, 0]

#data_sum.iloc[:, 0] = data_sum.iloc[:, 0].apply(lambda x: ((x*8.0 + 1)**0.5)/2.0 + 0.5) # (sum(0, 1, 2, ... n))^(-1), f(sum) = n
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
    plt.savefig(y_label[i] + ".png")
    print('graph ' + y_label[i] + ' saved')
