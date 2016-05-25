The /scrapers folder contains files that will teach the main file how to scrape codes from a particular website. If you'd like to create your own, here's how. If you get one up and running, please submit a pull request! :D
---

## Step 1
Define these global variables
<dl>
<dt>short_name</dt>
<dd>an abbreviation used within the script</dd>
<dt>full_name</dt>
<dd>the whole name that will appear as an option to the user</dd>
</dl>

## Step 2
Define class `host_scraper(object)`. This will be the class that the main file references for information from your scraper.

## Step 3
Define `host_scraper`'s initial function just like this:
```python
	def __init__(self, possible_hostsites):
		possible_hostsites.append([full_name,short_name])
```
This adds your new scraper to the main file's list of scrapers.

## Step 4
Define `host_scraper.program_search_vars()` with these variables:
<dl>
<dt>self.search_url</dt>
<dd>This is the first part of the url used for searches, include a final slash. (for example "http://www.example.com/search/" would be like "http://www.example.com/search/%s")</dd>
<dt>self.search_name</dt>
<dd>This is the name parameter for BeautifulSoup's find_all function used to grab possible program titles (for example: "div")</dd>
<dt>self.search_attrs</dt>
<dd>This is used for the attrs parameter for BeautifulSoup's find_all function mentioned before (for example: {"class": "program_title"})</dd>
<dt>self.server_url</dt>
<dd>This is used for websites that use relative paths (you know, "/index.html" in hyperlinks).
If you need it, write it in without a final slash (for example "http://www.example.com"). If you don't need it, define it as "".</dd>
</dl>

## Step 5
Define `host_scraper.tv_or_movie()`. It takes the `self` parameter obivously, but it also needs `program_url` (this is the url that the user will have chosen during the main file's execution). This function figures out whether the link chosen was a tv show or a movie. Define it however you want, but make sure it returns "tv" or "movie"

## Step 6
Define `host_scraper.episode_search_vars()` with these variables:
<dl>
<dt>self.search_name</dt>
<dd>This is the name parameter for BeautifulSoup's find_all function used to grab possible episode titles (for example: "div"). If it's the same as the one from step 5, you can comment it out.</dd>
<dt>self.search_attrs</dt>
<dd>This is used for the attrs parameter for BeautifulSoup's find_all function mentioned before (for example: {"class": "episode_title"}). If it's the same as the one from step 5, you can comment it out.</dd>
<dt>self.server_url</dt>
<dd>This is used for websites that use relative paths (you know, "/index.html" in hyperlinks).
If you need it, write it in without a final slash (for example "http://www.example.com"). If you don't need it, define it as "".
If it's the same as the one from step 5, you can comment it out.</dd>
<dt>self.commands</dt>
<dd>This is a list. Write BeautifulSoup codes, that the parsing main file will need for it's loop, as strings.</dd>
</dl>

```python
		self.commands = [
			"episode_info = episode.find('a')",
			"episode_title = episode_info.get('title').encode('UTF-8')",
			"episode_url = episode_info.get('href')",
			"episode_season = int( re.search(r'Season (.\d?) ', episode_title).group(1) )",
			"episode_number = int( re.search(r'Episode (.\d?) ', episode_title).group(1) )"
		]
```
In the example above, episodes are found with `episode_info` then cut up for the needed variables. You MUST define `episode_url`, `episode_season`, and `episode_number`. Those are the variables that will be appended into the list of episodes in the main file.

## Step 7
Define `host_scraper.source_search_vars()` with these variables:
<dl>
<dt>self.search_name</dt>
<dd>This is the name parameter for BeautifulSoup's find function used to grab the element containing the possible sources (for example: "table"). If it's the same as the one from step 6, you can comment it out.</dd>
<dt>self.search_attrs</dt>
<dd>This is used for the attrs parameter for BeautifulSoup's find_all function mentioned before (for example: {"class": "list_of_sources"}). If it's the same as the one from step 6, you can comment it out.</dd>
<dt>self.link_name</dt>
<dd>This is the name parameter for BeautifulSoup's find_all function used to grab possible source titles (for example: "div").</dd>
<dt>self.link_attrs</dt>
<dd>This is used for the attrs parameter for BeautifulSoup's find_all function mentioned before (for example: {"class": "source_title"}).</dd>
<dt>self.server_url</dt>
<dd>This is used for websites that use relative paths (you know, "/index.html" in hyperlinks).
If you need it, write it in without a final slash (for example "http://www.example.com"). If you don't need it, define it as "".
If it's the same as the one from step 6, you can comment it out.</dd>
</dl>

## Step 8
Define `host_scraper.final_step(self,url)`. It takes the `self` parameter obviously, but it also needs `url` (this is the url of a particular source site). The main file will be looping, looking for viable websites to watch the requested video from. This function is used if the URL's that you collected from step 7 are not actually the host site's links (i.e. it has a "click here for video" along with advertisements). If you're fortunate enough not to need this, just define it as `pass`.

HINT: If you need to scrape a website for BeautifulSoup in a commands variable, you can use the function `scrape_site(url)`.
Furthermore, if you need to scrap a javascript site, you can also pass that function `javascript="yes"`, but you'll need to edit the main file to include the path to your phantomjs exe.