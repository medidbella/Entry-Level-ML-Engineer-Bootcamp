from bs4 import BeautifulSoup
import requests

pageUrl = "https://data.1337ai.org/"
response = requests.get(pageUrl)
rawData = BeautifulSoup(response.text, 'html.parser')
rows = rawData.find_all("th")

rowsText = []
for elm in rows:
    rowsText.append(str(elm).replace("<th>", "").replace("</th>", ""))
print(rowsText)