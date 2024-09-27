from bs4 import BeautifulSoup
import requests

import re
from typing import Union

class Companies:

    def __init__(self, link: str, pages: int, cookie: str = None) -> None:
        self.link = link
        self.pages = pages
        self.cookie = cookie
        self.companies = list()
        self.domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:]).group(0)
        
        self.get_html()
    
    def get_html(self) -> Union[None | str]:
        if self.cookie != None:
            response = requests.get(url=self.link, headers={"cookie": self.cookie})   
        else:
            response = requests.get(url=self.link)

        code = response.status_code

        if code >= 200 and code < 400:
            with open("index.html", "w", encoding="utf-8") as file:
                file.writelines(response.text)
            
            with open("index.html", "r", encoding="utf-8") as file:
                self.soup = BeautifulSoup("".join(file.readlines()), "html.parser")
        else:
            self.soup = "error"
    
    def get_steel_fabrication(self) -> None:
        for i in range(2, self.pages + 2):
            h3_list = self.soup.find("div", class_="catalog-list").find_all("h3")

            for k in h3_list:
                self.companies.append("https://steel-fabrication.ru" + k.find("a")["href"])

            self.link = self.link.replace(re.search(pattern=r"PAGEN_6=\d+$", string=self.link).group(0), f"PAGEN_6={i}")

            self.get_html()

    def get_metalweb(self) -> None:
        for i in range(2, self.pages + 2):
            infinite_scroll = self.soup.find("article", class_="col-xs-12").find("div", class_="infinite-scroll")
            div_list = infinite_scroll.find_all("div", class_="pull-left")

            for k in div_list:
                self.companies.append(k.find("h3").find("a")["href"])
        
            self.link = self.link.replace(re.search(pattern=r"page.*", string=self.link).group(0), f"page{i}.html")
            self.get_html()
    
    def get_fabricators(self) -> None:
        for i in range(1, self.pages + 2):
            content_list_div = self.soup.find("div", class_="content-list--padding")
            div_enterprise = content_list_div.find_all("div", class_="enterprise-teaser")

            for k in div_enterprise:
                self.companies.append("https://fabricators.ru" + k.find("a")["href"])
            
            if i == 1:
                self.link += "?ysclid=m1kjzaqwyj637159448&page=1"
            else:
                self.link = self.link.replace(re.search(pattern=r"page=\d+$", string=self.link).group(0), f"page={i}")

            self.get_html()
    
    def get_oborudunion(self) -> None:
        for i in range(2, self.pages + 2):
            company_names = self.soup.find_all("div", class_="company-name")

            for k in company_names:
                if k.find("a") == None:
                    continue
                self.companies.append("https://www.oborudunion.ru" + k.find("a")["href"])
            
            self.link = self.link.replace(re.search(pattern=r"PAGEN_1=\d+$", string=self.link).group(0), f"PAGEN_1={i}")
            self.get_html()
















# c = Companies("https://www.oborudunion.ru/company/metalloobrabatyvayuschee-oborudovanie?PAGEN_1=1", pages=111, cookie="_ym_uid=1727160878853987332; _ym_d=1727160878; _ym_isad=1; _ym_visorc=w;")
# c.get_oborudunion()