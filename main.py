import time
import telegram
from selenium import webdriver

driver = webdriver.Chrome('chromedriver경로')

url = 'naver.com'
driver.get(url)
id = '~~'
pw = '~~'

driver.find_element_by_xpath("//input[@id='userid']").send_keys(id)
driver.find_element_by_xpath("//input[@id='userpass']").send_keys(pw)
driver.find_element_by_xpath("//button[@id='login_btn']").click()

while True:
    time.sleep(1)
    driver.refresh()
    time.sleep(2)
    for i in range(3):
        notReadEmail = driver.find_elements_by_xpath("//a[@style='font-weight: bold;']")
        print(driver.find_elements_by_xpath("//a[@style='font-weight: bold;']"))
        for title in notReadEmail:
            print(title.text)
            bot = telegram.Bot(token='~~~~')
            bot.send_message(chat_id=~~~~, text="`"+title.text)
