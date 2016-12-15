#python 3 only
import random
import urllib.request

def download_web_image(url):
	name = random.randrange(1,1000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url, full_name)
	
download_web_image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Culinary_fruits_front_view.jpg")
