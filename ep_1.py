import matplotlib.pyplot as plt

way = 'C:\\Users\\Admin\\Documents\\py\\mpl_lab\\dead_moroz\\dead_moroz\\00'
for n in range(1, 6):
    with open((way + str(n) + '.dat'), 'r') as f:
        data = [s for s in (f.read()).split()]
        x = []
        y = []
        i = 1
        while i < int(data[0]) * 2:
            x.append(float(data[i]))
            y.append(float(data[i + 1]))
            i += 2
        figure, gr = plt.subplots()
        gr.plot(x, y, marker='.', markersize=0.5, linestyle='')
        gr.set_aspect('equal', adjustable='datalim')
        gr.set_title("Number of points: " + data[0])
        plt.savefig("map " + str(n) + ".png", dpi=500)
        print("map " + str(n) + " saved")
