from bs4 import BeautifulSoup
import requests

from src.loggers import main_logger

import re
from time import sleep

class Site:

    def __init__(self, link: str, pages: int, headers: dict = None) -> None:
        self._link = link
        self._pages = pages
        self._headers = headers
        self._companies = list()
        self._domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:]).group(0)
        
        self._get_html()
    
    def _get_html(self) -> None:
        if self._headers != None:
            response = requests.get(url=self._link, headers=self._headers)   
        else:
            response = requests.get(url=self._link)

        code = response.status_code

        if code >= 200 and code < 400:
            self.soup = BeautifulSoup(response.text, "html.parser")
        else:
            self.soup = "error"
    
    def _get_steel_fabrication(self) -> None:
        for i in range(2, self._pages + 2):
            if self.soup != "error":
                h3_list = self.soup.find("div", class_="catalog-list").find_all("h3")

                for k in h3_list:
                    self._companies.append("https://steel-fabrication.ru" + k.find("a")["href"])

            self._link = self._link.replace(re.search(pattern=r"PAGEN_6=\d+$",
                                                      string=self._link).group(0), f"PAGEN_6={i}")
            self._get_html()
            main_logger.info(f"Собрано {i - 1} ссылок на профили (steel fabrication)")

    def _get_metalweb(self) -> None:
        for i in range(2, self._pages + 2):
            if self.soup != "error":
                infinite_scroll = self.soup.find("article", class_="col-xs-12").find("div", class_="infinite-scroll")
                div_list = infinite_scroll.find_all("div", class_="pull-left")

                for k in div_list:
                    self._companies.append(k.find("h3").find("a")["href"])
            
            self._link = self._link.replace(re.search(pattern=r"page.*",
                                                      string=self._link).group(0), f"page{i}.html")
            self._get_html()
            main_logger.info(f"Собрано {i - 1} ссылок на профили (metalweb)")
        
    def _get_fabricators(self) -> None:
        for i in range(1, self._pages + 2):
            if self.soup != "error":
                content_list_div = self.soup.find("div", class_="content-list--padding")
                div_enterprise = content_list_div.find_all("div", class_="enterprise-teaser")

                for k in div_enterprise:
                    self._companies.append("https://fabricators.ru" + k.find("a")["href"])
                
            if i == 1:
                self._link += "?ysclid=m1kjzaqwyj637159448&page=1"
            else:
                self._link = self._link.replace(re.search(pattern=r"page=\d+$",
                                                          string=self._link).group(0), f"page={i}")
            self._get_html()
            main_logger.info(f"Собрано {i} ссылок на профили (fabricators)")
            sleep(0.2)
            
    
    def _get_oborudunion(self) -> None:
        for i in range(2, self._pages + 2):
            if self.soup != "error":
                company_names = self.soup.find_all("div", class_="company-name")

                for k in company_names:
                    if k.find("a") == None:
                        continue
                    self._companies.append("https://www.oborudunion.ru" + k.find("a")["href"])
                
            self._link = self._link.replace(re.search(pattern=r"PAGEN_1=\d+$",
                                                      string=self._link).group(0), f"PAGEN_1={i}")
            self._get_html()
            main_logger.info(f"Собрано {i - 1} ссылок на профили (oborudunion)")
            sleep(0.2)
    
    def _get_manufacturers(self) -> None:
        for i in range(1, self._pages + 2):
            if self.soup != "error":
                sim_titles = self.soup.find("div", class_="companies-list").find_all("div", class_="sim-title")

                for k in sim_titles:
                    self._companies.append("https://manufacturers.ru/" + k.find("a")["href"])
                
            if i == 1:
                self._link += "?page=1"
            else:
                self._link = self._link.replace(re.search(pattern=r"page=\d+$",
                                                          string=self._link).group(0), f"page={i}") 
            self._get_html()
            main_logger.info(f"Собрано {i} ссылок на профили (manufacturers)")
            sleep(0.2)

    def _get_orgpage(self) -> None:
        for i in range(1, self._pages + 2):
            if self.soup != "error":
                item_titles = self.soup.find("div", id="rubricator-result").find_all("div", class_="similar-item__title")

                for k in item_titles:
                    self._companies.append(k.find("a")["href"])
                
            if i == 1:
                self._link += "2/"
            else:
                self._link = self._link.replace(re.search(pattern=r"\d+\/$",
                                                          string=self._link).group(0), f"{i}/") 
            self._get_html()
            main_logger.info(f"Собрано {i} ссылок на профили (orgpage)")
            
    def _get_checko(self) -> None:
        for i in range(2, self._pages + 2):
            if self.soup != "error":
                links = self.soup.find("table", class_="data-table").find_all("a", class_="link")

            for k in links:
                self._companies.append("https://checko.ru" + k["href"])
        
            self._link = self._link.replace(re.search(pattern=r"page=\d+$",
                                                      string=self._link).group(0), f"page={i}")
            self._get_html()
            main_logger.info(f"Собрано {i - 1} ссылок на профили (checko)")
    
    def _get_kemcsm(self)-> None:
        for i in range(1, self._pages + 2):
            if self.soup != "error":
                factory_heads = self.soup.find("div", class_="factory-wrap").find_all("div", class_="factory__head")

                for k in factory_heads:
                    self._companies.append("https://kemcsm.ru" + k.find("a")["href"])
                
            if i == 1:
                self._link += "?page=1"
            else:
                self._link = self._link.replace(re.search(pattern=r"page=\d+$",
                                                          string=self._link).group(0), f"page={i}")
            self._get_html()
            main_logger.info(f"Собрано {i} ссылок на профили (kemcsm)")

    def _get_wiki_prom(self) -> None:
        for i in range(2, self._pages + 2):
            if self.soup != "error":
                titles = self.soup.find("div", class_="list-block").find_all("div", class_="title")

                for k in titles:
                    self._companies.append(k.find("a")["href"])
            
            if i == 2:
                self._link = self._link[0:28] + "/page2/" + "mashinostroitelnye-zavody.html"
            else:
                self._link = self._link.replace(re.search(pattern=r"page\d+",
                                                          string=self._link).group(0), f"page{i}")
            self._get_html()
            main_logger.info(f"Собрано {i - 1} ссылок на профили (wiki-prom)")

    def get_info(self) -> list:
        PATHS = {
            "steel-fabrication.ru": self._get_steel_fabrication,
            "www.metalweb.ru": self._get_metalweb,
            "fabricators.ru": self._get_fabricators,
            "www.oborudunion.ru": self._get_oborudunion,
            "manufacturers.ru": self._get_manufacturers,
            "www.orgpage.ru": self._get_orgpage,
            "checko.ru": self._get_checko,
            "kemcsm.ru": self._get_kemcsm,
            "www.wiki-prom.ru": self._get_wiki_prom
            }
        
        PATHS[self._domain]()
        return self._companies
    