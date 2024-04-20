import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.co.uk/biz/fatisa-london?osq=Restaurants"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

mylinks = soup.find_all("div", {"class": "header_nav_unit"})
print(len(mylinks))


counter = 0
for link in mylinks:
  if counter > 1:
   print(link.text)
  counter += 1