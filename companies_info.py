from site_cls import Site

from time import sleep


class CompaniesInfo(Site):

    def __init__(self, link: str, pages: int, headers: dict = None) -> None:
        super().__init__(link, pages, headers)

        self.info = dict()

    def _get_steel_fabrication(self) -> None:
        super()._get_steel_fabrication()

        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            main_div = self.soup.find("div", class_="right-p")
            self.info[i] = [main_div.find("h1").text]

            all_p = main_div.find("div", class_="line-1").find_all("p")
            for v in all_p:
                if "Телефон:" in v.text:
                    self.info[i].append(v.text[9:])
                elif "Сайт:" in v.text:
                    self.info[i].append(v.text[6:])
                    
    def _get_metalweb(self) -> None:
        super()._get_metalweb()
        
        for i, k in enumerate(self._companies, start=1):
            self._link = k
            super()._get_html()

            self.info[i] = [self.soup.find("h1").text]
            
            table = self.soup.find("table", class_="table table-striped")
            phone = table.find("a", class_="btn btn-success")
            site = table.find("a", attrs={"itemprop": "url"})

            if phone != None:
                self.info[i].append(phone["href"])
            if site != None:
                self.info[i].append(site["href"])
            if i > 100:
                break
            

             
    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()
    
    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()
    
    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()
    
    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()
    
    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()

    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()

    # def _get_steel_fabrication(self) -> None:
    #     for i in super()._companies:
    #         self._link = i
    #         super()._get_html()



exam = CompaniesInfo("https://www.metalweb.ru/catalog7/okrug1058/page1.html", pages=28)
exam._get_metalweb()

for i, k in exam.info.items():
    print(f"{i} - {k}")