import unittest
from src.site_links import Site

class TestCompanies(unittest.TestCase):
    def setUp(self):
        self.ste_fabric_exam = Site("https://steel-fabrication.ru/?arrFilter2_ff%5BNAME%5D=&arrFilter2_pf%5BLOCATION%5D%5B0%5D=195&arrFilter2_pf%5BLOCATION%5D%5B1%5D=191&arrFilter2_pf%5BLOCATION%5D%5B2%5D=194&arrFilter2_pf%5BLOCATION%5D%5B3%5D=193&set_filter=Y&PAGEN_6=1", pages=10)

        self.metalweb = Site("https://www.metalweb.ru/catalog7/okrug1058/page1.html", pages=28)
        self.orgpage = Site("https://www.orgpage.ru/rossiya/elektroenergetika0/", pages=3)
        self.checko = Site("https://checko.ru/company/select?code=422230&page=1", pages=3)
        self.wiki_prom = Site("https://www.wiki-prom.ru/169/mashinostroitelnye-zavody.html", pages=3)

        headers_kemcsm = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
        self.kemcsm = Site("https://kemcsm.ru/factories/mashinostroitelnye-zavody", pages=14, headers=headers_kemcsm)

        self.oborudunion_1 = Site("https://www.oborudunion.ru/company/metalloobrabatyvayuschee-oborudovanie?PAGEN_1=1", pages=111)
        self.oborudunion_2 = Site("https://www.oborudunion.ru/company/energeticheskoe-oborudovanie?PAGEN_1=1", pages=60)
        self.oborudunion_3 = Site("https://www.oborudunion.ru/russia/company/mashinostroenie?PAGEN_1=1", pages=3)
        
        headers_fabricators = {"cookie": "_ym_uid=17273380524345500; _ym_d=1727338052; beget=begetok; SSESS0cfa4c8e8012789cd8880c3e327e70ba=Vs8iyoD3HvOcmJ4lSSXxd82F0lPba8WWLjwEOd6jubM; _ym_isad=1; _ym_visorc=w"}
        self.fabricators_1 = Site("https://fabricators.ru/proizvodstvo/zavody-metallokonstrukciy", pages=119, headers=headers_fabricators)
        self.fabricators_2 = Site("https://fabricators.ru/produkt/transformatorypodstancii", pages=9, headers=headers_fabricators)
        self.fabricators_3 = Site("https://fabricators.ru/proizvodstvo/mashinostroitelnye-zavody", pages=120, headers=headers_fabricators)

        headers_manufacturers = {"cookie": "beget=begetok; _ym_uid=1727343216296996738; _ym_d=1727343216; _ym_isad=1; _ym_visorc=w"}
        self.manufacturers_1 = Site("https://manufacturers.ru/companies/proizvodstvo-metallokonstrukciy", pages=33, headers=headers_manufacturers)
        self.manufacturers_2 = Site("https://manufacturers.ru/companies/tyazheloe-mashinostroenie?rn=6191", pages=1, headers=headers_manufacturers)
        self.manufacturers_3 = Site("https://manufacturers.ru/companies/tyazheloe-mashinostroenie", pages=52, headers=headers_manufacturers)
        self.manufacturers_4 = Site("https://manufacturers.ru/companies/mashinostroenie", pages=257, headers=headers_manufacturers)

    def test_steel(self):
        last_link = "https://steel-fabrication.ru/catalog-manufacturers/catalog/yuzhnouralskiy-yuzmkm/"
        result = self.ste_fabric_exam.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_metalweb(self):
        last_link = "https://irkutsk.metalweb.ru/catalog/all/resource1104.html"
        result = self.metalweb.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_orgpage(self):
        last_link = "https://www.orgpage.ru/vyiborg/kaskad-1-442503.html"
        result = self.orgpage.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_checko(self):
        last_link = "https://checko.ru/company/rif-1123926058761"
        result = self.checko.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_kemcsm(self):
        last_link = "https://kemcsm.ru/factory/midiel"
        result = self.kemcsm.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_wiki_prom(self):
        last_link = "https://www.wiki-prom.ru/6758zavod.html"
        result = self.wiki_prom.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_oborudunion_1(self):
        last_link = "https://www.oborudunion.ru/company/3088974/"
        result = self.oborudunion_1.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)
    
    def test_oborudunion_2(self):
        last_link = "https://www.oborudunion.ru/company/2035837/"
        result = self.oborudunion_2.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_oborudunion_3(self):
        last_link = "https://www.oborudunion.ru/company/3091415/"
        result = self.oborudunion_3.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_fabricators_1(self):
        last_link = "https://fabricators.ru/proizvoditel/veyn"
        result = self.fabricators_1.get_info()
        
        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_fabricators_2(self):
        last_link = "https://fabricators.ru/proizvoditel/chetz"
        result = self.fabricators_2.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_fabricators_3(self):
        last_link = "https://fabricators.ru/proizvoditel/ooo-kompaniya-partner"
        result = self.fabricators_3.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_manufacturers_1(self):
        last_link = "https://manufacturers.ru//company/asmu-stalkonstrukciya"
        result = self.manufacturers_1.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_manufacturers_2(self):
        last_link = "https://manufacturers.ru//company/zavod-imeni-m-tarasova"
        result = self.manufacturers_2.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_manufacturers_3(self):
        last_link = "https://manufacturers.ru//company/abatek"
        result = self.manufacturers_3.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

    def test_manufacturers_4(self):
        last_link = "https://manufacturers.ru//company/liga-proektov"
        result = self.manufacturers_4.get_info()

        self.assertIsInstance(list(), type(result))
        self.assertIn(last_link, result)

if __name__ == "__main__":
  unittest.main()