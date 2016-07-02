from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

title_of_show = "The Simpsons"
poster = "http://www.posters.com/simpsons"
color1 = ""
color2 = ""
color3 = ""
background_image = ""

season_number = "1"
title_of_episode = "Treehouse of Horror"
episode_number = "1"
airdate = "04/20/2000 16:20"
description = "Three scary stories that will scare you. Boo!"

user = "Jared"
timestamp = "04/20/2015 16:25"

show = Element("show", title=title_of_show, continuity="FALSE")
SubElement(show, "decor", background_image=background_image, color1=color1, color2=color2, color3=color3, poster=poster)

season = SubElement(show, "season", number=season_number)
episode = SubElement(season, "episode", title=title_of_episode, airdate=airdate, number=episode_number)
SubElement(episode, "description").text = description

views = SubElement(episode, "views")
SubElement(views, "view", user=user, time=timestamp)

print prettify(show)
