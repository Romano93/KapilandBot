from selenium import webdriver
import time

userName = ""
password = ""
world = "6"

baseUrl = "s6.kapilands.eu/"

browser = webdriver.Firefox(executable_path=r"C:\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
# Login
browser.get('http://kapiland.de/')
browser.execute_script("anaml()")
# Welt
welt = browser.find_element_by_name('server')
for option in welt.find_elements_by_tag_name('option'):
    if option.text == 'Welt6':
        option.click()
        break
# User
browser.find_element_by_name('USR').send_keys(userName)
#Password
browser.find_element_by_name('pass').send_keys(password)
# submit
browser.find_element_by_class_name('send').click()
# goto facility-tree
browser.find_element_by_id("href_stadt").click()
# markt merken
lager = browser.find_element_by_id("href_lager").get_attribute("href")
# goto produktionsgebaeude
browser.find_element_by_id("href_prod").click()
# elektrizitaetswerke
elWerke = browser.find_elements_by_xpath("//a[starts-with(@href, 'main.php?page=roh&art=43')]") # nur kraftwerke
# Links speichern
links = []
resetLinks = []
for eWerk in elWerke:
    if eWerk.text != "bereit":
        resetLinks.append(eWerk.get_attribute("href"))
    links.append(eWerk.get_attribute("href"))
for reslink in resetLinks:
    browser.get(reslink)
    browser.find_element_by_id('A_PRODUKTION_ABBRECHEN').click()
# alle links aufrufen und aktion ausführen
for link in links:
    browser.get(link)
    browser.find_element_by_id('produkt_0').click()
    browser.execute_script("document.getElementById('TABLE_PRODUKT_PRODUZIEREN_MYPRODUCTTABLE_TRID_91').style.display='';") # disbaled for some reasons
    browser.implicitly_wait(1)
    dauer = browser.find_element_by_id('dauer_91').get_attribute('value')
    browser.find_element_by_name('a_bestellen[]').send_keys(str((80 * 60 * 60)/float(dauer)))
    browser.find_element_by_class_name('send').click()
browser.get(lager)