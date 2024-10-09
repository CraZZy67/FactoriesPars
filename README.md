# Парсер компаний с нескольких сайтов каталогов

## Описание

Парсер создан для сбора информации о компаниях и добавления их данных в excel файл.

Парсер собирает данные с указанных сайтов каталогов, проверяет данные на совпадение и добавляет данные в образце: имя; номер; сайт; почта. Сайты собраны с разных поисковых систем.

В папке data создается excel файл.

## Под капотом

Парсер состоит из трех основных классов и data класса.

Первый класс специализируется на парсинге ссылок на профиля компаний из разных каталогов. Второй дочерний класс собирает все ссылки профилей и парсит с них данные о компаниях. Третий независимый класс записывает все в excel файл, в этом классе и создается экземпляр парсера который запускает всю программу.

Data класс в свою очередь нужен для хранения переменных настроек.

Так же в программе реализуется логирование и тесты двух классов.

## Запуск

Для запуска хватает создать excel файл в папке data с базовой страницей и запустить main файл. После нужно будет подождать парсинга всех данных и надпись о успешном завершении, после всего этого открыть excel файл.

Все зависимости проекта находятся в файле requirements.txt
