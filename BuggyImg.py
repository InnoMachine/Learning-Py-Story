__author__ = 'puppy'

#src="http://imgsrc.baidu.com/forumxxxxxxxxxx.jpg" pic_ext="jpeg"

import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.*?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x += 1
html = getHtml("http://tieba.baidu.com/p/2979214653")
print getImg(html)
