import requests, csv
from bs4 import BeautifulSoup

url = 'https://www.billboard.com/charts/r-b-hip-hop-songs'

with open('Billboard_Hip_Hop_Charts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Billboard Number','Artist Name','Song Title','Last Week Number','Peak Position','Weeks On Chart'])

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    for container in soup.find_all("article",class_="chart-row"):

        billboard_number = container.find(class_="chart-row__current-week").text

        artist_name_a_tag = container.find(class_="chart-row__artist").text.strip()

        song_title = container.find(class_="chart-row__song").text

        last_week_number_tag = container.find(class_="chart-row__value")
        last_week_number = last_week_number_tag.text

        peak_position_tag = last_week_number_tag.find_parent().find_next_sibling().find(class_="chart-row__value")
        peak_position = peak_position_tag.text

        weeks_on_chart_tag = peak_position_tag.find_parent().find_next_sibling().find(class_="chart-row__value").text

        print(billboard_number,artist_name_a_tag,song_title,last_week_number,peak_position,weeks_on_chart_tag)
        writer.writerow([billboard_number,artist_name_a_tag,song_title,last_week_number,peak_position,weeks_on_chart_tag])