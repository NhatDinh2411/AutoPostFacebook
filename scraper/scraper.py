import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List

def get_paper(path: str = 'https://congthuong.vn/thi-truong') -> List:

    detail_papers = []
    link_papers = []

    date = datetime.now().strftime("%d/%m/%Y")
    response = requests.get(path)
    bs = BeautifulSoup(response.content, 'html.parser')
    tags = bs.find("div", {"class": "colLeft lt"}).find_all("a", {"class": "article-link"})

    for tag in tags:
        link_papers.append(tag['href'])

    link_papers = link_papers[0:10]

    for link in link_papers:
        try:
            response = BeautifulSoup(requests.get(link).content, 'html.parser')
            date_paper = response.find("span", {"class": "format_time"}).text.split()[0]
            if date_paper != date:
                continue
            text = response.find("div", {"class": "article-detail-right"}).text
            detail_papers.append(text)

        except Exception as e:
            print(link, e)


    return detail_papers