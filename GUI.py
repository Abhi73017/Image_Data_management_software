"""

This GUI file has been originally designed and developed by Abhishek Kumar - Student(EEE) , Gaya College of Engineering, Gaya

"""

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtGui import (QFont, QIcon)
from PySide2.QtWidgets import *


class Ui_IDMS(object):

    def __init__(self):
        pass

    def UI_Setup(self, IDMS):
        if IDMS.objectName():
            IDMS.setObjectName(u"IDMS")
        IDMS.setFixedSize(642, 480)
        IDMS.setAutoFillBackground(True)
        self.stackedWidget = QStackedWidget(IDMS)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 641, 481))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.graphicsView = QGraphicsView(self.page_1)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(-5, 0, 661, 491))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.graphicsView.setFont(font)
        self.graphicsView.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(232, 82, 93, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 171, 61))
        self.label.setAutoFillBackground(False)
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 90, 451, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 140, 231, 51))
        self.label_3.setAutoFillBackground(False)
        self.startButton = QPushButton(self.page_1)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(270, 300, 111, 41))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.startButton.setFont(font1)
        self.startButton.setLayoutDirection(Qt.LeftToRight)
        self.startButton.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        icon = QIcon()
        icon.addFile(u"start_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setAutoRepeat(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setFlat(False)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tabWidget = QTabWidget(self.page_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 631, 471))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.tabWidget.setFont(font2)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setTabletTracking(True)
        self.tabWidget.setFocusPolicy(Qt.StrongFocus)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.feature_tab = QWidget()
        self.feature_tab.setObjectName(u"feature_tab")
        self.graphicsView_2 = QGraphicsView(self.feature_tab)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(0, -10, 631, 461))
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(200, 198, 198);\n"
"background-color: rgb(200, 196, 135);")
        self.label_4 = QLabel(self.feature_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 581, 41))
        self.label_5 = QLabel(self.feature_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 130, 171, 21))
        self.pushButton = QPushButton(self.feature_tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 160, 111, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)
        self.pushButton.setAutoFillBackground(True)
        self.label_6 = QLabel(self.feature_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 130, 171, 21))
        self.pushButton_2 = QPushButton(self.feature_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 160, 111, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(8)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setAutoFillBackground(True)
        self.label_7 = QLabel(self.feature_tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 40, 581, 51))
        self.label_8 = QLabel(self.feature_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 220, 231, 31))
        self.pushButton_3 = QPushButton(self.feature_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 250, 111, 31))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setAutoFillBackground(True)
        self.textBrowser = QTextBrowser(self.feature_tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(140, 160, 91, 31))
        self.textBrowser_2 = QTextBrowser(self.feature_tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(450, 160, 91, 31))
        self.textBrowser_3 = QTextBrowser(self.feature_tab)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(140, 250, 91, 31))
        self.label_9 = QLabel(self.feature_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 130, 41, 41))
        self.label_10 = QLabel(self.feature_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 310, 411, 16))
        self.checkBox = QCheckBox(self.feature_tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(430, 310, 111, 16))
        self.label_11 = QLabel(self.feature_tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 330, 421, 16))
        self.checkBox_2 = QCheckBox(self.feature_tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(450, 330, 111, 16))
        self.pushButton_4 = QPushButton(self.feature_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(260, 360, 111, 31))
        font5 = QFont()
        font5.setFamily(u"Comic Sans MS")
        font5.setPointSize(14)
        font5.setItalic(True)
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setAutoFillBackground(True)
        icon1 = QIcon()
        icon1.addFile(u"red_dot.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"start_logo.png", QSize(), QIcon.Active, QIcon.On)
        self.tabWidget.addTab(self.feature_tab, icon1, "")
        self.feature_map_tab = QWidget()
        self.feature_map_tab.setObjectName(u"feature_map_tab")
        self.graphicsView_5 = QGraphicsView(self.feature_map_tab)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(0, 0, 631, 461))
        self.graphicsView_5.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(200, 198, 198);\n"
"background-color: rgb(200, 196, 135);")
        self.label_25 = QLabel(self.feature_map_tab)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 50, 581, 41))
        icon2 = QIcon()
        icon2.addFile(u"red_dot.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"start_logo.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u"red_dot.png", QSize(), QIcon.Selected, QIcon.Off)
        self.tabWidget.addTab(self.feature_map_tab, icon2, "")
        self.segmentation_tab = QWidget()
        self.segmentation_tab.setObjectName(u"segmentation_tab")
        self.graphicsView_3 = QGraphicsView(self.segmentation_tab)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(-5, -10, 631, 461))
        self.graphicsView_3.setStyleSheet(u"background-color: rgb(200, 196, 135);")
        self.label_12 = QLabel(self.segmentation_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 581, 41))
        self.label_13 = QLabel(self.segmentation_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 40, 581, 51))
        self.label_14 = QLabel(self.segmentation_tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 130, 281, 21))
        self.pushButton_5 = QPushButton(self.segmentation_tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 160, 111, 31))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setAutoFillBackground(True)
        self.textBrowser_4 = QTextBrowser(self.segmentation_tab)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(150, 160, 91, 31))
        self.label_15 = QLabel(self.segmentation_tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 220, 321, 31))
        self.pushButton_6 = QPushButton(self.segmentation_tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 260, 111, 31))
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setAutoFillBackground(True)
        self.textBrowser_5 = QTextBrowser(self.segmentation_tab)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(150, 260, 91, 31))
        self.pushButton_7 = QPushButton(self.segmentation_tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(260, 330, 121, 41))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setAutoFillBackground(True)
        self.label_27 = QLabel(self.segmentation_tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 60, 581, 51))
        icon3 = QIcon()
        icon3.addFile(u"red_dot.png", QSize(), QIcon.Selected, QIcon.Off)
        icon3.addFile(u"start_logo.png", QSize(), QIcon.Selected, QIcon.On)
        self.tabWidget.addTab(self.segmentation_tab, icon3, "")
        self.more_tab = QWidget()
        self.more_tab.setObjectName(u"more_tab")
        self.graphicsView_6 = QGraphicsView(self.more_tab)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setGeometry(QRect(0, 0, 631, 461))
        self.graphicsView_6.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(200, 198, 198);\n"
