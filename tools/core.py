import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def check_internet():
	try:
		requests.get('http://www.google.com', timeout=1)
	except:
		print("ERROR: No internet connection")
		SystemExit(0)

def scrape_site(url_to_scrape, javascript="no"):
	if javascript == "no":
		try:
			req = requests.get(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0'})
			if req.status_code < 200 or req.status_code > 299:
				soup = "Broken Link"
			else:
				soup = BeautifulSoup(req.content, "html.parser")
		except:
			soup = "Broken Link"
	else:
		try:
			global path_to_webbrowser
			driver = webdriver.PhantomJS(executable_path=path_to_webbrowser)
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
					for i in range(hyphen_items[0], hyphen_items[1] + 1):
						char_result.append(i)
	return char_result
