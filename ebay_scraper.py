from Driver import Driver
from selenium.common import exceptions
# from Colors import bcolors as color
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
import os
import csv


class EbayScraper:
    def __init__(self, driver):
        self.select_variations = []
        self.images_to_download = []
        self.driver = driver
        self.base_price = self.driver.find_element_by_xpath('//span[@itemprop="price"]').text
        self.title = self.driver.find_element_by_id('itemTitle').text
        self.shipping = self.driver.find_element_by_id('fshippingCost').text
        self.details = self.driver.find_element_by_id('viTabs_0_is').text
        self.seller = self.driver.find_element_by_xpath("//div[@class='bdg-90']/div/a/span").text
        self.writer=self.spreadsheet()


    def spreadsheet(self,filename='Mother.csv'):
        if not os.path.exists("Output"):
            os.mkdir("Output")
        sheet = open("Output/" + filename, "w+", encoding="utf-8")
        csv_writer = csv.writer(sheet)
        return csv_writer


    def get_info(self):
        print("\n\n")
        print("----------Information Extracted-------------")
        print("TITLE:" + self.title)
        print("BASE PRICE:" + self.base_price)
        print("SELLER: "+self.seller)
        print("-----------sizes-available-------------")
        self.prepare_variations()

        # Uncomment  lines below after completion

        # print("\n")
        # print("Shipping:"+self.shipping)
        # print("----------IMAGES------\n")
        # self.get_images()
        # print("-------OTHER DETAILS------------")
        # print("DETAILS\n")
        # print(self.details)

    def get_price(self):
        return self.driver.find_element_by_xpath('//span[@itemprop="price"]').text

    def get_images(self):
        images = self.driver.find_elements_by_xpath('//div[@id="vi_main_img_fs"]//img')
        # description_images=self.driver.find_elements_by_xpath('//div[@class="box-images-details"]//img')
        for image in images:
            self.images_to_download.append(image.get_attribute('src'))
            print(image.get_attribute('src'))

    def get_number_of_variation(self):
        i = 1
        try:
            while True:
                dynamic_xpath = "//select[@id='msku-sel-" + str(i) + "']"
                mksu_select = self.driver.find_element_by_xpath(dynamic_xpath)
                self.select_variations.append(mksu_select)
                i += 1
        except exceptions.NoSuchElementException:
            pass
        finally:
            return

    def recursive_enumeration(self,information, depth):
        data = information[depth]
        if(len(information)>(depth+1)):
            print("HERE")
            depth=depth+1
            for info in data[1]:
                print("\t" +data[2] +":"+info)
                try:
                    self.current_recursive_item=info
                    data[0].select_by_visible_text(info)
                    self.recursive_enumeration(information,depth)
                except exceptions.NoSuchElementException:
                    pass
        elif(len(information)==(depth+1)):
            data=information[depth]
            for info in data[1]:
                try:
                    data[0].select_by_visible_text(info)
                    print("\t\t"+data[2]+info+"Price :"+self.get_price())
                    self.writer.writerow(["URL",self.title,self.seller,self.current_recursive_item,info,self.get_price()])
                except exceptions.NoSuchElementException:
                    pass
        else:
            print("No variations Found")



    def prepare_variations(self):
        self.get_number_of_variation()
        variation_list = []
        for var in self.select_variations:
            name = (var.get_attribute("name"))
            drp_down = Select(self.driver.find_element_by_name(name))
            enabled_values = []
            for values in drp_down.options[1:]:
                if values.get_attribute('disabled'):
                    continue
                enabled_values.append(values.text)
            variation_list.append([drp_down, enabled_values, name])
        self.recursive_enumeration(variation_list,0)

if __name__ == '__main__':
    scraper = Driver()
    error_list = open("error_url.txt", "a+")
    with open("ebayurllist.txt") as links:
        urls = links.readlines()
        for url in urls:
            try:
                print("\n\n---------------STARTING TO SCRAPE-------------")
                print("URL:" + url)
                scraper.loadurl(url)
                ebay_object = EbayScraper(scraper.driver)
                ebay_object.get_info()
            except:
                raise
                error_list.write(url)
                print(color.FAIL + "This URL WAS UNSUCESSFUL" + color.ENDC)
            finally:
                print("---------------------END OF SCRAPE---------------")
    scraper.terminate()
