import matplotlib.pyplot as plt

with open('C:\\Users\\Admin\\Documents\\py\\mpl_lab\\data_ep_2\\data.txt', 'r') as f:
    file = f.readlines()
    n = -1
    ind = 0
    max_x = min_x = max_y = min_y = 0
    for line in file:
        if ind == 0:
            x = list(map(float, line.split()))
            ind = 1
            max_x = max(max(x), max_x)
            min_x = min(min(x), min_x)
        else:
            ind = 0
            y = list(map(float, line.split()))
            max_y = max(max(y), max_y)
            min_y = min(min(y), min_y)

    for line in file:
        if ind == 0:
            x = list(map(float, line.split()))
            ind = 1
        else:
            ind = 0
            n += 1
            y = list(map(float, line.split()))
            figure, gr = plt.subplots()
            gr.plot(x, y)
            gr.grid(True)
            plt.xlim([round(min_x * 1.1), round(max_x * 1.1)])
            plt.ylim([round(min_y * 1.1), round(max_y * 1.1)])
            gr.set_title("Frame " + str(n))
            plt.savefig("Frame 0" + str(n) + ".png", dpi=2000)
            print("Frame " + str(n) + " saved")
