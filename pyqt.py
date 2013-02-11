#!/usr/bin/python
import subprocess
import sys
import PyQt4.QtGui as qtgui
import xml.etree.cElementTree as et
import pickle

class Scroll(qtgui.QScrollArea):
	main_window = None	
	anime_list = {}

	def __init__(self):
		super(Scroll, self).__init__()
		self.setWidgetResizable(True)
		self.main_window = MainWidget()
		self.anime_list = {} 

	def createWindow(self):
		tree = et.parse('sample2.xml')
		root = tree.getroot()
		self.parse_root(root)

		self.main_window.addAnimeList(self.anime_list)
		self.setWidget(self.main_window)
		self.show()

	def parse_root(self, xml_tree):
		for child in xml_tree:
			if(child.tag=='anime'):
				anime_series = self.parse_anime_entry(child)
				self.anime_list[anime_series['series_animedb_id']] = \
					anime_series

	def parse_anime_entry(self, anime_entry):
		result = {}
		for tag in anime_entry:
			result[tag.tag] = tag.text
		return result


class MainWidget(qtgui.QWidget):
	counter=0;
	layout_main_vert = None
	label_lineedit= []
	submit = None

#Initialize object variables. Has to be done in __init__ otherwise static vars
	def __init__(self):
		super(MainWidget, self).__init__()
		self.counter = 0
		self.label_lineedit= []

		self.setGeometry(300,300,250,150)
		self.setWindowTitle("MyAnimeList Updater")

		self.layout_main_vert = qtgui.QVBoxLayout()
		self.submit = qtgui.QPushButton("Update list on MAL")

		self.initSignalSlots()
		self.initLayout()	

#Setup QT signals and slots
	def initSignalSlots(self):
		self.submit.clicked.connect(self.debug)
		
#Setup window layout. Main layout is vertical, with nested horizontals
	def initLayout(self):
		self.layout_main_vert.addWidget(self.submit)
		self.setLayout(self.layout_main_vert)

#Add a line, which consists of a QLabel and a QLineEdit
	def addLine(self, label_text, lineedit_text):
		temp_layout_hz = qtgui.QHBoxLayout()
		temp_label = qtgui.QLabel(label_text)
		temp_lineedit = qtgui.QLineEdit(lineedit_text)
		temp_layout_hz.addWidget(temp_label)
		temp_layout_hz.addWidget(temp_lineedit)
	
		self.layout_main_vert.addLayout(temp_layout_hz)

	def addAnimeList(self, anime_list):
		for (series_id, series) in anime_list.items():
			for (tag,value) in series.items():
				print("ID:", series_id, "TAG:", tag, "VALUE:", value)
			self.addLine(series['series_title'],series['my_score'])

	def debug(self):
		self.addLine("Hello", "World!")
		print("FLAGGED!")

a = qtgui.QApplication(sys.argv)
scroller = Scroll()
scroller.createWindow()
sys.exit(a.exec_())
