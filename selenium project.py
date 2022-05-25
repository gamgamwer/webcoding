import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

#csv 만들기
f = open('코스타그램.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['이미지 주소', '내용', '해시테그', '좋아요 수', '댓글 수'])

#드라이버 가져오기&접속
s = Service('/Users/gamga/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get("https://workey.codeit.kr/costagram/index")
time.sleep(1)

#로그인
driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')
driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()
time.sleep(1)

#스크롤 끝까지
last_height = 0

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#이모지 제거
cleantext = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#썸네일 클릭
for post in driver.find_elements(By.CSS_SELECTOR, '.post'):
    post.click()
    time.sleep(0.5)
    #이미지 주소
    style = driver.find_element(By.CSS_SELECTOR, '.post-container__image').get_attribute('style')
    imageurl = style.split(sep='"')[1]
    #해시태그
    hashtag = ""
    for tag in driver.find_elements(By.CSS_SELECTOR, '.content__tag'):
        hashtag += tag.text
    #나머지 값
    text = driver.find_element(By.CSS_SELECTOR, '.content__text').text
    content = cleantext.sub(r'', text)
    like = driver.find_element(By.CSS_SELECTOR, '.content__like-count').text
    comment = driver.find_element(By.CSS_SELECTOR, '.content__comment-count').text
    #csv 입력
    writer.writerow([imageurl, content, hashtag, like, comment])
    #창닫기
    driver.find_element(By.CSS_SELECTOR, '.close-btn').click()
    time.sleep(0.5)

#드라이버 종료
driver.quit()
