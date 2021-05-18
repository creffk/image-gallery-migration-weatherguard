from bs4 import BeautifulSoup as BSHTML
import urllib3

http = urllib3.PoolManager()
url = 'https://www.rooferees.com/gallery/'

response = http.request('GET', url)
soup = BSHTML(response.data, "html.parser")
images = soup.findAll('img')

for image in images:
    #print image source
    print(image['src'])
