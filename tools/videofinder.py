class Video_Finder(object):

	def __init__(self, provided_title="", provided_host=""):   #Sets up the show and hostsite
		check_internet()
		self.provided_title=provided_title
		if self.provided_title == "":
			self.choose_show()
		self.choose_hostsite(provided_host)
		assert self.provided_title != "", "Video_Finder objects need a show name to find a program."
		self.choose_program()

	def watch(self, *args, **kwargs):   #Opens the url of a video
		assert hasattr(self, "program_url"), "The watch function needs a URL from a host site."
		if self.scraper.tv_or_movie(self.program_url) is "tv":
			self.collect_episodes()

			if kwargs:
				if "season" in kwargs:
					chosen_seasons = character_handler(kwargs["season"])
					if "Bad Input" not in chosen_seasons:
						self.season_selected = chosen_seasons[randint(0, len(chosen_seasons)-1)]
					else:
						print "Looks like you provided a bad season argument."
						self.choose_season()
			if not hasattr(self, "season_selected") and args:
				if "random" in args:
						self.season_selected = randint(1, self.number_of_seasons)
				elif "latest" in args:
						self.season_selected = self.number_of_seasons
				"""
				elif "unseen" in args:
						self.season_selected = "UNSEEN"
				"""
			if not hasattr(self, "season_selected"):
				self.choose_season()

			self.number_of_episodes = max(b for (a,b,c) in self.episodes if a == self.season_selected)

			if kwargs:
				if "episode" in kwargs:
					chosen_episodes = character_handler(kwargs["episode"])
					if "Bad Input" not in chosen_episodes:
						self.episode_selected = chosen_episodes[randint(0, len(chosen_episodes)-1)]
					else:
						print "Looks like you provided a bad episode argument."
						self.choose_episode()
			if not hasattr(self, "episode_selected") and args:
				if "random" in args:
						self.episode_selected = randint(1, self.number_of_episodes)
				elif "latest" in args:
						self.episode_selected = self.number_of_episodes
				"""
				elif "unseen" in args:
						self.episode_selected = "UNSEEN"
				"""
			if not hasattr(self, "episode_selected"):
				self.choose_episode()

			self.episode_url = [i for i in self.episodes if i[0] == self.season_selected and i[1] == self.episode_selected][0][2]
		else:
			pass #We need to grab movie URL's!!! self.episode_url = 
		self.collect_sources()
		self.choose_source()

	def choose_hostsite(self, provided_host=""):   #Helps the user choose a hostsite
		possible_hostsites = []
		modules = {}
		scraper = {}
		for path in glob(join(filepath+"/scrapers",'[!_]*.py')): # list .py files not starting with '_'
			name, ext = splitext(basename(path))
			if isfile(path+'c'):
				modules[name] = load_compiled(name, path+'c')
			else:
				modules[name] = load_source(name, path)
			scraper[name] = modules[name].host_scraper(possible_hostsites)

		if provided_host in scraper:
			chosen_hostsite = provided_host
		else:
			provided_host = ""

		if provided_host == "":
			print "Do you have a prefered hostsite?"
			for counter, host in enumerate(possible_hostsites):
				print str(counter+1)+". "+host[0]
			chosen_hostsite = raw_input()
			if chosen_hostsite.lower() == "no":
				chosen_hostsite = possible_hostsites[0][1]
			else:
				try:
					chosen_hostsite = possible_hostsites[int(chosen_hostsite)-1][1]
				except:
					print "You haven't provided a number choice or the word, no. So I don't know what to do..."
					raise SystemExit(0)
		self.chosen_hostsite = chosen_hostsite
		self.scraper = scraper[chosen_hostsite]

	def choose_show(self):   #Helps the user choose a show
		print "What would you like to watch?"
		self.provided_title = raw_input()

	def choose_program(self):   #Scrapes the URL of a program from a video host indexing site
		self.scraper.program_search_vars()
		soup = scrape_site(self.scraper.search_url + self.provided_title.replace(" ", "%20"))
		assert soup != "Broken Link", "Something may be wrong with the host site."
		possible_options = soup.find_all(name = self.scraper.search_name, attrs = self.scraper.search_attrs)
		if not possible_options:
			print "I'm sorry. I'm not finding any results for that program."
			print ""
			selection = ""
		elif len(possible_options) > 1:
			print "It looks like you have a few options for " + self.provided_title.title() + ". Take your pick!"
			print ""
			for counter, program_name in enumerate(possible_options):
				counter = counter + 1
				print counter,program_name.find('a').get("title").encode('UTF-8').replace('Watch ','')
			print ""
			selection = input()
			print ""
			selection = possible_options[selection-1].find('a').get("href")
		else:
			selection = possible_options[0].find('a').get("href")
		self.program_url = self.scraper.server_url + selection

	def collect_episodes(self):   #Scrapes the list of episodes from the video host indexing site
		soup = scrape_site(self.program_url)
		assert soup != "Broken Link", "Something may be wrong with the host site."
		self.scraper.episode_search_vars()
		self.episodes = []
		for episode in soup.find_all(name = self.scraper.search_name, attrs = self.scraper.search_attrs):
			for code in self.scraper.commands:
				exec code
			if episode_season != '0' and episode_number != '0':
				self.episodes.append([episode_season, episode_number, episode_url])
		self.number_of_seasons = max(a for (a,b,c) in self.episodes)

	def choose_season(self):   #Helps the user choose which season they want to watch
		print "Which season would you like to watch? There are %s." % self.number_of_seasons
		self.season_selected = input()

	def choose_episode(self):   #Helps the user choose which episode they want to watch
		print "Which episode would you like to watch? There are %s in this season." % self.number_of_episodes
		self.episode_selected = input()

	def get_votes(self):   #Checks the SQL table for video hosting ratings
		self.conn = sqlite3.connect('C:/sqlite3/source_hosts.db')
		self.c = self.conn.cursor()
		self.hosttable={}
		for (a,b) in self.c.execute("SELECT * from hosts"):
			self.hosttable[a]=int(b)

	def collect_sources(self):   #Scrapes the list of sources from the host indexing website
		soup = scrape_site(self.episode_url)
		assert soup != "Broken Link", "Something may be wrong with the host site."
		self.get_votes()
		self.scraper.source_search_vars()
		self.sources = []
		for source in soup.find_all(name = self.scraper.search_name, attrs = self.scraper.search_attrs):
			links = source.find_all(name = self.scraper.link_name, attrs = self.scraper.link_attrs)
			if str(links[-1]).find("Part") < 0:											#WITH THIS SET-UP, YOU CAN'T WATCH VIDEOS SPLIT INTO PARTS
				source_link = links[-1].get('href')
				if source_link.startswith('/'):
					host = links[-1].get('title').split()[-1]
					if host in self.hosttable:
						vote=self.hosttable[host]
					else:
						vote=0
					self.sources.append([self.scraper.server_url+source_link, host, vote])
		self.sources.sort(key=lambda x: x[2], reverse=True)

	def visible(self, element):   #Helps the program know if the text is visible or not
		if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
			return False
		return True

	def choose_source(self):   #Reorders the list of sources by reliability and helps the user choose one
		self.error_words = [f for f in error_words if f not in self.provided_title.lower()]
		print "Finding a source..."
		for (url,host,vote) in self.sources:
			for code in self.scraper.final_step(url):
				exec code
			soup = scrape_site(url)
			if soup != "Broken Link":
				texts = soup.find_all(text=True)											#WITH THIS SET-UP, IT DOES NOT CHECK FOR THE TITLE
				visible_text = str(filter(self.visible, texts)).decode('utf-8', 'ignore').lower()
				words_found=[x for x in self.error_words if x in visible_text]

				if any(words_found):
					print "Yeah... no. The one from %s is crap. I found these words: %s. Lemme check another..." % (host,", ".join(words_found))
					if host in self.hosttable:
						self.hosttable[host]-=1
					else:
						self.hosttable[host]=-1
				else:
					webbrowser.open(url)
					print "Does this link from %s work for you? yes/no" % host
					link_status=raw_input()
					if link_status == "escape":
						break
					if link_status == "yes":
						if host in self.hosttable:
							self.hosttable[host]+=1
						else:
							self.hosttable[host]=1
						print "Enjoy!"
						break
					else:
						print "Let's see..."
						if host in self.hosttable:
							self.hosttable[host]-=1
						else:
 							self.hosttable[host]=-1
			else:
				print "Yeah... no. This one from " + host + " is a broken link. Lemme check another..."
				if host in self.hosttable:
					self.hosttable[host]-=1
				else:
					self.hosttable[host]=-1
		else:
			print "I'm sorry. I was unable to find any working sources from LetMeWatchThis."
		self.report_to_table()

	def report_to_table(self):   #Updates the SQL table with host site ratings, deleting redundant zero rated sources
		self.hosttable = {k:v for k,v in self.hosttable.items() if v != 0}
		self.c.execute("DROP TABLE `hosts`;")
		self.conn.commit()
		self.c.execute("CREATE TABLE `hosts` (`hosts` TEXT,`vote` TEXT);")
		self.conn.commit()
		for k,v in self.hosttable.items():
			if v!=0:
				self.c.execute('INSERT INTO `hosts`(`hosts`,`vote`) VALUES ("%s","%s");' % (k,v))
				self.conn.commit()
		self.conn.close()
