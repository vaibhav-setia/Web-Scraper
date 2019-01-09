import random
import urllib.request

def download_web_image(url):
	name = random.randrange(1,1000)
	full_name = str(name) + ".png"
	urllib.request.urlretrieve(url,full_name)
	
download_web_image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")