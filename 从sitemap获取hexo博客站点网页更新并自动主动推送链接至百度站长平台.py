import requests
import time
import  datetime
import dateutil.parser
from bs4 import BeautifulSoup as bp

def get_(data):
    headers={'User-Agent':'curl/7.12.1 ',
             'Content-Type':'text/plain '}
    try:
        r = requests.post(url='你的百度主动推送地址',data=data)
        print(r.status_code)
        print(r.content)
    except Exception.e:
        print(e)

print('自动推送开启....','utf-8')
time.sleep(0.5)

site_url = '你的sitemap.xml地址'

try:
    print('获取sitemap链接....','utf-8')
    data_ = bp(requests.get(site_url).content,'lxml')
except Exception.e:
    print(e)

list_url=[]
list_date=[]

print('---------------------------------')
for x,y in enumerate(data_.find_all('loc')):
    print(x,y.string)
    list_url.append(y.string)

for x2,y2 in enumerate(data_.find_all('lastmod')):
    startTime=y2.string
    startTime=dateutil.parser.parse(startTime)
    date1=(startTime.isoformat())[0:10]
    startTime=date1+" "+(startTime.isoformat())[11:19]
    startTime=datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
    now=datetime.datetime.utcnow()
    endTime = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    date2=(endTime.isoformat())[0:10]
    date = endTime- startTime
    seconds=date.seconds
    if date1==date2 and seconds<600:#可修改，推送sitemap时间距现在600秒以内的网页链接
        list_date.append(x2)

print('---------------------------------')
print(list_date)
print('开始推送....','utf-8')

for x in list_date:
    cjhurl=list_url[x]
    print('当前推送条目为:','utf-8' + cjhurl)
    get_(cjhurl)
