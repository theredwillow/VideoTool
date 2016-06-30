from tools.core import *
from tools.videofinder import *
from tools.episode_guide import *
from tools.watch_channel import *

path_to_webbrowser = 'C:\Python35-32\Tools\webbrowsers\phantomjs.exe'
error_words = ["404", "inconvenience", " not found", "expired", " delete", "t comply",
				"t exist", "remove", "error", "t be found"]  # Must be in lowercase

print(Episode_Guide("coupling").random_episode())

# simp = Episode_Guide("phineas and ferb")
# simp.download(save="TRUE")
# simp.decorate()

# channel = Watch_Channel(programs=["How I Met Your Mother"], host="LMWT")
# channel.launch()
