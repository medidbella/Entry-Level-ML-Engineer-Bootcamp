from bs4 import BeautifulSoup
import requests

pageUrl = "https://data.1337ai.org/"
response = requests.get(pageUrl)
rawData = BeautifulSoup(response.text, 'html.parser')
tableHeaders = rawData.find_all("th")
TableData = rawData.find_all("td")
keys = [str(elm).replace("<th>", "").
        replace("</th>", "") for elm in tableHeaders]
Values = [str(elm).replace("<td>", "").
          replace("</td>", "") for elm in TableData]
csvFile = open("data.csv", 'w')
index = 0
keysNumber = len(keys)

while index < keysNumber:
    csvFile.write(keys[index])
    if index != keysNumber - 1:
        csvFile.write(", ")
    index += 1
csvFile.write('\n')
index = 0


while index < len(Values):
    csvFile.write(Values[index])
    if (index + 1) % keysNumber == 0:
        csvFile.write('\n')
    else:
        csvFile.write(", ")
    index += 1
csvFile.write('\n')
