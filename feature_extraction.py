import PIL.Image
import os
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import *


class extract_features():

    def __init__(self):
        pass

    def extract_features(img_path,save_directory, indicator):
        root=Tk()
        messagebox.showinfo("ATTENTION PLEASE", "Processing.... Click OK and Wait...")
        root.destroy()
        w=28
        h=28
        if indicator == 1:
            img = PIL.Image.open(os.path.join(img_path))
            img = img.resize((w, h), PIL.Image.BILINEAR)
            print('1')
        else:
            img = PIL.Image.open(os.path.join(img_path))
            print('2')
        pixels = list(img.getdata())
        width, height = img.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        pixels = np.ravel(pixels)
        save_dir = save_directory + '/temp.csv'
        np.savetxt(save_dir, pixels, delimiter=",")
        file = save_directory + '/temp.csv'
        print('Opening file  ' + file)
        save_dir1 = save_directory + '/features.csv'
        pd.read_csv(file, header=None).T.to_csv(save_dir1, header=False, index=False)
        print('tranposing  ' + file)
        print('Saved  ' + save_dir1)
        root1=Tk()
        messagebox.showinfo("ATTENTION PLEASE", "The csv file has been saved in your selected folder/directory")
        os.remove(save_directory + '/temp.csv')
        root1.destroy()

