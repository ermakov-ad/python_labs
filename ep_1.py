import numpy as np
from PIL import Image

file_path1 = 'lunar_images\\lunar0'
file_path2 = '_raw'
file_format = '.jpg'
for i in range(1, 4):
    # считаем картинку в numpy array
    img = Image.open(file_path1 + str(i) + file_path2 + file_format)
    data = np.array(img)

    a = data.min()
    b = data.max()
    ndata = ((data - a) / (b-a) * 255).astype(int)

    # запись картинки после обработки
    res_img = Image.fromarray(ndata)
    res_img = res_img.convert("RGB")
    res_img.save(file_path1 + str(i) + file_path2 + '_changed' + file_format)
    print('image ' + str(i) + ' saved')