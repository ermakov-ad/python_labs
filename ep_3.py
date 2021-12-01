import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

path_info = "students\\students_info.xlsx"
path_results = "students\\results_ejudge.html"

my_sheet = "logins"
info = read_excel(path_info, sheet_name = my_sheet).rename(columns={'login':'User'})
results = pd.read_html(path_results)[0]

data = info.merge(results)

a_ans = data.groupby('group_faculty').mean()

figure, gr = plt.subplots()
label = list(a_ans.index)
gr.bar(range(len(label)), a_ans.iloc[:, 10])
gr.set_xticks(range(len(label)))
gr.set_xticklabels(label)
gr.set_title("results/group_faculty")
#plt.show()
plt.savefig("results for group_faculty.png")

b_ans = data.groupby('group_out').mean()

figure, gr = plt.subplots()
label = list(b_ans.index)
gr.bar(range(len(label)), b_ans.iloc[:, 10])
gr.set_xticks(range(len(label)))
gr.set_xticklabels(label)
gr.set_title("results/group_out")
#plt.show()
plt.savefig("results for group_out.png")

print(data[data['H'] + data['G'] >= 10].loc[:,['User', 'group_faculty', 'group_out', 'G', 'H']])