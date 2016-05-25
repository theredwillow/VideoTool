The /show_info folder is used to keep episode guides for your favorite shows.
---

## Naming Convention
These xml files are named by replacing spaces with -. First words are capitalized. For example "Modern Family" becomes `Modern-Family.xml`

## The Structure
```xml
<?xml version="1.0" ?>
<show continuity="FALSE" title="modern-family">
	<hostsites>
		<host site="LMWT" url="http://www.letmewatchthis.ch/series/modern-family123" />
	</hostsites>
	<decor background_image="http://www.example.com/familyshow.png" color1="#00e600" color2="#cc99ff" color3="#33cc33" poster="http://www.posters.com/simpsons.jpg"/>
	<season number="1">
		<episode airdate="5/18/16" number="1">
			<title>Episode S01E01's Title Goes Here</title>
			<description>In season one's first episode, the protagonist does stuff. The antagonist sucks though!</description>
			<views>
				<view time="04/20/2015 16:25" user="Bob"/>
			</views>
		</episode>
	</season>
</show>
```

#### What does it all mean?
<dl>
<dt>`show` is the main tag.</dt>
<dd>It has `continuity` a binary attribute. If "TRUE", the show must be viewed in order to make sense. Game of Thrones is an excellent example (you have to watch it from the beginning to understand what's going on). If "FALSE", any episode can be viewed at any time. The Simpsons is an excellent example (you can pick up any episode and be just fine).</dd>
<dd>It also has `title`.</dd>

<dt>`hostsites` is below `show`.</dt>
<dd>It is used to collect the program url's from the host sites (that way you don't have to bug the user for clarification each use, like "The Simpsons (1989)" vs "The Simpsons Movie").</dd>
<dd>It contains the tags, `host`, which have the attributes `site` (which is the host scraper's short name) and `url` (the URL of the program on that particular host).</dd>

<dt>`decor` is below `show`.</dt>
<dd>It is used for display decoration.</dd>
<dd>It has the attribute `background_image` which is the URL of an image that the script can run for a background image (like the clouds on the Simpsons).</dd>
<dd>The color attributes `color1`, `color2`, and `color3` are hexadecimal color codes. Depending on the user's settings, the darkest one will be the background, the lightest one will be the text color, or vice-versa etc...</dd>
<dd>The `poster` attribute is the URL to a poster for the show (height must be longer than width).</dd>

<dt>`season` is a season.</dt>
<dd>They are differentiated by the `number` attribute.</dd>

<dt>`episode` is below the season that it belongs to.</dt>
<dd>They have the attributes `airdate` and `number` (which is the number it was in the season, not the series).</dd>
<dd>Below it are the `title` of the episode, the `description` of the episode, and `views`.</dd>

<dt>`views` is a way for this program to remember if you've watched the episode or not.</dt>
<dd>Entries are added as `view` with the attributes `time` which was the time and date that the user watched it and `user`.</dd>
<dd>This is a great way to query the program for the episodes you haven't seen.</dd>
</dl>
---
NOTE: Any show can have an episode guide generated for it, but only your favorites are stored here. This reduces long-term memory issues, but also allows your frequent shows to be viewed without having to constantly contact the episode guide website.