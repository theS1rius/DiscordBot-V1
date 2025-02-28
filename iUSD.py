import requests
from bs4 import BeautifulSoup

class Website_Process():
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def fetch_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        return None  

    def parse(self, soup):
        theValue = []
        target_element = soup.select_one("div.loop-grid")
        if target_element:
            target_value = target_value.find_all("div", class_="description")
        return theValue

if __name__ == "__main__":
    url = "https://tw.tradingview.com/symbols/TVC-DXY/"  # 你的目標網址
    website_process = Website_Process(url)

    soup = website_process.fetch_page()  
    if soup:
        result = website_process.parse(soup)  
        if result:
            print([result])  # 應該輸出 107.38
        else:
            print("❌ 未找到目標數值")
    else:
        print("❌ 無法獲取網頁內容")