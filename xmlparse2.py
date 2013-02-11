#!/usr/bin/python

import pickle
import xml.etree.cElementTree as et

def parse_root(xml_tree):
	anime_list = {}
	for child in xml_tree:
		if(child.tag=='anime'):
			anime_series=parse_anime_entry(child)
			anime_list[anime_series['series_animedb_id']]=anime_series
	print(anime_list)
	return anime_list

def parse_anime_entry(anime_entry):
	result = {}
	for tag in anime_entry:
		result[tag.tag] = tag.text
	return result

tree=et.parse('sample2.xml')
root=tree.getroot()

print(root.tag)
anime_list = parse_root(root)

file = open("xml-file.pickle", "wb")
pickle.dump(anime_list,file,2)
