import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://disclosures.ecq.qld.gov.au/Map'
response = requests.get(url)
html = response.content

soup = BeautifulSoup (html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)


outfile = open("./donations.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Donor", "Recipient", "Date of gift", "Donor electorate", "Donor address", "Gift value"])
writer.writerows(list_of_rows)
