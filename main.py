import csv
import requests
from bs4 import BeautifulSoup

csv_file = open('SBS_데이터.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(5):
            url = 'https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}'.format(year, month, weekIndex)
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')

            for tag in soup.select('tr')[1:]:
                if tag.select_one('td.channel').get_text() == 'SBS':
                    period = '{}년 {}월 {}주차'.format(year, month, weekIndex)
                    row = [
                        period,
                        tag.select_one('td.rank').get_text(),
                        tag.select_one('td.program').get_text(),
                        tag.select_one('td.percent').get_text()]
                    csv_writer.writerow(row)

csv_file.close()