from src.parser import Parser
from src.settings import settings1
from src.loggers import main_logger


if __name__ == "__main__":
    parsing_companies = Parser(links=settings1.LINKS, pages=settings1.PAGES, headers=settings1.HEADERS)

    main_logger.info("Начало выполнения программы!")

    parsing_companies.get_excel("topic_1", sheet="Metal")
    parsing_companies.get_excel("topic_2", sheet="Energy")
    parsing_companies.get_excel("topic_3", sheet="Mashin")

    main_logger.info("Программа успешно выполнена! В папке 'data' файл excel с данными.")