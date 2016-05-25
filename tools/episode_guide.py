class Episode_Guide(object):

	def __init__(self, name_of_show):
		if name_of_show == "":
			print "You didn't provide the Episode_Guide instance with a name_of_show parameter."
			name_of_show = raw_input("What program would you like to work with?")
		self.proper_name_of_show=name_of_show.title()
		self.name_of_show = name_of_show.replace(" ", "-").lower()
		self.filename = join(filepath+"/show_info", self.proper_name_of_show.replace(" ", "-")+".xml")
		
	def load(self):
		if isfile(self.filename):
			self.show = ElementTree(file=self.filename)
		else:
			print "You don't have an episode guide saved for "+self.proper_name_of_show+", would you like to save one? yes/no"
			saveornot = raw_input()
			if saveornot == "yes":
				self.download(save="TRUE")
			else:
				self.download()

	def decorate(self):
		if not hasattr(self, "show"):
			self.load()
		print "Let's decorate!"
		print self.show
		#print self.show.find("decor")
		"""
		poster="http://www.posters.com/simpsons"
		color1="222"
		color2="222"
		color3="222"
		background_image="222"
		SubElement(self.show, "decor", background_image=background_image, color1=color1, color2=color2, color3=color3, poster=poster)
		"""

	"""
	def view(self):
		user="Jared"
		timestamp="04/20/2015 16:25"
		user = str(self.user)
		timestamp = str(self.timestamp)
		views = SubElement(episode, "views")
		SubElement(views,"view", user=user, time=timestamp)
	"""
	
	def download(self, save="FALSE"):
		soup = scrape_site("http://www.tv.com/shows/"+self.name_of_show+"/episodes/")
		assert soup != "Broken Link", "TV.com doesn't have an episode guide for "+self.proper_name_of_show+"."

		if save == "TRUE":
			print "I will be adding this show to your list of downloaded episode guides."
			print "Could you tell me if this show has continuity (i.e. you have to watch the episodes in order)?"
			print "If so, please type the word, TRUE. If not, please type the word, FALSE."
			continuity = raw_input()
			self.show = Element("show", title=self.name_of_show, continuity=continuity)
		else:
			self.show = Element("show", title=self.name_of_show)

		print "Creating an XML episode guide for "+self.proper_name_of_show+" by season...",
		seasonurls = [a['href'] for a in soup.findAll('a', href=re.compile(".*/shows/"+self.name_of_show+"/season-(\d+)/$"))]
		for season_counter, season in enumerate(seasonurls):
			current_season = len(seasonurls)-season_counter
			current_season=str(current_season).decode('utf-8')
			print current_season,
			soup = scrape_site("http://www.tv.com"+season)
			assert soup != "Broken Link", "Something went wrong while trying to download this season."
			season = SubElement(self.show, "season", number=str(current_season))
			episode_links = soup.findAll('a', href=re.compile(".*/shows/"+self.name_of_show+"/.*"), attrs={"class":"title"})
			for episode_counter, a in enumerate(episode_links):
				a.contents = ''.join(a.contents)

				current_episode = len(episode_links)-episode_counter
				description = a.findNext('div', attrs={"class":"description"})
				print description.contents
				print "Here's the change"
				print [str(a).decode("utf-8") for a in description.contents]
				description = ''.join(t for t in description.contents)
				print description
				description = ''.join(re.sub(r'<.*?>', '', description))
				description = ''.join(re.sub("(&nbsp;)|(moreless)|(\n)", ' ', description))
				
				airdate=''.join(a.findNext('div', attrs={"class":"date"}).contents)

				a.contents = a.contents.decode('utf-8')
				description = description.decode('utf-8')
				current_episode = str(current_episode)
				airdate = str(airdate)

				episode = SubElement(season, "episode", number=current_episode, airdate=airdate)
				SubElement(episode, "title").text = a.contents
				SubElement(episode, "description").text = description

		if save is "TRUE":
			xml_to_save = ElementTree.tostring(self.show, method='xml')
			xml_to_save = minidom.parseString(xml_to_save).toprettyxml(indent="\t")
			file = open(self.filename,"w")
			file.writelines(xml_to_save)
			file.close()
		print "Done."

	def random_episode(self):
		episode_list = self.show.getElementsByTagName('episode')
		random_epi = episode_list[randrange(0, len(episode_list)-1)]
		random_ep = []
		random_ep.append(random_epi.getElementsByTagName('title')[0].firstChild.data)
		random_ep.append(random_epi.getElementsByTagName('description')[0].firstChild.data)
		random_ep.append(random_epi.parentNode.getAttribute("number"))
		random_ep.append(random_epi.getAttribute("number"))
		random_ep.append(random_epi.getAttribute("airdate"))
		return random_ep
