#!/usr/bin/python
import subprocess
import sys
import PyQt4.QtGui as qtgui
import pickle
import pycurl

class series_data:
	
	def __init__(self):
		

def generateXML(xml_data_hash):
	xmlstring='data=<?xml version="1.0" encoding="UTF-8"?>\n'
	"	<entry>\n"
	"		<episode>",xml_data_hash['episode'],"</episode>\n"
	"		<status>",xml_data_hash['status'],"</status>\n"
	"		<score>",xml_data_hash['score'],"</score>\n"
	"		<downloaded_episodes>",
	xml_data_hash['downloaded_episodes'],
	"</downloaded_episodes>\n"
	"		<storage_type>",xml_data_hash['storage_type'],"</storage_type>\n"
	"		<storage_value>",xml_data_hash['storage_value'],"</storage_value>\n"
	"		<times_rewatched>",
	xml_data_hash['times_rewatched'],
	"</times_rewatched>\n"
	"		<rewatch_value>",xml_data_hash['rewatch_value'],"</rewatch_value>\n"
	"		<date_start>",xml_data_hash['date_start'],"</date_start>\n"
	"		<date_finish>",xml_data_hash['date_finish'],"</date_finish>\n"
	"		<priority>",xml_data_hash['priority'],"</priority>\n"
	"		<enable_discussion>",
	xml_data_hash['enable_discussion'],
	"</enable_discussion>\n"
	"		<enable_rewatching>",
	xml_data_hash['enable_rewatching'],
	"</enable_rewatching>\n"
	"		<comments>",xml_data_hash['comments'],"</comments>\n"
	"		<fansub_group>",xml_data_hash['fansub_group'],"</fansub_group>\n"
	"		<tags>",xml_data_hash['tags'],"</tags>\n"
	"	</entry>"
	return xmlstring
xml_data_hash = { 'episode' : 24, 'status' : 'completed' }
stri = generateXML(xml_data_hash)
print(stri)

#curl_handle = pycurl.Curl()
