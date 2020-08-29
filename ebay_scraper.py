from Driver import Driver

class EbayScraper():
    def __init__(self,driver):
        self.driver=driver
        self.base_price=self.driver.find_element_by_id('prcIsum').text
        self.title=self.driver.find_element_by_id('itemTitle').text
        self.shipping=self.driver.find_element_by_id('fshippingCost').text
        self.details=self.driver.find_element_by_id('viTabs_0_is').text



    def print_info(self):
        print("TITLE:"+self.title)
        print("PRICE:"+self.base_price)
        print("Shipping:"+self.shipping)
        print("DETAILS\n")
        print(self.details)




if __name__ == '__main__':
    scraper=Driver()
    url = "https://www.ebay.com.au/itm/adidas-AU-Men-Broma-Shoes/402289629493?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3Dbefe5eb0fcbe47cba44d0c6922427643%26pid%3D100970%26rk%3D4%26rkt%3D8%26mehot%3Dnone%26sd%3D323540595944%26itm%3D402289629493%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3Dadidas&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3A8250fb12-ea06-11ea-98b5-36db824a1e63%7Cparentrq%3A3aafaff11740a4d6ad986a38ffffd302%7Ciid%3A1"
    scraper.loadurl(url)
    ebay_object = EbayScraper(scraper.driver)
    ebay_object.print_info()
    scraper.terminate()

