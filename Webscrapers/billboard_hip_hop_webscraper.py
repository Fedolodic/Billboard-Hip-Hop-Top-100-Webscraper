from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.billboard.com/charts/r-b-hip-hop-songs'

# Opens web connetion and grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs song title, artist and picture
mainContainer = page_soup.findAll("div", {"class":"chart-row__main-display"})

# CSV filename creation
filename = "Billboard_Hip_Hop_Charts.csv"
f = open(filename, "w")

# Creating Headers
headers = "Billboard Number, Artist Name, Song Title, Last Week Number, Peak Position, Weeks On Chart\n"
f.write(headers)

# Get Billboard Number, Artist Name and Song Title 
for container in mainContainer:
	# Gets billboard number
	billboard_number = container.div.span.text

	# Gets artist name
	artist_name_a_tag = container.findAll("", {"class":"chart-row__artist"})
	artist_name = artist_name_a_tag[0].text.strip()

	# Gets song title
	song_title = container.h2.text

	print("Billboard Number: " + billboard_number)
	print("Artist Name: " + artist_name)
	print("Song Title: " + song_title)
	
	f.write(billboard_number + "," + artist_name + "," + song_title + "\n")

# Grabs side container from main container
secondaryContainer = page_soup.findAll("div", {"class":"chart-row__secondary"})

# Get Last Week Number, Peak Position and Weeks On Chart
for container in secondaryContainer:
	# Gets last week number
	last_week_number_tag = container.findAll("", {"class":"chart-row__value"})
	last_week_number = last_week_number_tag[0].text

	# Gets peak position
	peak_position_tag = container.findAll("", {"class":"chart-row__value"})
	peak_position = peak_position_tag[1].text

	# Gets week on chart
	weeks_on_chart_tag = container.findAll("", {"class":"chart-row__value"})
	weeks_on_chart = weeks_on_chart_tag[2].text

	print("Last Week Number: " + last_week_number)
	print("Peak Position: " + peak_position)
	print("Weeks On Chart: " + weeks_on_chart)
	
	f.write(last_week_number + "," + peak_position + "," + weeks_on_chart + "\n")

f.close()