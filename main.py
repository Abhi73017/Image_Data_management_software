from PySide2 import QtWidgets
from GUI import Ui_IDMS
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from segmentation import Otsu_segmentation
from feature_extraction import extract_features


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.flag = 0
        self.img_file = ''
        self.img_file1 = ''
        self.filepath = ''
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_IDMS()
        self.ui.UI_Setup(self)

        self.ui.startButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(self.browse_image_for_segmentation)
        self.ui.pushButton_6.clicked.connect(self.browse_folder_to_save_segmented_image)
        self.ui.pushButton_7.clicked.connect(self.run_segmentation)
        self.ui.pushButton.clicked.connect(self.browse_image_for_feature_extraction)
        self.ui.pushButton_2.clicked.connect(self.select_image_folder)
        self.ui.pushButton_3.clicked.connect(self.select_path_for_saving_csv_file)
        self.ui.pushButton_4.clicked.connect(self.trigger_feature_extraction)

    def browse_image_for_segmentation(self):
        root = Tk()
        self.img_file = filedialog.askopenfilename(initialdir="/", title="Select the Image", filetypes=(
        ("jpeg files", "*.jpg",), ("png files", "*.png")))
        print(self.img_file)
        root.destroy()
        if len(self.img_file) != 0:
            self.ui.textBrowser_4.setText("Selected")
        if len(self.img_file) == 0:
            root1=Tk()
            messagebox.showwarning("WARNING", "You haven't selected any Image for segmentation")
            root1.destroy()

    def browse_folder_to_save_segmented_image(self):
        root=Tk()
        messagebox.showinfo("ATTENTION PLEASE", "The function hasn't been created yet. Your segmented image will be "
                                                "saved in your working directory.")
        root.destroy()

    def run_segmentation(self):
        if len(self.img_file) != 0:
            Otsu_segmentation.segment(self.img_file)
        else:
            root = Tk()
            messagebox.showerror("ERROR", "Please select the required objects")
            root.destroy()

    def browse_image_for_feature_extraction(self):
        root = Tk()
        self.img_file1 = filedialog.askopenfilename(initialdir="/", title="Select the Image", filetypes=(
            ("jpeg files", "*.jpg",), ("png files", "*.png")))
        print(self.img_file1)
        root.destroy()
        if len(self.img_file1) != 0:
            self.ui.textBrowser.setText("Selected")
        if len(self.img_file1) == 0:
            root1 = Tk()
            messagebox.showwarning("WARNING", "You haven't selected any Image for feature extraction")
            root1.destroy()

    def select_image_folder(self):
        root=Tk()
        messagebox.showinfo("ATTENTION PLEASE", "This Feature has not been developed yet but I make sure it will be "
                                                "available soon.")
        root.destroy()

    def select_path_for_saving_csv_file(self):
        root = Tk()
        self.filepath = filedialog.askdirectory(initialdir="/", title="Select the folder to save csv file")
        print(self.filepath)
        root.destroy()
        if len(self.filepath) != 0:
            self.ui.textBrowser_3.setText("Selected")
        if len(self.filepath) == 0:
            root1=Tk()
            messagebox.showwarning("WARNING", "The PCA feature is not available at this time. It will be available soon")
            root1.destroy()

    def trigger_feature_extraction(self):
        if len(self.filepath) != 0 and len(self.img_file1) != 0:
            if self.ui.checkBox.isChecked():
                self.flag = 1
            if self.ui.checkBox_2.isChecked():
                root = Tk()
                messagebox.showerror("ERROR", "The PCA feature is not Available")
                root.destroy()
            extract_features.extract_features(self.img_file1, self.filepath, self.flag)

        else:
            root = Tk()
            messagebox.showerror("ERROR", "Please select the required objects")
            root.destroy()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

