import urllib2, re, sqlite3, requests, webbrowser
from os.path import *
from bs4 import BeautifulSoup
from random import randint, randrange
from glob import glob
from imp import load_source, load_compiled
from selenium import webdriver
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, XML
from xml.dom import minidom
import subprocess

filepath = dirname(abspath(__file__))
error_words = ["404", "inconvenience", " not found", "expired", " delete", "t comply", "t exist", "remove", "error", "t be found"] #must be in lowercase

def check_internet():
	try:
		response=urllib2.urlopen('http://www.google.com',timeout=1)
	except urllib2.URLError as err:
		print "I'm sorry. This script only works if you're connected to the internet."
		raise SystemExit(0)

def scrape_site(url_to_scrape, javascript="no"):
	if javascript == "no":
		try:
			req = urllib2.Request(url_to_scrape, headers={ 'User-Agent': 'Mozilla/5.0' })
			content = urllib2.urlopen(req)
			httpcode = content.getcode()
			if httpcode < 200 or httpcode > 299:
				soup = "Broken Link"
			else:
				soup = BeautifulSoup(content.read(), "html.parser")
		except:
			soup = "Broken Link"
	else:
		try:
			driver = webdriver.PhantomJS(executable_path='C:\Python27\Tools\phantomjs.exe')
			driver.get(url_to_scrape)
			soup = BeautifulSoup(driver.page_source, "html.parser")
			driver.quit()
		except:
			soup = "Broken Link"
	return soup

def character_handler(char_solve):
	char_result = []
	try:
		char_result.append(int(char_solve))
	except:
		for slash_item in char_solve.split("/"):
			hyphen_splits = slash_item.split("-")
			if len(hyphen_splits) == 1:
				try:
					char_result.append(int(hyphen_splits[0]))
				except:
					char_result.append("Bad Input")
			elif len(hyphen_splits) > 2:
				char_result.append("Bad Input")
			else:
				hyphen_items = []
				for hyphen_item in hyphen_splits:
					try:
						hyphen_item = int(hyphen_item)
					except:
						char_result.append("Bad Input")
					hyphen_items.append(hyphen_item)
				if "Bad Input" not in char_result:
					for i in range(hyphen_items[0], hyphen_items[1]+1):
						char_result.append(i)
	return char_result

execfile(filepath+"/tools/videofinder.py")
execfile(filepath+"/tools/episode_guide.py")
execfile(filepath+"/tools/watch_channel.py")

#simp = Episode_Guide("phineas and ferb")
#simp.download(save="TRUE")
#simp.decorate()

channel = watch_channel(programs=["How I Met Your Mother"], host="LMWT")
channel.launch()