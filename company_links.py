from bs4 import BeautifulSoup
import requests

import re

class Companies:

    def __init__(self, link: str, pages: int, headers: dict = None) -> None:
        self.link = link
        self.pages = pages
        self.headers = headers
        self.companies = list()
        self.domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:]).group(0)
        
        self.get_html()
    
    def get_html(self) -> None:
        if self.headers != None:
            response = requests.get(url=self.link, headers=self.headers)   
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
            if self.soup != "error":
                h3_list = self.soup.find("div", class_="catalog-list").find_all("h3")

                for k in h3_list:
                    self.companies.append("https://steel-fabrication.ru" + k.find("a")["href"])

            self.link = self.link.replace(re.search(pattern=r"PAGEN_6=\d+$", string=self.link).group(0), f"PAGEN_6={i}")
            self.get_html()

    def get_metalweb(self) -> None:
        for i in range(2, self.pages + 2):
            if self.soup != "error":
                infinite_scroll = self.soup.find("article", class_="col-xs-12").find("div", class_="infinite-scroll")
                div_list = infinite_scroll.find_all("div", class_="pull-left")

                for k in div_list:
                    self.companies.append(k.find("h3").find("a")["href"])
            
            self.link = self.link.replace(re.search(pattern=r"page.*", string=self.link).group(0), f"page{i}.html")
            self.get_html()
        
    def get_fabricators(self) -> None:
        for i in range(1, self.pages + 2):
            if self.soup != "error":
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
            if self.soup != "error":
                company_names = self.soup.find_all("div", class_="company-name")

                for k in company_names:
                    if k.find("a") == None:
                        continue
                    self.companies.append("https://www.oborudunion.ru" + k.find("a")["href"])
                
            self.link = self.link.replace(re.search(pattern=r"PAGEN_1=\d+$", string=self.link).group(0), f"PAGEN_1={i}")
            self.get_html()
    
    def get_manufacturers(self) -> None:
        for i in range(1, self.pages + 2):
            if self.soup != "error":
                sim_titles = self.soup.find("div", class_="companies-list").find_all("div", class_="sim-title")

                for k in sim_titles:
                    self.companies.append("https://manufacturers.ru/" + k.find("a")["href"])
                
            if i == 1:
                self.link += "?page=1"
            else:
                self.link = self.link.replace(re.search(pattern=r"page=\d+$", string=self.link).group(0), f"page={i}") 
            self.get_html()

    def get_orgpage(self) -> None:
        for i in range(1, self.pages + 2):
            if self.soup != "error":
                item_titles = self.soup.find("div", id="rubricator-result").find_all("div", class_="similar-item__title")

                for k in item_titles:
                    self.companies.append(k.find("a")["href"])
                
            if i == 1:
                self.link += "2/"
            else:
                self.link = self.link.replace(re.search(pattern=r"\d+\/$", string=self.link).group(0), f"{i}/") 
            self.get_html()
            
    def get_checko(self) -> None:
        for i in range(2, self.pages + 2):
            if self.soup != "error":
                links = self.soup.find("table", class_="data-table").find_all("a", class_="link")

            for k in links:
                self.companies.append("https://checko.ru" + k["href"])
        
            self.link = self.link.replace(re.search(pattern=r"page=\d+$", string=self.link).group(0), f"page={i}")
            self.get_html()
    
    def get_kemcsm(self)-> None:
        for i in range(1, self.pages + 2):
            if self.soup != "error":
                factory_heads = self.soup.find("div", class_="factory-wrap").find_all("div", class_="factory__head")

                for k in factory_heads:
                    self.companies.append("https://kemcsm.ru" + k.find("a")["href"])
                
            if i == 1:
                self.link += "?page=1"
            else:
                self.link = self.link.replace(re.search(pattern=r"page=\d+$", string=self.link).group(0), f"page={i}")
            self.get_html()

    def get_wiki_prom(self) -> None:
        for i in range(2, self.pages + 2):
            if self.soup != "error":
                titles = self.soup.find("div", class_="list-block").find_all("div", class_="title")

                for k in titles:
                    self.companies.append(k.find("a")["href"])
            
            if i == 2:
                self.link = self.link[0:28] + "/page2/" + "mashinostroitelnye-zavody.html"
            else:
                self.link = self.link.replace(re.search(pattern=r"page\d+", string=self.link).group(0), f"page{i}")
            self.get_html()












# dict_ = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

# c = Companies(link="https://www.wiki-prom.ru/169/mashinostroitelnye-zavody.html", pages=3)
# c.get_wiki_prom()
# print(c.companies)