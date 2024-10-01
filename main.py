from src.parser import Parser
from src.settings import settings1


if __name__ == "__main__":
    parsing_companies = Parser(links=settings1.LINKS, pages=settings1.PAGES, headers=settings1.HEADERS)

    parsing_companies.get_excel("topic_1", sheet="Metal")
    # parsing_companies.get_excel("topic_2", sheet="Energy")
    # parsing_companies.get_excel("topic_3", sheet="Mashin")