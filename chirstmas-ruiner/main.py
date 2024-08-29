from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#copyright @hydrosoftworks                                                                                


#datavars

database = {
    'bestbuy (recomended)',
    'walmart' ,
    'newegg',
    'amazon  (recomended)',
    'ebay',
    'facebook marketplace'
}

#title
title = "ps5 bot by elytra@vermillion"
guide = "with dev tool get the xpath of the checkout and the ad to cart buttons"
print(title)
print(guide)


#user input enter xpath url and second xpath
grablink = input("product name:  ")
xpath1 = input("enter cart xpath: ")
xpath2 = input("enter checkhout xpath: ")


#were using shitty linux so thats for linux
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#grabs the link / url
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.bestbuy.com/site/searchpage.jsp?st=" + grablink)

#clicks the elemnt wich is the ad to cart button 
send = driver.find_element_by_xpath(xpath1)
send.click()


#checkout options
buy = driver.find_element_by_xpath(xpath2)
buy.click()




