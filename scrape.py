#!/usr/bin/python3
"""scrapes a website"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

igbo_foods = []

url = "https://allnigerianfoods.com/igbo-foods/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div = soup.find("div", class_="karma-blog--single__content-wrapper page")

names = div.find_all("h3")
images = div.find_all("img")[1:]  # Adjusted the indexing
descs = div.find_all("a")[1:]  # Adjusted the indexing

# Iterate over the data and store in a list
for name, image, desc in zip(names, images, descs):
    igbo_foods.append([name.text, image['src'], desc['href']])

# Create a DataFrame
df = pd.DataFrame(igbo_foods, columns=['name', 'image', 'description'])

# Save the DataFrame to a CSV file
df.to_csv('igbo_foods.csv', index=False)
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

igbo_foods = []
names = []
images = []
descs = []
url = "https://allnigerianfoods.com/igbo-foods/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div = soup.find("div", class_="karma-blog--single__content-wrapper page")

for data in div:
	names = div.find_all("h3")
	images = div.find_all("img")
	images = images[1:]
	descs = div.find_all("a")
	descs = descs[1:]
igbo_foods.append([names, images, descs])


df = pd.DataFrame(igbo_foods, columns=['name', 'image', 'description'])
df.to_csv.writerows(('igbo_foods.csv'))
"""

