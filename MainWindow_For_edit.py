# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSDS_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import json
import os
import threading

import requests as rq
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

SIRI_content = {}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.cwd = os.getcwd()
        MainWindow.setObjectName("MSDS_DataBase")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1278, 912)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/if evangelion Win/Icons/3rd Angel SASCHIEL.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1547, 985)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/if evangelion Win/Icons/3rd Angel SASCHIEL.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CASInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CASInput.setObjectName("CASInput")
        self.horizontalLayout.addWidget(self.CASInput)
        self.CASButton = QtWidgets.QPushButton(self.centralwidget)
        self.CASButton.setEnabled(False)
        self.CASButton.setCheckable(False)
        self.CASButton.setDefault(False)
        self.CASButton.setFlat(False)
        self.CASButton.setObjectName("CASButton")
        self.horizontalLayout.addWidget(self.CASButton)
        self.DataBase_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.DataBase_Name.setEnabled(False)
        self.DataBase_Name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DataBase_Name.setInputMask("")
        self.DataBase_Name.setText("")
        self.DataBase_Name.setObjectName("DataBase_Name")
        self.horizontalLayout.addWidget(self.DataBase_Name)
        self.Database_select = QtWidgets.QPushButton(self.centralwidget)
        self.Database_select.setObjectName("Database_select")
        self.horizontalLayout.addWidget(self.Database_select)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ECnumLabel = QtWidgets.QPushButton(self.centralwidget)
        self.ECnumLabel.setEnabled(False)
        self.ECnumLabel.setObjectName("ECnumLabel")
        self.horizontalLayout_2.addWidget(self.ECnumLabel)
        self.ECnum = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ECnum.sizePolicy().hasHeightForWidth())
        self.ECnum.setSizePolicy(sizePolicy)
        self.ECnum.setMaximumSize(QtCore.QSize(16777215, 20))
        self.ECnum.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ECnum.setObjectName("ECnum")
        self.horizontalLayout_2.addWidget(self.ECnum)
        self.InBookLabel = QtWidgets.QPushButton(self.centralwidget)
        self.InBookLabel.setEnabled(False)
        self.InBookLabel.setObjectName("InBookLabel")
        self.horizontalLayout_2.addWidget(self.InBookLabel)
        self.InBook = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InBook.sizePolicy().hasHeightForWidth())
        self.InBook.setSizePolicy(sizePolicy)
        self.InBook.setMaximumSize(QtCore.QSize(16777215, 20))
        self.InBook.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InBook.setObjectName("InBook")
        self.horizontalLayout_2.addWidget(self.InBook)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SearchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchInput.setObjectName("SearchInput")
        self.horizontalLayout_3.addWidget(self.SearchInput)
        self.SearchGo = QtWidgets.QPushButton(self.centralwidget)
        self.SearchGo.setObjectName("SearchGo")
        self.horizontalLayout_3.addWidget(self.SearchGo)
        self.SearchCount = QtWidgets.QLabel(self.centralwidget)
        self.SearchCount.setMinimumSize(QtCore.QSize(50, 0))
        self.SearchCount.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.SearchCount.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchCount.setObjectName("SearchCount")
        self.horizontalLayout_3.addWidget(self.SearchCount)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.Output_Win = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.Output_Win.setFont(font)
        self.Output_Win.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Output_Win.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Output_Win.setAutoFillBackground(False)
        self.Output_Win.setObjectName("Output_Win")
        self.MSDS = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MSDS.sizePolicy().hasHeightForWidth())
        self.MSDS.setSizePolicy(sizePolicy)
        self.MSDS.setObjectName("MSDS")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.MSDS)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.MSDS_Output = QtWidgets.QTextBrowser(self.MSDS)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.MSDS_Output.setFont(font)
        self.MSDS_Output.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>")
        self.MSDS_Output.setOverwriteMode(False)
        self.MSDS_Output.setObjectName("MSDS_Output")
        self.horizontalLayout_4.addWidget(self.MSDS_Output)
        self.Output_Win.addTab(self.MSDS, "")
        self.Arti = QtWidgets.QWidget()
        self.Arti.setObjectName("Arti")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Arti)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Arti_Ouput = QtWidgets.QTextBrowser(self.Arti)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.Arti_Ouput.setFont(font)
        self.Arti_Ouput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Arti_Ouput.setObjectName("Arti_Ouput")
        self.horizontalLayout_5.addWidget(self.Arti_Ouput)
        self.Output_Win.addTab(self.Arti, "")
        self.Toxic = QtWidgets.QWidget()
        self.Toxic.setObjectName("Toxic")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Toxic)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Toxic_Output = QtWidgets.QTextBrowser(self.Toxic)
        self.Toxic_Output.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.Toxic_Output.setObjectName("Toxic_Output")
        self.horizontalLayout_6.addWidget(self.Toxic_Output)
        self.Output_Win.addTab(self.Toxic, "")
        self.ECHA_Cla = QtWidgets.QWidget()
        self.ECHA_Cla.setObjectName("ECHA_Cla")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ECHA_Cla)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ECHA_Cla_Output = QtWidgets.QTextBrowser(self.ECHA_Cla)
        self.ECHA_Cla_Output.setObjectName("ECHA_Cla_Output")
        self.horizontalLayout_7.addWidget(self.ECHA_Cla_Output)
        self.Output_Win.addTab(self.ECHA_Cla, "")
        self.EHCA_Busi_Cla = QtWidgets.QWidget()
        self.EHCA_Busi_Cla.setObjectName("EHCA_Busi_Cla")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.EHCA_Busi_Cla)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.EHCA_Busi_Cla_Output = QtWidgets.QTextBrowser(self.EHCA_Busi_Cla)
        self.EHCA_Busi_Cla_Output.setObjectName("EHCA_Busi_Cla_Output")
        self.horizontalLayout_8.addWidget(self.EHCA_Busi_Cla_Output)
        self.Output_Win.addTab(self.EHCA_Busi_Cla, "")
        self.SIRI = QtWidgets.QWidget()
        self.SIRI.setObjectName("SIRI")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.SIRI)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.SIRI_Output = QtWidgets.QTextBrowser(self.SIRI)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.SIRI_Output.setFont(font)
        self.SIRI_Output.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>")
        self.SIRI_Output.setOverwriteMode(False)
        self.SIRI_Output.setObjectName("SIRI_Output")
        self.horizontalLayout_9.addWidget(self.SIRI_Output)
        self.Output_Win.addTab(self.SIRI, "")
        self.Alfa = QtWidgets.QWidget()
        self.Alfa.setObjectName("Alfa")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Alfa)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Alfa_url = QtWidgets.QLabel(self.Alfa)
        self.Alfa_url.setMinimumSize(QtCore.QSize(0, 20))
        self.Alfa_url.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.Alfa_url.setFont(font)
        self.Alfa_url.setObjectName("Alfa_url")
        self.verticalLayout.addWidget(self.Alfa_url)
        self.Alfa_browser = QtWebEngineWidgets.QWebEngineView(self.Alfa)
        self.Alfa_browser.setObjectName("Alfa_browser")
        self.verticalLayout.addWidget(self.Alfa_browser)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.Output_Win.addTab(self.Alfa, "")
        self.verticalLayout_6.addWidget(self.Output_Win)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1417, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.SearchButton = QtWidgets.QAction(MainWindow)
        self.SearchButton.setObjectName("SearchButton")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.Output_Win.setCurrentIndex(0)
        self.CASButton.clicked.connect(self.ComeOnGirl)
        self.Database_select.clicked.connect(self.InputData)  # 载入数据库文件
        self.Database_select.clicked.connect(self.AfterInputData)  # 更新数据库名称，解锁查询按钮
        self.MSDS_Output.textChanged.connect(self.reset_search_content)  # MSDS文本框内容变化重设被搜索内容
        self.Arti_Ouput.textChanged.connect(self.reset_search_content)  # Arti文本框内容变化重设被搜索内容
        self.Toxic_Output.textChanged.connect(self.reset_search_content)  # Toxic文本框内容变化重设被搜索内容
        self.ECHA_Cla_Output.textChanged.connect(self.reset_search_content) # CLP文本框内容变化重设被搜索内容
        self.EHCA_Busi_Cla_Output.textChanged.connect(self.reset_search_content)  # CLP_Business文本框内容变化重设被搜索内容
        self.SIRI_Output.textChanged.connect(self.reset_search_content)  # SIRI文本框内容变化重设被搜索内容
        self.Output_Win.currentChanged.connect(self.reset_search_content)  # 文本框切换重设被搜索内容
        self.SearchGo.clicked.connect(self.search)  # 检索并高亮显示
        self.Alfa_browser.urlChanged.connect(self.Alfa_refresh_url)  # Alfa每次进新网页，刷新一下url信息
        self.Alfa_browser.urlChanged.connect(self.Acors_pdf)  # Alfa每次进网页，看看是否到要出SDS的那个页面了
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 在线检索的相关预留参数
        self.Alfa_browser.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.Alfa_browser.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

        # 搜索相关项
        self.search_content = None
        self.search_key = None
        self.search_count = 0
        self.search_current = 0
        self.search_colored = None

        # 测试一下
        self.table = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CASButton.setText(_translate("MainWindow", "查  询"))
        self.DataBase_Name.setPlaceholderText(_translate("MainWindow", "查询前必须选择数据库"))
        self.Database_select.setText(_translate("MainWindow", "载入数据库"))
        self.ECnumLabel.setText(_translate("MainWindow", "EC Number"))
        self.InBookLabel.setText(_translate("MainWindow", "In Which Book"))
        self.SearchGo.setText(_translate("MainWindow", "在结果中搜索"))
        self.SearchCount.setText(_translate("MainWindow", "0/0"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.MSDS), _translate("MainWindow", "MSDS"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.Arti), _translate("MainWindow", "文献"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.Toxic), _translate("MainWindow", "毒性资料"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.ECHA_Cla), _translate("MainWindow", "ECHA分类"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.EHCA_Busi_Cla), _translate("MainWindow", "ECHA企业分类"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.SIRI), _translate("MainWindow", "SIRI"))
        self.Alfa_url.setText(_translate("MainWindow", "Alfa_Url"))
        self.Output_Win.setTabText(self.Output_Win.indexOf(self.Alfa), _translate("MainWindow", "Alfa"))
        self.menu.setTitle(_translate("MainWindow", "帮  助"))
        self.SearchButton.setText(_translate("MainWindow", "search"))

    def InputData(self):
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                          "选取文件", self.cwd,  # 起始路径
                                                                          "Excel Files (*.json)")  # 设置文件扩展名过滤,用双分号间隔
        if '.json' in fileName_choose:
            self.DataBook_Name = fileName_choose
            with open(self.DataBook_Name, 'r') as f:
                self.DataBook = json.load(f)
        # print(len(self.DataBook.keys()))
        else:
            return

    def AfterInputData(self):
        _translate = QtCore.QCoreApplication.translate
        self.CASButton.setEnabled(True)
        self.CASButton.setFocus()
        self.CASButton.setShortcut('enter')
        self.DataBase_Name.setPlaceholderText(_translate("MainWindow", self.DataBook_Name))

    def FindMyGirl(self, Book, Girl_Name):
        girl_pool = {}
        try:
            self.getAlfa(Girl_Name)
        except:
            self.Alfa_browser.setHtml('<p>臣妾没有找到相应的页面哦...T^T</p>')
        try:
            for mm in Book.keys():
                if Girl_Name == mm:
                    girl_pool[mm] = Book[mm]
        except:
            girl_pool = 999  # ‘臣妾好像发生了什么错误....’
        finally:
            return girl_pool

    def ShowMyGirl(self, girl_pool):
        if girl_pool == 999:
            self.MSDS_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.Arti_Ouput.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.Toxic_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.ECHA_Cla_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.EHCA_Busi_Cla_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.SIRI_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            return
        if not girl_pool:
            self.MSDS_Output.append('臣妾不认识这个物质呀....T^T')
            self.Arti_Ouput.append('臣妾不认识这个物质呀....T^T')
            self.Toxic_Output.append('臣妾不认识这个物质呀....T^T')
        #MSDS
        try:
            for girl in girl_pool.keys():
                self.MSDS_Output.append(girl)
                self.MSDS_Output.append('************臣妾查到了************')
                for info_MSDS in girl_pool[girl]['MSDS']:
                    info = ",    ".join(info_MSDS)
                    self.MSDS_Output.append(info)
                self.MSDS_Output.append('============下一个============')
        except:
            self.MSDS_Output.clear()
            self.MSDS_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
        #Arti
        try:
            for girl in girl_pool.keys():
                self.Arti_Ouput.append(girl)
                self.Arti_Ouput.append('************臣妾查到了************')
                for info_Arti in girl_pool[girl]['Arti']:
                    info = "    ".join(info_Arti)
                    self.Arti_Ouput.append(info)
                self.Arti_Ouput.append('============下一个============')
        except:
            self.Arti_Ouput.clear()
            self.Arti_Ouput.append('臣妾似乎发生了什么奇怪的错误....T^T')
        #Toxic
        try:
            for girl in girl_pool.keys():
                self.Toxic_Output.append(girl)
                self.Toxic_Output.append('************臣妾查到了************')
                print(girl_pool[girl]['Toxic'], 'Toxic is good')
                for info_Toxic in girl_pool[girl]['Toxic']:
                    info = "    ".join(info_Toxic)
                    self.Toxic_Output.append(info)
                self.Toxic_Output.append('============下一个============')
        except:
            self.Toxic_Output.clear()
            self.Toxic_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
        #ECHA_CLP
        self.ECHA_Cla_Output.toHtml()
        try:
            for girl in girl_pool.keys():
                self.ECHA_Cla_Output.append('<p>' + girl + '</p>')
                self.ECHA_Cla_Output.append('<p>************臣妾查到了************</p>')
                self.ECHA_Cla_Output.append(girl_pool[girl]['CLP'])
                self.ECHA_Cla_Output.append('<p>============下一个============</p>')
        except:
            self.ECHA_Cla_Output.clear()
            self.ECHA_Cla_Output.append('<p>臣妾似乎发生了什么奇怪的错误....T^T</p>')
        #ECHA_CLP_Business
        self.EHCA_Busi_Cla_Output.toHtml()
        try:
            for girl in girl_pool.keys():
                self.EHCA_Busi_Cla_Output.append('<p>' + girl + '</p>')
                self.EHCA_Busi_Cla_Output.append('<p>************臣妾查到了************</p>')
                self.EHCA_Busi_Cla_Output.append(girl_pool[girl]['CLP_Business'])
                self.EHCA_Busi_Cla_Output.append('<p>============下一个============</p>')
        except:
            self.EHCA_Busi_Cla_Output.clear()
            self.EHCA_Busi_Cla_Output.append('<p>臣妾似乎发生了什么奇怪的错误....T^T</p>')
        #SIRI
        try:
            self.getSIRI_multi(girl_pool)
        except:
            self.SIRI_Output.clear()
            self.SIRI_Output.append('<p>臣妾似乎发生了什么奇怪的错误....T^T</p>')
        #EC_num
        try:
            for girl in girl_pool.keys():
                self.ECnum.append(girl_pool[girl]['EC_num'])
        except:
            self.ECnum.clear()
            self.ECnum.append('<p>臣妾似乎发生了什么奇怪的错误....T^T</p>')
        pass

    def ComeOnGirl(self):
        self.MSDS_Output.clear()
        self.Arti_Ouput.clear()
        self.Toxic_Output.clear()
        self.ECHA_Cla_Output.clear()
        self.EHCA_Busi_Cla_Output.clear()
        self.SIRI_Output.clear()
        Girl_Name = self.CASInput.text()
        try:
            if Girl_Name:
                girl_pool = self.FindMyGirl(self.DataBook, Girl_Name)
                self.ShowMyGirl(girl_pool)
            else:
                self.MSDS_Output.clear()
                self.Arti_Ouput.clear()
                self.Toxic_Output.clear()
                self.MSDS_Output.append('想要臣妾查什么？')
                self.Arti_Ouput.append('想要臣妾查什么？')
                self.Toxic_Output.append('想要臣妾查什么？')
        except:
            self.MSDS_Output.clear()
            self.Arti_Ouput.clear()
            self.Toxic_Output.clear()
            self.MSDS_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.Arti_Ouput.append('臣妾似乎发生了什么奇怪的错误....T^T')
            self.Toxic_Output.append('臣妾似乎发生了什么奇怪的错误....T^T')

    # 从这里开始，是【检索】功能组件，增加tab千万不要忘记更新这里的所有内容
    # 不然会被自己蠢哭的.......
    def select(self, start, length):
        """选中文字,高亮显示"""
        if self.Output_Win.currentIndex() == 0:
            cur = self.MSDS_Output.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.MSDS_Output.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 1:
            cur = self.Arti_Ouput.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.Arti_Ouput.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 2:
            cur = self.Toxic_Output.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.Toxic_Output.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 3:
            cur = self.ECHA_Cla_Output.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.ECHA_Cla_Output.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 4:
            cur = self.EHCA_Busi_Cla_Output.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.EHCA_Busi_Cla_Output.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 5:
            cur = self.SIRI_Output.textCursor()
            cur.setPosition(start)
            cur.setPosition(start + length, QtGui.QTextCursor.KeepAnchor)
            self.SIRI_Output.setTextCursor(cur)
        elif self.Output_Win.currentIndex() == 6:
            pass
    def reset_search_content(self):
        """改变待搜索内容"""
        self.search_content = None
        self.search_count = 0
        self.search_current = 0
    def search(self):
        """搜索"""
        key_word = self.SearchInput.text()
        if key_word != self.search_key:
            self.search_key = key_word
            self.search_count = 0
            self.search_current = 0
        if not self.search_content:
            if self.Output_Win.currentIndex() == 0:
                self.search_content = self.MSDS_Output.toPlainText()
            elif self.Output_Win.currentIndex() == 1:
                self.search_content = self.Arti_Ouput.toPlainText()
            elif self.Output_Win.currentIndex() == 2:
                self.search_content = self.Toxic_Output.toPlainText()
            elif self.Output_Win.currentIndex() == 3:
                self.search_content = self.ECHA_Cla_Output.toPlainText()
            elif self.Output_Win.currentIndex() == 4:
                self.search_content = self.EHCA_Busi_Cla_Output.toPlainText()
            elif self.Output_Win.currentIndex() == 5:
                self.search_content = self.SIRI_Output.toPlainText()
            elif self.Output_Win.currentIndex() == 6:
                return
        if not self.search_count:
            self.search_count = self.search_content.count(key_word)
            if self.search_count != 0:
                start = self.search_content.index(key_word)
                self.select(start, len(key_word))
                self.search_current += 1
        else:
            if self.search_current < self.search_count:
                if self.Output_Win.currentIndex() == 0:
                    start = self.search_content.find(key_word, self.MSDS_Output.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 1:
                    start = self.search_content.find(key_word, self.Arti_Ouput.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 2:
                    start = self.search_content.find(key_word, self.Toxic_Output.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 3:
                    start = self.search_content.find(key_word, self.ECHA_Cla_Output.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 4:
                    start = self.search_content.find(key_word, self.EHCA_Busi_Cla_Output.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 5:
                    start = self.search_content.find(key_word, self.SIRI_Output.textCursor().position())
                    if start != -1:
                        self.select(start, len(key_word))
                        self.search_current += 1
                elif self.Output_Win.currentIndex() == 6:
                    pass
            else:
                self.search_count = 0
                self.search_current = 0
                self.search()
        if self.Output_Win.currentIndex() == 0:
            self.MSDS_Output.setFocus()
        elif self.Output_Win.currentIndex() == 1:
            self.Arti_Ouput.setFocus()
        elif self.Output_Win.currentIndex() == 2:
            self.Toxic_Output.setFocus()
        elif self.Output_Win.currentIndex() == 3:
            self.ECHA_Cla_Output.setFocus()
        elif self.Output_Win.currentIndex() == 4:
            self.EHCA_Busi_Cla_Output.setFocus()
        elif self.Output_Win.currentIndex() == 5:
            self.SIRI_Output.setFocus()
        elif self.Output_Win.currentIndex() == 6:
            pass
        self.SearchCount.setText("{}/{}".format(self.search_current, self.search_count))
    # 【检索】组件到这里结束
    # 这组是SIRI网站的在线查询功能，用了QThread多线程，神烦，发现pyqtSignal没有emit、connect方法，找了很多资料，可能是pyQt5本体不完整
    def getSIRI_multi(self, girls):
        global SIRI_content
        SIRI_content = {}
        self.SIRI_Output.append('臣妾正在努力查找中......')
        self.getSIRI = getSIRI(girls)
        # thread = threading.Thread(target=self.getSIRI_online, args=(girl, girls[girl]))
        self.getSIRI.start()
        self.getSIRI.finished.connect(self.SIRI_refresh)
        pass
    def SIRI_refresh(self):
        self.SIRI_Output.clear()
        global SIRI_content
        for cas in SIRI_content.keys():
            self.SIRI_Output.append(cas)
            self.SIRI_Output.append('************臣妾查到了************')
            self.SIRI_Output.append(SIRI_content[cas])
            self.SIRI_Output.append('============下一个============')
    '''Alfa Model'''
    # 这组是Alfa的在线查询功能，使用了严格检索，使用了WebEngine
    # 思路是在线进入查询页面，然后让玩家自己选择货号，最后通过截取货号的MSDS文件链接，直接展示PDF
    # 同时，为了方便记录页面，在Alfa_url的label上，实时显示网页地址
    def Alfa_refresh_url(self):
        url = self.Alfa_browser.url().toString()
        self.Alfa_url.setText(url)
    def getAlfa(self, girl):
        url = 'https://www.alfa.com/zh-cn/search/?q=%s' % girl
        self.Alfa_browser.load(QtCore.QUrl(url))
        self.Alfa_refresh_url()
    def Acors_pdf(self):
        url = self.Alfa_browser.url().toString()
        if r'https://www.alfa.com/zh-cn/catalog/sds/' in url:
            sku = url[-7:-1]
            if sku[0] == '0':
                sku = sku[1:]
            print('SKU = ', sku)
            pdf_url = 'https://www.alfa.com/zh-cn/msds/?language=CN&subformat=CGV4&sku=%s' % sku
            print('pdf_url = ', pdf_url)
            self.Alfa_browser.load(QtCore.QUrl(pdf_url))
            self.Alfa_refresh_url()
    '''finished at 0219'''

class getSIRI(QtCore.QThread):
    cas = 999
    url = 999
    def __init__(self, girls, parent=None):
        super(getSIRI, self).__init__(parent)
        self.girls = girls
    def run(self):
        for girl in self.girls.keys():
            url = self.girls[girl]['SIRI_url']
            cas, content = self.getSIRI_online(girl, url)
            global SIRI_content
            SIRI_content[cas] = content
        print('Global SIRI ready!!!')
        print(SIRI_content)
    def getSIRI_online(self, cas, url):
        if url == 999:
            content = '<p>臣妾没有在SIRI网站内找到信息呢...嘤嘤嘤...</p>'
            return cas, content
        else:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/88.0.4324.146 Safari/537.36'}
                web = rq.get(url=url, headers=headers, timeout=60)
                content = web.text
            except:
                content = '<p>臣妾没有在SIRI网站内找到信息呢...嘤嘤嘤...</p>'
            finally:
                return cas, content
