import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#드라이버 가져오기&접속
s = Service('/Users/gamga/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get("https://new.land.naver.com/complexes/104343?ms=36.5022829,127.2534747,16&a=APT&e=RETAIL&ad=true")
time.sleep(1)

#csv 만들기
f = open('가재9단지.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['아파트', '동', '매매유형', '가격', '면적', '층수', '방향', '확인날짜'])