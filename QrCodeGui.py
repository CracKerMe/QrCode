# -*- coding: utf-8 -*-
from sys import argv, exit
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QDoubleSpinBox, QFrame, QLabel, QLineEdit, QPushButton, QSpinBox, QPlainTextEdit, QToolButton, QWidget, QFileDialog, QMessageBox
from re import compile
from os import getcwd
from os.path import isdir
from MyQR.myqr import run
from webbrowser import open_new

class Ui_MainForm(object):
    def __init__(self):
        self.cwd = getcwd()

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(808, 768)
        MainForm.setLayoutDirection(Qt.RightToLeft)

        K12 = QFont()
        K12.setFamily("楷体")
        K12.setPointSize(12)

        JBI9 = QFont()
        JBI9.setFamily("JetBrains Mono")
        JBI9.setPointSize(9)
        JBI9.setBold(True)
        JBI9.setItalic(True)
        JBI9.setWeight(75)

        JBI12 = QFont()
        JBI12.setFamily("JetBrains Mono")
        JBI12.setPointSize(12)
        JBI12.setBold(True)
        JBI12.setItalic(True)
        JBI12.setWeight(75)

        JBI16 = QFont()
        JBI16.setFamily("JetBrains Mono")
        JBI16.setPointSize(16)
        JBI16.setBold(True)
        JBI16.setItalic(True)
        JBI16.setWeight(75)

        self.wordsValue = QPlainTextEdit(MainForm)
        self.wordsValue.setGeometry(QRect(250, 80, 512, 384))
        self.wordsValue.setFont(JBI16)
        self.wordsValue.setPlaceholderText("")
        self.wordsValue.setObjectName("wordsValue")

        self.wordsKey = QLabel(MainForm)
        self.wordsKey.setGeometry(QRect(465, 40, 80, 20))
        self.wordsKey.setFont(K12)
        self.wordsKey.setObjectName("wordsKey")

        self.versionValue = QSpinBox(MainForm)
        self.versionValue.setGeometry(QRect(110, 130, 60, 20))
        self.versionValue.setFont(JBI9)
        self.versionValue.setMinimum(1)
        self.versionValue.setMaximum(40)
        self.versionValue.setSingleStep(1)
        self.versionValue.setProperty("value", 20)
        self.versionValue.setObjectName("versionValue")
        self.versionKey = QLabel(MainForm)
        self.versionKey.setGeometry(QRect(30, 130, 80, 20))
        self.versionKey.setFont(K12)
        self.versionKey.setObjectName("versionKey")

        self.pictureValue = QLineEdit(MainForm)
        self.pictureValue.setGeometry(QRect(250, 520, 450, 40))
        self.pictureValue.setFont(JBI12)
        self.pictureValue.setObjectName("pictureValue")
        self.pictureValue.setPlaceholderText("选填, 如果为空则生成普通二维码")
        self.pictureKey = QLabel(MainForm)
        self.pictureKey.setGeometry(QRect(465, 490, 80, 20))
        self.pictureKey.setFont(K12)
        self.pictureKey.setObjectName("pictureKey")
        self.pictureTool = QToolButton(MainForm)
        self.pictureTool.setGeometry(QRect(710, 520, 50, 40))
        self.pictureTool.setObjectName("pictureTool")
        self.pictureTool.clicked.connect(self.GetFilePath)

        self.colorizedValue = QCheckBox(MainForm)
        self.colorizedValue.setGeometry(QRect(30, 280, 85, 20))
        self.colorizedValue.setFont(K12)
        self.colorizedValue.setChecked(True)
        self.colorizedValue.setTristate(False)
        self.colorizedValue.setObjectName("colorizedValue")

        self.brightnessValue = QDoubleSpinBox(MainForm)
        self.brightnessValue.setGeometry(QRect(110, 180, 60, 20))
        self.brightnessValue.setFont(JBI9)
        self.brightnessValue.setSingleStep(0.1)
        self.brightnessValue.setProperty("value", 1.0)
        self.brightnessValue.setObjectName("brightnessValue")

        self.contrastValue = QDoubleSpinBox(MainForm)
        self.contrastValue.setGeometry(QRect(110, 230, 60, 20))
        self.contrastValue.setFont(JBI9)
        self.contrastValue.setSingleStep(0.1)
        self.contrastValue.setProperty("value", 1.0)
        self.contrastValue.setObjectName("contrastValue")
        self.contrastKey = QLabel(MainForm)
        self.contrastKey.setGeometry(QRect(30, 230, 80, 20))
        self.contrastKey.setFont(K12)
        self.contrastKey.setObjectName("contrastKey")

        self.brightnessKey = QLabel(MainForm)
        self.brightnessKey.setGeometry(QRect(30, 180, 80, 20))
        self.brightnessKey.setFont(K12)
        self.brightnessKey.setObjectName("brightnessKey")

        self.saveKey = QLabel(MainForm)
        self.saveKey.setGeometry(QRect(465, 590, 80, 20))
        self.saveKey.setFont(K12)
        self.saveKey.setObjectName("saveKey")
        self.saveValue = QLineEdit(MainForm)
        self.saveValue.setGeometry(QRect(250, 630, 450, 40))
        self.saveValue.setFont(JBI12)
        self.saveValue.setObjectName("saveValue")
        self.saveValue.setPlaceholderText("选填, 如果为空则在程序所在目录下生成")
        self.saveTool = QToolButton(MainForm)
        self.saveTool.setGeometry(QRect(710, 630, 50, 40))
        self.saveTool.setObjectName("saveTool")
        self.saveTool.clicked.connect(self.GetSavePath)

        self.startButton = QPushButton(MainForm)
        self.startButton.setGeometry(QRect(30, 350, 150, 50))
        self.startButton.setFont(K12)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.Run)

        self.line = QFrame(MainForm)
        self.line.setGeometry(QRect(212, 10, 2, 750))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(MainForm)
        self.line_2.setGeometry(QRect(20, 460, 180, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.homepageButton = QPushButton(MainForm)
        self.homepageButton.setGeometry(QRect(35, 550, 150, 50))
        self.homepageButton.setFont(K12)
        self.homepageButton.setObjectName("homepageButton")
        self.homepageButton.clicked.connect(self.GoItem)

        self.versionValue_ = QLabel(MainForm)
        self.versionValue_.setGeometry(QRect(40, 670, 141, 40))
        self.versionValue_.setFont(JBI12)
        self.versionValue_.setObjectName("versionValue_")

        self.levelValue = QComboBox(MainForm)
        self.levelValue.setGeometry(QRect(110, 80, 60, 20))
        self.levelValue.setFont(JBI12)
        self.levelValue.setObjectName("levelValue")
        self.levelValue.addItem("")
        self.levelValue.addItem("")
        self.levelValue.addItem("")
        self.levelValue.addItem("")
        self.levelValue.setCurrentIndex(3)
        self.levelKey = QLabel(MainForm)
        self.levelKey.setGeometry(QRect(30, 80, 80, 20))
        self.levelKey.setFont(K12)
        self.levelKey.setObjectName("levelKey")

        self.retranslateUi(MainForm)
        QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "QrCode"))
        self.wordsKey.setText(_translate("MainForm", "文本输入"))
        self.versionKey.setText(_translate("MainForm", "边长:"))
        self.pictureKey.setText(_translate("MainForm", "图片路径"))
        self.pictureTool.setText(_translate("MainForm", "..."))
        self.colorizedValue.setText(_translate("MainForm", "使用彩色"))
        self.contrastKey.setText(_translate("MainForm", "对比度:"))
        self.brightnessKey.setText(_translate("MainForm", "亮度:"))
        self.saveKey.setText(_translate("MainForm", "存储路径"))
        self.saveTool.setText(_translate("MainForm", "..."))
        self.startButton.setText(_translate("MainForm", "开始生成"))
        self.homepageButton.setText(_translate("MainForm", "访问开源项目"))
        self.versionValue_.setText(_translate("MainForm", "version: 0.2.1"))
        self.levelValue.setItemText(0, _translate("MainForm", "L"))
        self.levelValue.setItemText(1, _translate("MainForm", "M"))
        self.levelValue.setItemText(2, _translate("MainForm", "Q"))
        self.levelValue.setItemText(3, _translate("MainForm", "H"))
        self.levelKey.setText(_translate("MainForm", "纠错等级:"))

    def TextValidator(self):
        inText = self.wordsValue.toPlainText()
        exText = compile(r"^[0-9A-Za-z ··,.:;\+\-\*/\~!@#\$%\^&`'=<>\[\]\(\)\?_\{\}\|]+$")
        res = exText.match(inText)
        if res != None:
            return inText
        else:
            return False

    def GetFilePath(self):
        self.filePath = QFileDialog.getOpenFileName(
            self.widget,
            "选择背景图片",
            self.cwd,
            "JPG Image(*.jpg);;PNG Image(*.png);;BMP Image(*.bmp);;GIF Image(*.gif)"
            )
        self.pictureValue.setText(self.filePath[0])

    def GetSavePath(self):
        self.savePath = QFileDialog.getSaveFileName(
            self.widget,
            "选择背景图片",
            self.cwd,
            "JPG Image(*.jpg);;PNG Image(*.png);;BMP Image(*.bmp);;GIF Image(*.gif)"
                )
        self.saveValue.setText(self.savePath[0])

    def GoItem(self):
        open_new("https://github.com/Pu-gayhub/QrCode")

    def Run(self):
        textRes = self.TextValidator()
        if textRes != False:
            try:
                words = textRes
                version = self.versionValue.value()
                level = self.levelValue.currentText()
                picture = self.pictureValue.text()
                colorized = self.colorizedValue.isChecked()
                contrast = self.contrastValue.value()
                brightness = self.brightnessValue.value()
                save_name = self.saveValue.text()
                run(
                    words=words,
                    version=version,
                    level=level,
                    picture=picture,
                    colorized=colorized,
                    contrast=contrast,
                    brightness=brightness,
                    save_name=save_name
                )
            except OSError:
                QMessageBox.critical(self.widget, "失败", "无法将RGBA写入JPG图像,请尝试其他格式")
            except:
                QMessageBox.critical(self.widget, "失败", "出现错误")
            else:
                QMessageBox.information(self.widget, "成功!", "成功生成二维码")
        else:
            QMessageBox.critical(self.widget, "值错误", "文本为空或不支持所输入字符")

    def ShowWindow(self):
        app = QApplication(argv)
        self.widget = QWidget()
        mainForm = self.setupUi(self.widget)
        self.widget.show()
        exit(app.exec_())


if __name__ == "__main__":
    Ui_MainForm().ShowWindow()
