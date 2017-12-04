# tools

## slideshare.py
* git clone https://github.com/enguru/tools.git ile indirebilirsiniz
* Indirmek istediğiniz slideshare dökümanı kaynak da belirlemelisiniz
```python 
sayfa = requests.get('https://www.slideshare.net/secret/<BURAYA LINKI YAPISTIR>')
```

#### Not
```lxml``` ve ```requests``` modulari kurmak icin şu komutlar gerekli: ```pit install lxml``` ve ```pit install requests```.

#### TODOs
* PDF function ekle
* Daha fazla link birden işle
