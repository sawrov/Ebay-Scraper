from Driver import Driver
from Colors import bcolors as color
from selenium.webdriver.support.ui import Select

class EbayScraper():
    def __init__(self,driver):
        self.images_to_download=[]
        self.driver=driver
        self.base_price=self.driver.find_element_by_id('prcIsum').text
        self.title=self.driver.find_element_by_id('itemTitle').text
        self.shipping=self.driver.find_element_by_id('fshippingCost').text
        self.details=self.driver.find_element_by_id('viTabs_0_is').text

    def get_info(self):
        print("\n\n")
        print("----------Information Extracted-------------")
        print("TITLE:"+self.title)
        print("PRICE:"+self.base_price)
        print("-----------sizes-available-------------")
        self.get_variation()
        print("\n")
        print("Shipping:"+self.shipping)
        print("----------IMAGES------\n")
        self.get_images()
        print("-------OTHER DETAILS------------")
        print("DETAILS\n")
        print(self.details)

    def get_images(self):
        images=self.driver.find_elements_by_xpath('//div[@id="vi_main_img_fs"]//img')
        # description_images=self.driver.find_elements_by_xpath('//div[@class="box-images-details"]//img')
        for image in images:
            self.images_to_download.append(image.get_attribute('src'))
            print(image.get_attribute('src'))

    def get_variation(self):
        selector=self.driver.find_elements_by_xpath('//div[@id="test12"]//option')
        select=Select(self.driver.find_element_by_xpath('//select[@id="msku-sel-1"]'))
        available=[]
        for selection in selector[1:]:
            # print(selection.text)
            if selection.get_attribute('disabled'):
                continue
            available.append(selection.text)
        for item in available:
            select.select_by_visible_text(item)

if __name__ == '__main__':
    scraper = Driver()
    error_list=open("error_url.txt","a+")
    with open("ebayurllist.txt") as links:
        urls=links.readlines()
        for url in urls:
            try:
                print("\n\n---------------STARTING TO SCRAPE-------------")
                print("URL:"+url)
                scraper.loadurl(url)
                ebay_object = EbayScraper(scraper.driver)
                ebay_object.get_info()
            except:
                raise
                error_list.write(url)
                print(color.FAIL+ "This URL WAS UNSUCESSFUL" + color.ENDC)
            finally:
                print("---------------------END OF SCRAPE---------------")
    scraper.terminate()


