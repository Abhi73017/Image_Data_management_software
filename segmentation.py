"""

This module is an implementation of Otsu's method of segmentation
@Author - Abhishek Kumar - Student(EEE) , Gaya College of Engineering, Gaya


"""

import math
import numpy as np
from matplotlib import pyplot as plt
import PIL.Image

threshold_values = {}


class Otsu_segmentation():

    def __init__(self):
        self.h = [1]

    def Hist(self,img):
        row, col = img.shape
        y = np.zeros(256)
        for i in range(0, row):
            for j in range(0, col):
                y[img[i, j]] += 1
        x = np.arange(0, 256)
        plt.bar(x, y, color='b', width=5, align='center', alpha=0.25)
        plt.show()
        return y

    def regenerate_img(self,img, threshold):
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

    def weight(self,s, e):
        w = 0
        for i in range(s, e):
            w += self.h[i]
        return w

    def mean(self,s, e):
        m = 0
        w = self.weight(s, e)
        for i in range(s, e):
            m += self.h[i] * i

        return m / float(w)

    def variance(self,s, e):
        v = 0
        m = self.mean(s, e)
        w = self.weight(s, e)
        for i in range(s, e):
            v += ((i - m) ** 2) * self.h[i]
        v /= w
        return v

    def threshold(self,h):
        self.h = h
        cnt = Otsu_segmentation.countPixel(h)
        for i in range(1, len(h)):
            vb = self.variance(0, i)
            wb = self.weight(0, i) / float(cnt)
            mb = self.mean(0, i)

            vf = self.variance(i, len(h))
            wf = self.weight(i, len(h)) / float(cnt)
            mf = self.mean(i, len(h))

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

    def get_optimal_threshold(self):
        min_V2w = min(threshold_values.values())
        optimal_threshold = [k for k, v in threshold_values.items() if v == min_V2w]
        print('optimal threshold', optimal_threshold[0])
        return optimal_threshold[0]

    def segment(file):
        image = PIL.Image.open(file).convert("L")
        img = np.asarray(image)
        a = Otsu_segmentation()
        h = a.Hist(img)
        a.threshold(h)
        plt.savefig('otsu.jpg')
