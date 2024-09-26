from bs4 import BeautifulSoup
import requests

import re
from typing import Union

class Companies:

    def __init__(self, link: str, pages: int) -> None:
        self.link = link
        self.pages = pages
        self.companies = list()
        self.domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:])
        

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

            self.link = self.link[0:-1] + str(i)
            self.get_html()
            













# c = Companies("https://steel-fabrication.ru/?arrFilter2_ff%5BNAME%5D=&arrFilter2_pf%5BLOCATION%5D%5B0%5D=195&arrFilter2_pf%5BLOCATION%5D%5B1%5D=191&arrFilter2_pf%5BLOCATION%5D%5B2%5D=194&arrFilter2_pf%5BLOCATION%5D%5B3%5D=193&set_filter=Y&PAGEN_6=1", pages=10)
# c.get_steel_fabrication()