"background-color: rgb(200, 196, 135);")
        self.label_26 = QLabel(self.more_tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 50, 581, 41))
        self.tabWidget.addTab(self.more_tab, icon3, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.graphicsView_4 = QGraphicsView(self.about)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(0, -10, 631, 461))
        self.graphicsView_4.setStyleSheet(u"background-color: rgb(200, 196, 135);")
        self.label_16 = QLabel(self.about)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 20, 581, 41))
        self.label_17 = QLabel(self.about)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(460, 70, 151, 141))
        self.label_18 = QLabel(self.about)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 110, 581, 41))
        self.label_19 = QLabel(self.about)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 150, 581, 21))
        self.label_20 = QLabel(self.about)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 170, 581, 21))
        self.label_21 = QLabel(self.about)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 200, 581, 21))
        self.label_22 = QLabel(self.about)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 250, 581, 41))
        self.label_23 = QLabel(self.about)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 290, 581, 21))
        self.label_24 = QLabel(self.about)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 310, 581, 21))
        self.tabWidget.addTab(self.about, icon3, "")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(IDMS)

        self.stackedWidget.setCurrentIndex(0)
        self.startButton.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(IDMS)

    def retranslateUi(self, IDMS):
        IDMS.setWindowTitle(QCoreApplication.translate("IDMS", u"IDMS", None))
        self.label.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Image</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Data Management </span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Software</span></p></body></html>", None))
        self.startButton.setToolTip(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Start</span></p></body></html>", None))
        self.startButton.setText(QCoreApplication.translate("IDMS", u"Start", None))
        self.label_4.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; color:#00006d;\">Create csv file of pixel values of Image</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#ffffff;\">Single Image - </span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("IDMS", u"Browse Image", None))
        self.label_6.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#ffffff;\">Image Directory -</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("IDMS", u"Browse folder", None))
        self.label_7.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:400; color:#ffffff;\">Use this Software to extract pixel data from images and save it in csv file. Just select the image and your work is done.</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Path for saving csv file -</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("IDMS", u"Browse Folder", None))
        self.textBrowser.setHtml(QCoreApplication.translate("IDMS", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial Black'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">OR</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-weight:400; color:#ffffff;\">Resize images to 28X28 before extracting pixel values?</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("IDMS", u"Yes", None))
        self.label_11.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" color:#ffffff;\">Do you want to apply PCA and reduce the no. of features?</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("IDMS", u"Yes", None))
        self.pushButton_4.setText(QCoreApplication.translate("IDMS", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.feature_tab), QCoreApplication.translate("IDMS", u"Feature Extraction", None))
        self.label_25.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; color:#00006d;\">Will be implemented soon....</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.feature_map_tab), QCoreApplication.translate("IDMS", u"Feature Maps", None))
        self.label_12.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; color:#00006d;\">Segment Images using Otsu's Method</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:400; color:#ffffff;\">Use this Software to segment images using Otsu's Method. Make sure your Image must be </span><span style=\" font-weight:400; color:#ffffff;\">Grayscale</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">Note That If your ins't Grayscale, This software will convert your image into grayscale first.</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#ffffff;\">Select your Image (Grayscale) - </span></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("IDMS", u"Browse Image", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("IDMS", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial Black'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Path for saving segmented image -</span></p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("IDMS", u"Browse Folder", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("IDMS", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial Black'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("IDMS", u"Segment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.segmentation_tab), QCoreApplication.translate("IDMS", u"Segmentation", None))
        self.label_26.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; color:#00006d;\">Will be implemented soon....</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.more_tab), QCoreApplication.translate("IDMS", u"More..", None))
        self.label_16.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:24pt; text-decoration: underline; color:#00006d;\">About                     </span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><img src=\"abhi.png\"/></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:18pt; color:#00006d;\">Abhishek Kumar</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:400; color:#ffffff;\">Engineering Student, Research Scholar</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:400; color:#ffffff;\">Android Developer, Open Source Developer</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#ffffff;\">Gaya College of Engineering, Gaya</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:16pt; color:#00006d;\">Contact -</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; color:#ffffff;\">Email - Abhisheksingh73017@gmail.com</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("IDMS", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; color:#ffffff;\">Mobile - +919128451514</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("IDMS", u"About", None))

