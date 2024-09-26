import re
import requests

from typing import Union

class Companies:

    def __init__(self, link: str) -> None:
        self.link = link
        self.domain = re.search(pattern=r".*(\.ru|\.com)", string=link[8:])
        self.get_html()
    
    def get_html(self) -> Union[None | str]:

        response = requests.get(url=self.link)
        code = response.status_code

        if code >= 200 and code < 400:
            with open("index.html", "w", encoding="utf-8") as file:
                file.writelines(response.text)
        else:
            return "error"
    
    # def get_steel_fabrication(self):














# c = Companies("https://steel-fabrication.ru/?arrFilter2_ff%5BNAME%5D=&arrFilter2_pf%5BLOCATION%5D%5B0%5D=195&arrFilter2_pf%5BLOCATION%5D%5B1%5D=191&arrFilter2_pf%5BLOCATION%5D%5B2%5D=194&arrFilter2_pf%5BLOCATION%5D%5B3%5D=193&set_filter=Y&PAGEN_6=100")
# c.get_html()