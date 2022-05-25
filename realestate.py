import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#csv 만들기
f = open('종촌동.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['단지명', '유형', '매매', '전세', '월세', '확인날짜'])

#드라이버 가져오기&접속
s = Service('/Users/gamga/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get("https://land.naver.com/")
time.sleep(1)

#검색어 입력, 단지목록 열기
driver.find_element(By.ID, 'queryInputHeader').send_keys('종촌동')
driver.find_element(By.CSS_SELECTOR, 'a.search_button').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.type_complex').click()

#단지정보 얻기
for complex in driver.find_elements(By.CSS_SELECTOR, '.complex_item_inner'):
    title = complex.find_element(By.CSS_SELECTOR, '.complex_title').text
    type = complex.find_element(By.CSS_SELECTOR, '.sale_type').text
    sale = complex.find_elements(By.CSS_SELECTOR, '.quantity')[0].text
    totalrent = complex.find_elements(By.CSS_SELECTOR, '.quantity')[1].text
    monthrent = complex.find_elements(By.CSS_SELECTOR, '.quantity')[2].text
    writer.writerow([title, type, sale, totalrent, monthrent, ])

f.close()
driver.close()

