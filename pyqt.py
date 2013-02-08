#!/usr/bin/python
import subprocess
import sys
import PyQt4.QtGui as qtgui
import pickle


class MainWindow(qtgui.QWidget):
	counter=0;
	layout_main_vert = None
	label_lineedit= []
	submit = None

#Initialize object variables. Has to be done in __init__ otherwise static vars
	def __init__(self):
		super(MainWindow, self).__init__()
		self.counter = 0
		self.label_lineedit= []

		self.setGeometry(300,300,250,150)
		self.setWindowTitle("Dis Window Title")

		self.layout_main_vert = qtgui.QVBoxLayout()
		self.submit = qtgui.QPushButton("Submit!")

		self.initSignalSlots()
		self.initLayout()	

#Setup QT signals and slots
	def initSignalSlots(self):
		self.submit.clicked.connect(self.debug)
		
#Setup window layout. Main layout is vertical, with nested horizontals
	def initLayout(self):
		self.layout_main_vert.addWidget(self.submit)
		self.setLayout(self.layout_main_vert)
		self.show()

#Add a line, which consists of a QLabel and a QLineEdit
	def addLine(self, label_text, lineedit_text):
		if(self.counter == 100):
			return 0
		temp_layout_hz = qtgui.QHBoxLayout()
		temp_label = qtgui.QLabel(label_text)
		temp_lineedit = qtgui.QLineEdit(lineedit_text)
		temp_layout_hz.addWidget(temp_label)
		temp_layout_hz.addWidget(temp_lineedit)
	
		self.layout_main_vert.addLayout(temp_layout_hz)
		self.counter = self.counter + 1

	def addAnimeList(self, anime_list):
		for (series_id, series) in anime_list.items():
			for (tag,value) in series.items():
				print("ID:", series_id, "TAG:", tag, "VALUE:", value)
			self.addLine(series['series_title'],series['my_score'])

	def debug(self):
		self.addLine("Hello", "World!")
		print("FLAGGED!")

#Get the parsed xml result from xmlparse2.py
subprocess.Popen(["./xmlparse2.py"], 
					stdout=subprocess.PIPE, 
					stderr=subprocess.PIPE).communicate()
xml_file = open("xml-file.pickle", "rb")
anime_list = pickle.load(xml_file)
	
a = qtgui.QApplication(sys.argv)
window = MainWindow()
window.addAnimeList(anime_list)

sys.exit(a.exec_())
