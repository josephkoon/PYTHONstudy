import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)

    for post_text in soup.findAll('a',{'class':'button-blue button-md book hidden-xs'})
        content = post_text.string
        print content


start(https://www.flipkey.com/gatlinburg-cabin-rentals/g60842/?page=2)