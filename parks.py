# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

PARKS_LIST = [
    "Acadia", "American Samoa", "Arches", "Badlands", "Big Bend",
    "Biscayne", "Black Canyon of the Gunnison", "Bryce Canyon", "Canyonlands", "Capitol Reef",
    "Carlsbad Caverns", "Channel Islands", "Congaree", "Crater Lake", "Cuyahoga Valley",
    "Death Valley", "Denali", "Dry Tortugas", "Everglades", "Gates of the Arctic",
    "Gateway Arch", "Glacier", "Glacier Bay", "Grand Canyon", "Grand Teton",
    "Great Basin", "Great Sand Dunes", "Great Smoky Mountains", "Guadalupe Mountains", "Haleakalā",
    "Hawaiʻi Volcanoes", "Hot Springs", "Indiana Dunes", "Isle Royale", "Joshua Tree",
    "Katmai", "Kenai Fjords", "Kings Canyon", "Kobuk Valley", "Lake Clark",
    "Lassen Volcanic", "Mammoth Cave", "Mesa Verde", "Mount Rainier","North Cascades",
    "Olympic", "Petrified Forest", "Pinnacles", "Redwood", "Rocky Mountain",
    "Saguaro", "Sequoia", "Shenandoah", "Theodore Roosevelt", "Virgin Islands",
    "Voyageurs", "Wind Cave", "Wrangell–St. Elias", "Yellowstone", "Yosemite", "Zion"
]

URL_PREFIX = 'https://www.google.com/search?newwindow=1&btnI=I%27m+Feeling+Lucky&q="'
URL_SUFFIX = '" "National Park" "Plan Your Visit" "Basic Information" "Pets" site:nps.gov'

for park in PARKS_LIST:

    URL = URL_PREFIX + park + URL_SUFFIX

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    html = requests.get(URL, headers=headers).content
    soup = BeautifulSoup(html, features="html.parser")
    soup = soup.select('div.ColumnMain')[0]

    print(park)
    print("==========")
    print(soup.getText())
    print("\n\n")
