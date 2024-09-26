from bs4 import BeautifulSoup
import requests

import re
from typing import Union

class Companies:

    def __init__(self, link: str, pages: int) -> None:
        self.link = link
        self.pages = pages
        self.companies = list()
        self.domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:]).group(0)
        

        self.get_html()
    
    def get_html(self) -> Union[None | str]:

        response = requests.get(url=self.link)
        code = response.status_code

        if code >= 200 and code < 400:
            with open("index.html", "w", encoding="utf-8") as file:
                file.writelines(response.text)
            
            with open("index.html", "r", encoding="utf-8") as file:
                self.soup = BeautifulSoup("".join(file.readlines()), "html.parser")

        else:
            return "error"
    
    def get_steel_fabrication(self):
        for i in range(2, self.pages + 2):
            h3_list = self.soup.find("div", class_="catalog-list").find_all("h3")

            for k in h3_list:
                self.companies.append("https://steel-fabrication.ru" + k.find("a")["href"])

            self.link = self.link.replace(re.search(pattern=r"\d$", string=self.link).group(0), str(i))
            self.get_html()

    def get_metalweb(self):
        for i in range(2, self.pages + 2):
            infinite_scroll = self.soup.find("article", class_="col-xs-12").find("div", class_="infinite-scroll")
            div_list = infinite_scroll.find_all("div", class_="pull-left")

            for k in div_list:
                self.companies.append(k.find("h3").find("a")["href"])
        
            self.link = self.link.replace(re.search(pattern=r"page.*", string=self.link).group(0), f"page{i}.html")
            self.get_html()















# c = Companies("https://www.metalweb.ru/catalog7/okrug1058/region291/", pages=28)
# c.get_metalweb()