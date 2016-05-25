#from re import compile

short_name = "LMWT"
full_name = "LetMeWatchThis"

class host_scraper(object):

	def __init__(self, possible_hostsites):
		possible_hostsites.append([full_name,short_name])

	def program_search_vars(self):
		self.search_url = "http://www.watchfreemovies.ch/search/"
		self.search_name = "div"
		self.search_attrs = {"class": "index_item index_item_ie"}
		self.server_url = ""

	def tv_or_movie(self,program_url):
		if "watch-tv-shows" in program_url:
			return "tv"
		elif "watch-movies" in program_url:
			return "movie"
		elif not program_url:
			print "ERROR: Cannot determine if this is a television show or a movie without the URL of the program."
			raise SystemExit(0)
		else:
			print "ERROR: Cannot determine if this is a television show or a movie. Please check the web scraping code."
			raise SystemExit(0)

	def episode_search_vars(self):
		#self.search_name = "div"
		self.search_attrs = {"class": "tv_episode_item"}
		#self.server_url = ""
		self.commands = [
			"episode_info = episode.find('a')",
			"episode_title = episode_info.get('title').encode('UTF-8')",
			"episode_url = episode_info.get('href')",
			"episode_season = int( re.search(r'Season (.\d?) ', episode_title).group(1) )",
			"episode_number = int( re.search(r'Episode (.\d?) ', episode_title).group(1) )"
		]

	def source_search_vars(self):
		self.search_name = "table"
		self.search_attrs = {"class": "movie_version"}
		self.link_name = "a"
		self.link_attrs = {"target":"_blank"}
		self.server_url = "http://www.watchfreemovies.ch"

	def final_step(self,url):
		return []