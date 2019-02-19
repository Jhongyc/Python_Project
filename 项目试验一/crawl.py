# Author:GaoYuCai
from bs4 import  BeautifulSoup
import  requests
import  csv
url = "http://bj.58.com/pinpaigongyu/pn/{page}/"
csv_file=open("rent.csv",'w')
csv_writer=csv.writer(csv_file,delimiter=',')

while True:
    page +=1
    print('')

