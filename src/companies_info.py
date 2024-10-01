from src.site_links import Site

from time import sleep


class CompaniesInfo(Site):

    def __init__(self, link: str, pages: int, headers: dict = None) -> None:
        super().__init__(link, pages, headers)

        self._info = dict()

    def _get_steel_fabrication(self) -> None:
        super()._get_steel_fabrication()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                main_div = self.soup.find("div", class_="right-p")
                self._info[i] = [main_div.find("h1").text]

                all_p = main_div.find("div", class_="line-1").find_all("p")
                for v in all_p:
                    if "Телефон:" in v.text:
                        self._info[i].append(v.text[9:])
                    elif "Сайт:" in v.text:
                        self._info[i].append(v.text[6:])
                    
    def _get_metalweb(self) -> None:
        super()._get_metalweb()
        
        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]
                
                table = self.soup.find("table", class_="table table-striped")
                phone = table.find("a", class_="btn btn-success")
                site = table.find("a", attrs={"itemprop": "url"})

                if phone != None:
                    self._info[i].append(phone["href"][4:])
                if site != None:
                    self._info[i].append(site["href"])
            if i > 100:
                break
               
    def _get_fabricators(self) -> None:
        super()._get_fabricators()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]

                section = self.soup.find("div", id="section-st-block5")
                contact_list = section.find("div", class_="content-contact-list")
                a_links = contact_list.find_all("a")

                for v in a_links:
                    if "tel:" in v["href"]:
                        self._info[i].insert(1, v["href"][4:])
                    elif "http" in v["href"]:
                        self._info[i].append(v["href"])
            if i > 100:
                break
    
    def _get_oborudunion(self) -> None:
        super()._get_oborudunion()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                aside = self.soup.find("aside")
                self._info[i] = [aside.find("h3").text]

                phone_list = aside.find("ul", class_="c-phone-list")
                if phone_list != None:
                    self._info[i].append(phone_list.find("a")["href"][4:])
            
                site_list = aside.find("ul", class_="c-site-list")
                if site_list != None:
                    self._info[i].append(site_list.find("a")["href"])
            if i > 100:
                break
            sleep(0.2)
    
    def _get_manufacturers(self) -> None:
        super()._get_manufacturers()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]

                cont_body = self.soup.find("tbody", class_="cont-tbody")
                all_a = cont_body.find_all("a")

                for v in all_a:
                    if "tel:" in v["href"]:
                        self._info[i].insert(1, v["href"][4:])
                    elif "http" in v["href"]:
                        self._info[i].append(v["href"])
            if i > 100:
                break
            sleep(0.2)
    
    def _get_orgpage(self) -> None:
        super()._get_orgpage()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text.replace(" ", "").replace("\n", "")]

                company_information = self.soup.find("ul", class_="company-information__phone-list")
                li = company_information.find_all("li")
                phone = li[0].find("span", class_="company-information__phone")
                if phone != None:
                    self._info[i].append(phone.text)

                div_inf = self.soup.find("div", class_="company-information__site-text")
                if div_inf != None:
                    site = div_inf.find("a", class_="nofol-link")
                    if site != None:
                        self._info[i].append(site["href"])
  
    def _get_checko(self) -> None:
        super()._get_checko()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]

                div = self.soup.find("div", class_="uk-width-1 uk-width-1-3@m")
                if div != None:
                    all_a = div.find_all("a")
                    if all_a != None and len(all_a) != 0:
                        self._info[i].append(all_a[0].text)
                
                main_div = self.soup.find("div", class_="uk-grid-divider mt-5")
                if main_div != None:
                    a_link = main_div.find("a", attrs={"rel": "nofollow noopener"})
                    if a_link != None:
                        self._info[i].append(a_link["href"])

    def _get_kemcsm(self)-> None:
        super()._get_kemcsm()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]

                contact_company = self.soup.find("div", id="contact-company")
                all_li = contact_company.find_all("li")
                phone = all_li[1].find("a")
                if phone != None:
                    self._info[i].append(phone["href"][4:])
                
                site = self.soup.find("a", attrs={"target": "_blank"})
                if site != None:
                    self._info[i].append(site.text)

    def _get_wiki_prom(self) -> None:
        super()._get_wiki_prom()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            if self.soup != "error":
                self._info[i] = [self.soup.find("h1").text]

                site = self.soup.find("a", attrs={"target": "_blank"})
                if site != None:
                    self._info[i].append(site["href"])
    
    def get_info(self) -> dict:
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
        return self._info