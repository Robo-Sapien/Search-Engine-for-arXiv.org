import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('Phy-gr-qc.csv', 'w'))
f.writerow(['Title', 'Authors', 'Abstract', 'Date', 'URL'])
CSpages = []
# CSpages.append(requests.get('https://arxiv.org/list/cs.DS/pastweek?show=26'))
# CSpages.append(requests.get('https://arxiv.org/list/cs.GR/recent'))
# CSpages.append(requests.get('https://arxiv.org/list/cs.LG/pastweek?show=152'))
# CSpages.append(requests.get('https://arxiv.org/list/cs.AI/pastweek?show=70'))
# CSpages.append(requests.get('https://arxiv.org/list/cs.IR/pastweek?show=26'))
# CSpages.append(requests.get('https://arxiv.org/list/astro-ph/new'))
# CSpages.append(requests.get('https://arxiv.org/list/cond-mat/new'))
# CSpages.append(requests.get('https://arxiv.org/list/gr-qc/new'))


for page in CSpages:
    relativeLinks = []
    soup = BeautifulSoup(page.text, 'html.parser')
    AbstractLinks = soup.find_all('a', {"title" : "Abstract"})
    for link in AbstractLinks:
        relativeLinks.append(link['href']);
    for relativeLink in relativeLinks:
        finalLink = 'https://arxiv.org' + relativeLink
        abstractPage = requests.get(finalLink)
        abstractPageSoup = BeautifulSoup(abstractPage.text, 'html.parser')
        title = abstractPageSoup.find('h1', class_='title').contents[1]
        submissionDate = abstractPageSoup.find('div', class_='dateline').contents[0]
        authorDiv = abstractPageSoup.find('div', class_='authors')
        authorList = authorDiv.find_all('a')
        authors = []
        for author in authorList:
            authors.append(author.contents[0])
        authorString = (", ".join(authors))
        abstract = abstractPageSoup.find('blockquote', class_='abstract').contents[2]
        print(title)
        # print(submissionDate)
        # print(authorString)
        # print(abstract)
        f.writerow([title, authorString, abstract, submissionDate, finalLink])
