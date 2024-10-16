import pandas as pd

from src.loggers import main_logger
from src.companies_info import CompaniesInfo

import re

class Parser:

    def __init__(self, links: dict, pages: dict, headers: dict) -> None:
        self.links = links
        self.pages = pages
        self.headers = headers

    def get_excel(self, topic: str, sheet: str) -> None:
        for i, k in enumerate(self.links[topic]):
            info = CompaniesInfo(link=k, pages=self.pages[topic][i], headers=self.headers[topic][i]).get_info()

            for v, j in enumerate(info.values()):
                filtered_data = self.filtering_data(j)

                if i == 0 and v == 0:
                    data = {"name": [filtered_data[0]], "number": [filtered_data[1]], "web_site": [filtered_data[2]], "mail": [filtered_data[3]]}
                    existing_data = pd.DataFrame(data)
                
                    with pd.ExcelWriter("data/data_companies.xlsx", mode='a', engine='openpyxl') as writer:
                        existing_data.to_excel(writer, sheet_name=sheet, index=False)
                
                elif not self.check_repeat(data=filtered_data, data_frame=data):
                    data["name"].append(filtered_data[0])
                    data["number"].append(filtered_data[1])
                    data["web_site"].append(filtered_data[2])
                    data["mail"].append(filtered_data[3])
                main_logger.info(f"Запись в excel файл данных ({v})")

        new_data_frame = pd.DataFrame(data)
        with pd.ExcelWriter("data/data_companies.xlsx", mode='a', engine='openpyxl', if_sheet_exists="overlay") as writer:
            new_data_frame.to_excel(writer, sheet_name=sheet, index=False)

    @staticmethod
    def filtering_data(data: list) -> list:
        filtered_data_one = list()
        filtered_data_two = list()

        for k in data[1:]:
            filtered_data_one.append(k.replace(" ", "").replace("\n", ""))

        filtered_data_two.append(data[0])

        for k in filtered_data_one:
            if re.search(pattern=r"^\+?\d?\(?\d+", string=k) != None:
                filtered_data_two.append(k)
                break

        for k in filtered_data_one:
            if re.search(pattern=r"^[a-zA-Z]+", string=k) != None and "@" not in k:
                filtered_data_two.append(k)
                break

        for k in filtered_data_one:
            if "@" in k:
                filtered_data_two.append(k)
                break

        if len(filtered_data_two) == 2:
            if "http" in filtered_data_two[1]:
                filtered_data_two.insert(1, "None")
                filtered_data_two.insert(3, "None")
            elif "@" in filtered_data_two[1]:
                filtered_data_two.insert(1, "None")
                filtered_data_two.insert(2, "None")
            else:
                filtered_data_two.insert(2, "None")
                filtered_data_two.insert(3, "None")

        elif len(filtered_data_two) == 3:
            if "http" in filtered_data_two[1]:
                filtered_data_two.insert(1, "None")
            elif "@" in filtered_data_two[2]:
                filtered_data_two.insert(2, "None")
            else:
                filtered_data_two.insert(3, "None")

        elif len(filtered_data_two) == 1:
            filtered_data_two.insert(1, "None")
            filtered_data_two.insert(2, "None")
            filtered_data_two.insert(3, "None")
                
        return filtered_data_two
        
    @staticmethod
    def check_repeat(data: list, data_frame: dict) -> bool:
        for i in data_frame["name"]:
            if data[0] == i:
                return True
            
        for i in data_frame["number"]:
            if data[1] != None:
                if data[1] == i:
                   return True
        
        for i in data_frame["web_site"]:
            if data[2] != None:
                if data[2] == i:
                   return True 
        return False
