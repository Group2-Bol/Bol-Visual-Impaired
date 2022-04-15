import time
from selenium import webdriver
import os
from urllib import request

PATH = "C:\\Users\\guido\\Desktop\\Informatica\\Project D\\webscraper\\chromedriver.exe"
imagesStorage = "Image Storage"
imageId = 0

def createImageStorage():
    if not os.path.exists(imagesStorage):
        os.mkdir(imagesStorage)
    
def acceptCookies():
    try:
        cookieButton = driver.find_element_by_xpath('//*[@id="modalWindow"]/div[2]/div[2]/wsp-consent-modal/div[2]/button[1]')
        cookieButton.click()
    except:
        print("Hij pakt hem niet!")

def getMenus():
    subMenus = (driver.find_element_by_xpath('//*[@id="mainContent"]/div/div')).find_elements_by_tag_name('a')
    linksToSubMenus = []

    for menu in subMenus:
        menuText = menu.get_attribute("innerHTML") 
        if "Alles" in menuText or "Sieraden" in menuText:
            pass
        else:
            linksToSubMenus.append(menu.get_attribute('href'))
    
    navigateWebsite(linksToSubMenus)

def navigateWebsite(linksToSubMenus):
    for link in linksToSubMenus:
        driver.get(link)
        findImages()
    driver.close()
        
def findImages():
    time.sleep(2)
    try:
        content = driver.find_element_by_id("mainContent")

        foundImages = content.find_elements_by_tag_name("img")
        downloadImages(foundImages)
    except:
        print("Woops, er gaat iets mis!")

def downloadImages(foundImages):
    for j,i in enumerate(foundImages):
        global imageId
        if j < hoeveelheidImages:
            src = i.get_attribute("src")
            try:
                if src != None:
                    src = str(src)
                    print('Ik heb een source!')

                    request.urlretrieve(src, os.path.join(imagesStorage, f"kleding{imageId}.jpg"))
                    imageId += 1
                else:
                    raise TypeError
            except Exception as e:
                print("Woopsie!")


hoeveelheidImages = int(input("Hoeveel afbeeldingen wil je per pagina hebben? "))
createImageStorage()
   
driver = webdriver.Chrome(PATH)
driver.get(f"https://www.bol.com/nl/nl/menu/categories/subMenu/7")
driver.implicitly_wait(10)
acceptCookies()
getMenus()


  

