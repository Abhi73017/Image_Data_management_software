from PySide2 import QtWidgets
from GUI import Ui_IDMS
from tkinter import filedialog
from tkinter import *
import sys


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_IDMS()
        self.ui.setupUi(self)

        self.ui.startButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(self.browse_image_for_segmentation)

    def browse_image_for_segmentation(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select the Image", filetypes=(
        ("jpeg files", "*.jpg",), ("png files", "*.png"), ("all files", "*.*")))
        print(root.filename)
        root.destroy()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = ControlMainWindow()
    window.show()
    sys.exit(app.exec_())
