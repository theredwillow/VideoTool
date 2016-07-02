#!/usr/bin/python3 -i

import subprocess

from tools.core import *
from tools.videofinder import *


class Watch_Channel(object):

    def __init__(self, programs="", host=""):
        self.programs = []
        self.provided_host = host
        if programs == "":
            self.choose_shows()
        else:
            for program in programs:
                showtofind = Video_Finder(program, self.provided_host)
                self.programs.append(showtofind)
                self.provided_host = showtofind.chosen_hostsite
        # Now you have a list of Video_Finder objects

    def choose_shows(self):
        print("In order to watch a channel, you need shows. What would you like to watch?")
        continue_var = "yes"
        while continue_var == "yes":
            print("Tell me a show title you'd like to watch.")
            provided_title = input()
            showtofind = Video_Finder(provided_title, self.provided_host)
            self.programs.append(showtofind)
            self.provided_host = showtofind.chosen_hostsite
            print("Would you like to add another show to this channel? yes/no")
            continue_var = input()

    def launch(self):
        # This function starts the channel
        # NEEDS TO BE UPDATED WITH REAL RANDOM EPISODE
        process = subprocess.Popen(["youtube-dl", "https://www.youtube.com/watch?v=97_LhVw0qDg"],
                                   shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        print("Okay. I'm downloading an episode for you. Please hold.")
        # Can we put an actual download status bar here?
        print("Okay. It's downloaded!")
        # It needs to say "enjoy" and wait for an additional show to be added
