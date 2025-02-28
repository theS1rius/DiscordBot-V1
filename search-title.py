import requests
from bs4 import BeautifulSoup
import time
import random


class Website_Process():
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def fetch_page(self, page_number=None):
        if page_number:
            url = f"{self.url}/page/{page_number}"
        else:
            url = self.url
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        return None

    def parse_first_layer(self, soup):
        titles = []
        target_element = soup.select_one("div.loop-grid")
        if target_element:
            descriptions = target_element.find_all("div", class_="description")
            for description in descriptions:
                h3 = description.find("h3")
                if h3:
                    a_tag = h3.find("a")
                    if a_tag:
                        title = h3.get_text(strip=True)
                        href = a_tag["href"]
                        titles.append({"title": title, "href": href})
        return titles

    def parse_second_layer(self, soup):
        titles = []
        target_element = soup.select_one("div.container")
        if target_element:
            sections = target_element.find_all("div", class_="loop-post")
            for section in sections:
                articles = section.find_all("article")
                for article in articles:
                    h3 = article.find("h3")
                    if h3:
                        a_tag = h3.find("a")
                        if a_tag:
                            title = h3.get_text(strip=True)
                            href = a_tag["href"]
                            titles.append({"title": title, "href": href})
        return titles
    
    def get_all_title(self, max_pages=3):
        titles = []
        for page_number in range(1, max_pages + 1):
            soup = self.fetch_page(page_number)
            if soup:
                titles.extend(self.parse_first_layer(soup))
                titles.extend(self.parse_second_layer(soup))
            # 添加隨機緩衝時間
            time.sleep(random.uniform(1, 3))
        return titles




if __name__ == "__main__":
    url = "https://abmedia.io/category/trend/technology-development"  # 替換成你要爬取的網址
    website_process = Website_Process(url)
    loops = website_process.get_all_title()
    for i in loops :
        print(i["title"])
        print(i["href"])
        print("=====")