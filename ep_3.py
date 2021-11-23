import matplotlib.pyplot as plt
import csv
import collections

def get_plot(file_name, plot_name, data):
    fig, gr = plt.subplots()
    labels = []
    for item in data:
        labels.append(item)

    sum_st = []
    for item in data:
        sum_st.append(sum(data[item]))
    gr.bar(labels, sum_st, label=str(10))
    for i in range(8, 0, -1):
        k = 0
        for item in data:
            sum_st[k] -= data[item][i]
            k += 1
        gr.bar(labels, sum_st, label=str(i + 1))

    fig.tight_layout()
    gr.legend()
    gr.set_title(plot_name)
    plt.savefig(file_name + ".png", dpi=2000)


preps = collections.defaultdict(lambda: [0] * 9)
groups = collections.defaultdict(lambda: [0] * 9)

with open("C:\\Users\\Admin\\Documents\\py\\mpl_lab\\students.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    for row in file_reader:
        preps[row[0]][int(row[2]) - 2] += 1
        groups[row[1]][int(row[2]) - 2] += 1

print(preps)
print(groups)
get_plot('prep', 'Marks per prep', preps)
get_plot('group', 'Marks per group', groups)