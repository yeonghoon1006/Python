import os
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlsxwriter

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://finance.daum.net/domestic/influential_investors')

time.sleep(2)

soup = BeautifulSoup(browser.page_source, "html.parser")
#print(soup.prettify())

workbook = xlsxwriter.Workbook("mini_project3(외국인 및 기관 거래 RANK 20).xlsx")


### 순 매수 ###
worksheet = workbook.add_worksheet('순매수')
ins_cnt = 1

for i in range(1,21):
    company = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[1]/a'.format(i))
    price = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[2]/span'.format(i))
    count = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[3]/span'.format(i))
    updown = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[4]/span'.format(i))

    #print(company[0].text + " | " + price[0].text + " | " + count[0].text + " | " + updown[0].text)
    worksheet.write('A%s' % ins_cnt, company[0].text)
    worksheet.write('B%s' % ins_cnt, price[0].text)
    worksheet.write('C%s' % ins_cnt, count[0].text)
    worksheet.write('D%s' % ins_cnt, updown[0].text)

    ins_cnt+=1
### 순 매도 ###
worksheet2 = workbook.add_worksheet('순매도')
ins_cnt2 = 1
for i in range(1,21):
    company = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[5]/a'.format(i))
    price = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[6]/span'.format(i))
    count = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[7]/span'.format(i))
    updown = browser.find_elements_by_xpath('//*[@id="boxInfluentialInvestors"]/div[2]/div[1]/table/tbody/tr[{}]/td[8]/span'.format(i))

    #print(company[0].text + " | " + price[0].text + " | " + count[0].text + " | " + updown[0].text)
    worksheet2.write('A%s' % ins_cnt2, company[0].text)
    worksheet2.write('B%s' % ins_cnt2, price[0].text)
    worksheet2.write('C%s' % ins_cnt2, count[0].text)
    worksheet2.write('D%s' % ins_cnt2, updown[0].text)

    ins_cnt2+=1
browser.quit()

workbook.close()