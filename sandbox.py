#!/usr/bin/python
import subprocess
import sys
import PyQt4.QtGui as qtgui
import pickle

class MainWindow(qtgui.QScrollArea):
	layout_main_vert = None
	submit = None

	def __init__(self):
		super(MainWindow, self).__init__()
		self.setWidgetResizable(True)
		self.setGeometry(300,300,250,150)
		self.setWindowTitle("Dis Window Title")

		self.layout_main_vert = qtgui.QVBoxLayout()
		self.submit = qtgui.QPushButton("Submit!")
		self.layout_main_vert.addWidget(self.submit)

		for btn in range(1,20):
			btn = qtgui.QPushButton("Nananana")
			self.layout_main_vert.addWidget(btn)

		self.setLayout(self.layout_main_vert)
		self.show()

a = qtgui.QApplication(sys.argv)
window = MainWindow()

sys.exit(a.exec_())
