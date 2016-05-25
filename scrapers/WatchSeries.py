from re import compile

short_name = "WatchSeries"
full_name = "WatchSeries.to"

class host_scraper(object):

	def __init__(self, possible_hostsites):
		possible_hostsites.append([full_name,short_name])

	def program_search_vars(self):
		self.search_url = "http://thewatchseries.to/search/"
		self.search_name = "div"
		self.search_attrs = {"valign": "top","style": "padding-left: 10px;"}
		self.server_url = "http://thewatchseries.to"

	def tv_or_movie(self,program_url):
		return "tv"

	def episode_search_vars(self):
		self.search_name = "li"
		self.search_attrs = {"itemprop": "episode", "itemscope": "", "itemtype": "http://schema.org/TVEpisode"}
		#self.server_url = "http://thewatchseries.to"
		self.commands = [
			"episode_number = int( episode.find('meta', {'itemprop':'episodenumber'}).get('content') )",
			"episode_url = '"+self.server_url+"' + episode.find('a').get('href')",
			"episode_season = int( re.search(r'_s(.\d?)_e', episode_url).group(1) )",
		]

	def source_search_vars(self):
		self.search_name = "tr"
		self.search_attrs = {"class": compile('download_link_.*'), "id": compile('link_.*')}
		self.link_name = "a"
		self.link_attrs = {"target":"_blank","class":"buttonlink","style":"cursor:pointer;"}
		#self.server_url = "http://thewatchseries.to"

	def final_step(self,url):
		return [
			"url = scrape_site('"+url+"', javascript='yes').find('a',{'class': 'push_button blue'}).get('href')"
		]