The /tools folder is filled with classes that the main file executes. They really give the script its power.
---
Below is a list of the files in this folder. Beneath each one are the classes they contain and the functions you can use from them.

###videofinder.py
<dl>
<dt>Video_Finder.__init__()</dt>
<dd>Ran when class is initiated.</dd>
<dt>Video_Finder.watch()</dt>
<dd>Lets you watch a particular episode of a show via your web browser</dd>
</dl>


###watch_channel.py
Class `TV_Channel`
class that lets you watch random episodes from a `list` of shows. It uses youtube-dl and VLC.

###episode_guide.py
<dl>
<dt>Episode_Guide()</dt>
<dd>THIS IS A CLASS. Used to access episode guide information.</dd>
<dt>Episode_Guide().__init__()</dt>
<dd>Ran when class is initiated. It requires a name_of_show parameter.</dd>
<dt>Episode_Guide().load()</dt>
<dd>Checks if an episode guide is downloaded then opens it from xml file. If it's not, it starts the download() function.</dd>
<dt>Episode_Guide().download()</dt>
<dd>Downloads a complete episode guide from the internet. Optional parameter: "save" (set to "yes" to save an xml file of it as one of your frequented watched/favorite shows).</dd>
<dt>Episode_Guide().update()</dt>
<dd>Checks if an episode guide is up-to-date and downloads any missing information.</dd>
<dt>Episode_Guide().decorate()</dt>
<dd>After an episode guide has been downloaded, this helps you add information such as the poster and background URL's and colors.</dd>
<dt>Episode_Guide().view()</dt>
<dd>Adds a view to an episode. Requires the parameters: season, episode, and user. Optional parameter: time in "MM/DD/YYYY HH:MM" format.</dd>
<dt>Episode_Guide().unseen()</dt>
<dd>Returns a list of episodes that the user hasn't seen (two-dimensional, each item is a list of season and episode numbers). Requires the user parameter. Doesn't return unaired episodes (see unaired() function).</dd>
<dt>Episode_Guide().unaired()</dt>
<dd>Returns a list of episodes that haven't been aired yet (two-dimensional, each item is a list of season numbers, and episode numbers, and airdates).</dd>
</dl>
---
<dl>
<dt>Episode_Guide().episode()</dt>
<dd>THIS IS A SUBCLASS. Uses the character handler to choose an episode and gets its information. Read more about the character handler in /docs/character_handler.md. Also has shortcuts to closest downloaded match with exclamation marks (for example, "!simp" will open "The Simpsons" episode guide from the guide folder).</dd>
<dt>Episode_Guide().episode().__init__()</dt>
<dd>Ran when class is initiated. It returns an episode's information.</dd>
<dt>Episode_Guide().episode().detail()</dt>
<dd>Parameter: tag (set to a particular piece of information such as "airdate" or "description" to return it as a string).</dd>
<dt>Episode_Guide().episode().next()</dt>
<dd>Loads self with the next episode's information (i.e. S01E01 -> S01E02).</dd>
<dt>Episode_Guide().episode().previous()</dt>
<dd>Loads self with the previous episode's information (i.e. S01E02 -> S01E01).</dd>
</dl>
