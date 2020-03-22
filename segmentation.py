#this module is an implementation of otsu's method of segmentation

import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

threshold_values = {}
h = [1]

class Otsu_segmentation():

    def __init__(self):
        pass

    def Hist(img):
        row, col = img.shape
        y = np.zeros(256)
        for i in range(0, row):
            for j in range(0, col):
                y[img[i, j]] += 1
        x = np.arange(0, 256)
        plt.bar(x, y, color='b', width=5, align='center', alpha=0.25)
        plt.show()
        return y

    def regenerate_img(img, threshold):
        row, col = img.shape
        y = np.zeros((row, col))
        for i in range(0, row):
            for j in range(0, col):
                if img[i, j] >= threshold:
                    y[i, j] = 255
                else:
                    y[i, j] = 0
        return y

    def countPixel(h):
        cnt = 0
        for i in range(0, len(h)):
            if h[i] > 0:
                cnt += h[i]
        return cnt

    def wieght(s, e):
        w = 0
        for i in range(s, e):
            w += h[i]
        return w

    def mean(s, e):
        m = 0
        w = Otsu_segmentation.wieght(s, e)
        for i in range(s, e):
            m += h[i] * i

        return m / float(w)

    def variance(s, e):
        v = 0
        m = Otsu_segmentation.mean(s, e)
        w = Otsu_segmentation.wieght(s, e)
        for i in range(s, e):
            v += ((i - m) ** 2) * h[i]
        v /= w
        return v

    def threshold(h):
        cnt = Otsu_segmentation.countPixel(h)
        for i in range(1, len(h)):
            vb = Otsu_segmentation.variance(0, i)
            wb = Otsu_segmentation.wieght(0, i) / float(cnt)
            mb = Otsu_segmentation.mean(0, i)

            vf = Otsu_segmentation.variance(i, len(h))
            wf = Otsu_segmentation.wieght(i, len(h)) / float(cnt)
            mf = Otsu_segmentation.mean(i, len(h))

            V2w = wb * (vb) + wf * (vf)
            V2b = wb * wf * (mb - mf) ** 2

            fw = open("trace.txt", "a")
            fw.write('T=' + str(i) + "\n")

            fw.write('Wb=' + str(wb) + "\n")
            fw.write('Mb=' + str(mb) + "\n")
            fw.write('Vb=' + str(vb) + "\n")

            fw.write('Wf=' + str(wf) + "\n")
            fw.write('Mf=' + str(mf) + "\n")
            fw.write('Vf=' + str(vf) + "\n")

            fw.write('within class variance=' + str(V2w) + "\n")
            fw.write('between class variance=' + str(V2b) + "\n")
            fw.write("\n")

            if not math.isnan(V2w):
                threshold_values[i] = V2w

    def get_optimal_threshold():
        min_V2w = min(threshold_values.values())
        optimal_threshold = [k for k, v in threshold_values.items() if v == min_V2w]
        print('optimal threshold', optimal_threshold[0])
        return optimal_threshold[0]


image = Image.open('gray_test.png').convert("L")
img = np.asarray(image)

h = Otsu_segmentation.Hist(img)
Otsu_segmentation.threshold(h)
op_thres = Otsu_segmentation.get_optimal_threshold()

res = Otsu_segmentation.regenerate_img(img, op_thres)
plt.imshow(res)
plt.savefig("otsu.png")