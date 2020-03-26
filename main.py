from PySide2 import QtWidgets
from GUI import Ui_IDMS
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from segmentation import Otsu_segmentation


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_IDMS()
        self.ui.UI_Setup(self)

        self.ui.startButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(self.browse_image_for_segmentation)
        self.ui.pushButton_6.clicked.connect(self.browse_folder_to_save_segmented_image)
        self.ui.pushButton_7.clicked.connect(self.run_segmentation)

    def browse_image_for_segmentation(self):
        root = Tk()
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select the Image", filetypes=(
        ("jpeg files", "*.jpg",), ("png files", "*.png")))
        print(self.filename)
        root.destroy()
        if self.filename is not None:
            self.ui.textBrowser_4.setText("Selected")

    def browse_folder_to_save_segmented_image(self):
        root=Tk()
        messagebox.showinfo("ATTENTION PLEASE", "The function hasn't been created yet. Your segmented image will be "
                                                "saved in your working directory.")
        root.destroy()

    def run_segmentation(self):
        Otsu_segmentation.segment(self.filename)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

