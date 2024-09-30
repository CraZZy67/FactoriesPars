import unittest
from companies_info import CompaniesInfo

class TestCompanies(unittest.TestCase):
    def setUp(self):
        self.ste_fabric_exam = CompaniesInfo("https://steel-fabrication.ru/?arrFilter2_ff%5BNAME%5D=&arrFilter2_pf%5BLOCATION%5D%5B0%5D=195&arrFilter2_pf%5BLOCATION%5D%5B1%5D=191&arrFilter2_pf%5BLOCATION%5D%5B2%5D=194&arrFilter2_pf%5BLOCATION%5D%5B3%5D=193&set_filter=Y&PAGEN_6=1", pages=10)

        self.metalweb = CompaniesInfo("https://www.metalweb.ru/catalog7/okrug1058/page1.html", pages=28)
        self.orgpage = CompaniesInfo("https://www.orgpage.ru/rossiya/elektroenergetika0/", pages=3)
        self.checko = CompaniesInfo("https://checko.ru/company/select?code=422230&page=1", pages=3)
        self.wiki_prom = CompaniesInfo("https://www.wiki-prom.ru/169/mashinostroitelnye-zavody.html", pages=3)

        headers_kemcsm = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
        self.kemcsm = CompaniesInfo("https://kemcsm.ru/factories/mashinostroitelnye-zavody", pages=14, headers=headers_kemcsm)

        self.oborudunion_1 = CompaniesInfo("https://www.oborudunion.ru/company/metalloobrabatyvayuschee-oborudovanie?PAGEN_1=1", pages=111)
        self.oborudunion_2 = CompaniesInfo("https://www.oborudunion.ru/company/energeticheskoe-oborudovanie?PAGEN_1=1", pages=60)
        self.oborudunion_3 = CompaniesInfo("https://www.oborudunion.ru/russia/company/mashinostroenie?PAGEN_1=1", pages=3)
        
        headers_fabricators = {"cookie": "_ym_uid=17273380524345500; _ym_d=1727338052; beget=begetok; SSESS0cfa4c8e8012789cd8880c3e327e70ba=Vs8iyoD3HvOcmJ4lSSXxd82F0lPba8WWLjwEOd6jubM; _ym_isad=1; _ym_visorc=w"}
        self.fabricators_1 = CompaniesInfo("https://fabricators.ru/proizvodstvo/zavody-metallokonstrukciy", pages=119, headers=headers_fabricators)
        self.fabricators_2 = CompaniesInfo("https://fabricators.ru/produkt/transformatorypodstancii", pages=9, headers=headers_fabricators)
        self.fabricators_3 = CompaniesInfo("https://fabricators.ru/proizvodstvo/mashinostroitelnye-zavody", pages=120, headers=headers_fabricators)

        headers_manufacturers = {"cookie": "beget=begetok; _ym_uid=1727343216296996738; _ym_d=1727343216; _ym_isad=1; _ym_visorc=w"}
        self.manufacturers_1 = CompaniesInfo("https://manufacturers.ru/companies/proizvodstvo-metallokonstrukciy", pages=33, headers=headers_manufacturers)
        self.manufacturers_2 = CompaniesInfo("https://manufacturers.ru/companies/tyazheloe-mashinostroenie?rn=6191", pages=1, headers=headers_manufacturers)
        self.manufacturers_3 = CompaniesInfo("https://manufacturers.ru/companies/tyazheloe-mashinostroenie", pages=52, headers=headers_manufacturers)
        self.manufacturers_4 = CompaniesInfo("https://manufacturers.ru/companies/mashinostroenie", pages=257, headers=headers_manufacturers)

    def test_steel(self):
        result = self.ste_fabric_exam.get_info()

        self.assertTrue(len(result) >= 45)
    
    def test_metalweb(self):
        result = self.metalweb.get_info()

        self.assertTrue(len(result) >= 99)
    
    def test_orgpage(self):
        result = self.orgpage.get_info()

        self.assertTrue(len(result) >= 10)
    
    def test_checko(self):
        result = self.checko.get_info()

        self.assertTrue(len(result) >= 10)
    
    def test_kemcsm(self):
        result = self.kemcsm.get_info()

        self.assertTrue(len(result) >= 50)
    
    def test_wiki_prom(self):
        result = self.wiki_prom.get_info()

        self.assertTrue(len(result) >= 10)
    
    def test_oborudunion_1(self):
        result = self.oborudunion_1.get_info()

        self.assertTrue(len(result) >= 99)
    
    def test_oborudunion_2(self):
        result = self.oborudunion_2.get_info()

        self.assertTrue(len(result) >= 99)

    def test_oborudunion_3(self):
        result = self.oborudunion_3.get_info()

        self.assertTrue(len(result) >= 10)

    def test_fabricators_1(self):
        result = self.fabricators_1.get_info()
        
        self.assertTrue(len(result) >= 99)

    def test_fabricators_2(self):
        result = self.fabricators_2.get_info()

        self.assertTrue(len(result) >= 50)

    def test_fabricators_3(self):
        result = self.fabricators_3.get_info()

        self.assertTrue(len(result) >= 99)

    def test_manufacturers_1(self):
        result = self.manufacturers_1.get_info()

        self.assertTrue(len(result) >= 99)

    def test_manufacturers_2(self):
        result = self.manufacturers_2.get_info()

        self.assertTrue(len(result) >= 5)

    def test_manufacturers_3(self):
        result = self.manufacturers_3.get_info()

        self.assertTrue(len(result) >= 99)

    def test_manufacturers_4(self):
        result = self.manufacturers_4.get_info()

        self.assertTrue(len(result) >= 99)

if __name__ == "__main__":
  unittest.main()