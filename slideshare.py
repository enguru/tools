from lxml import html
import requests

sayfa = requests.get('https://www.slideshare.net/secret/<BURAYA LINKI YAPISTIR>')
agac = html.fromstring(sayfa.content)
urls = agac.xpath('//img[@data-full]/@data-full')
c = 1
for url in urls:
    print(url)
    veri = requests.get(url).content
    with open('sayfa'+str(c)+'.jpg', 'wb') as handler:
        handler.write(veri)
    c = c + 1   # c++
