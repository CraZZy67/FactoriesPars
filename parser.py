import pandas as pd

from companies_info import CompaniesInfo

import re
import json

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
                    data = {"name": [filtered_data[0]], "number": [filtered_data[1]], "web_site": [filtered_data[2]]}
                    existing_data = pd.DataFrame(data)
                
                    with pd.ExcelWriter("data/data_companies.xlsx", mode='w', engine='openpyxl') as writer:
                        existing_data.to_excel(writer, sheet_name=sheet, index=False)
                
                elif not self.check_repeat(data=filtered_data, data_frame=data):
                    data["name"].append(filtered_data[0])
                    data["number"].append(filtered_data[1])
                    data["web_site"].append(filtered_data[2])

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

        if len(data) == 3:
            filtered_data_two.append(filtered_data_one[0])
            filtered_data_two.append(filtered_data_one[1])
            return filtered_data_two

        if len(data) > 3:
            for k in filtered_data_one:
                if re.search(pattern=r"^\+?\d?\(?\d+", string=k) != None:
                    filtered_data_two.append(k)
                    break

            for k in filtered_data_one:
                if re.search(pattern=r"^\+?\d?\(?\d+", string=k) == None:
                    filtered_data_two.append(k)
                    break 
            
            if len(filtered_data_two) == 2:
                if "http" in filtered_data_two[1]:
                    filtered_data_two.insert(1, "None")
                else:
                    filtered_data_two.insert(2, "None")

        elif len(data) == 2:
            if "http" in filtered_data_one[0]:
                filtered_data_two.append("None")
                filtered_data_two.append(filtered_data_one[0])
            else:
                filtered_data_two.append(filtered_data_one[0])
                filtered_data_two.append("None")
        else:
            filtered_data_two.append("None")
            filtered_data_two.append("None")
                
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


header_kemcsm = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
header_fabricators = {"cookie": "_ym_uid=17273380524345500; _ym_d=1727338052; beget=begetok; SSESS0cfa4c8e8012789cd8880c3e327e70ba=Vs8iyoD3HvOcmJ4lSSXxd82F0lPba8WWLjwEOd6jubM; _ym_isad=1; _ym_visorc=w"}
header_manufacturers = {"cookie": "beget=begetok; _ym_uid=1727343216296996738; _ym_d=1727343216; _ym_isad=1; _ym_visorc=w"}

headers = { "topic_1": [None, None, header_fabricators, None, header_manufacturers],
            "topic_2": [header_fabricators, None, None, None],
            "topic_3": [header_manufacturers, header_manufacturers, header_manufacturers, None, header_kemcsm, None, header_fabricators]
            }

pages = {"topic_1": [10, 28, 119, 111, 33],
         "topic_2": [9, 60, 3, 3],
         "topic_3": [1, 52, 257, 3, 14, 3, 120]}

with open('data/sites.json', 'r') as file:
    links = json.load(file)

parser = Parser(links=links, pages=pages, headers=headers)
parser.get_excel(topic="topic_1", sheet="Metal")