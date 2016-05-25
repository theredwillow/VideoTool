class watch_channel(object):

	def __init__(self, programs=""):
		if programs == "":
			choose_shows()
		else:
			for program in programs:
				check_for_program_url(program)

	def check_for_program_url(self,program_title=""):
		#check episode guides for provided_title
		#check if provided title has program urls for each hostsite
		#if they don't, ask the user to choose

	def choose_shows(self):
		print "In order to watch a channel, you need shows. What would you like to watch?"
		continue_var = "yes"
		while continue_var == "yes":
			print "Tell me a show title you'd like to watch."
			provided_title = raw_input()
			check_for_program_url(provided_title)
			print "Would you like to add another show to this channel? yes/no"
			continue_var = raw_input()


#watch_channel(programs=["The Simpsons", "Friends", "How I Met Your Mother"])