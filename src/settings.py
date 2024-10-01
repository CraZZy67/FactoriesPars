from dataclasses import dataclass
import os
import json


@dataclass(frozen=True, init=False)
class Settings:
    HEADER_KEMCSM = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
    HEADER_FABRICATORS = {"cookie": "_ym_uid=17273380524345500; _ym_d=1727338052; beget=begetok; SSESS0cfa4c8e8012789cd8880c3e327e70ba=Vs8iyoD3HvOcmJ4lSSXxd82F0lPba8WWLjwEOd6jubM; _ym_isad=1; _ym_visorc=w"}
    HEADER_MANUFACTURERS = {"cookie": "beget=begetok; _ym_uid=1727343216296996738; _ym_d=1727343216; _ym_isad=1; _ym_visorc=w"}

    HEADERS = { "topic_1": [None, None, HEADER_FABRICATORS, None, HEADER_MANUFACTURERS],
                "topic_2": [HEADER_FABRICATORS, None, None, None],
                "topic_3": [HEADER_MANUFACTURERS, HEADER_MANUFACTURERS, HEADER_MANUFACTURERS, None, HEADER_KEMCSM, None, HEADER_FABRICATORS]
                }
    
    PAGES = {"topic_1": [10, 28, 119, 111, 33],
             "topic_2": [9, 60, 3, 3],
             "topic_3": [1, 52, 257, 3, 14, 3, 120]}
    
    with open('data/sites.json', 'r') as file:
        LINKS = json.load(file)

settings1 = Settings()
