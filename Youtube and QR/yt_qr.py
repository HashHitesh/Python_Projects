import urllib.request
import re
import pyqrcode 
from pyqrcode import QRCode 

search_keyword = input("Enter the title of the video:\n")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)

video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
#print(video_ids) All the video ids for the video

temp = "https://www.youtube.com/watch?v=" + video_ids[0]
#print("https://www.youtube.com/watch?v=" + video_ids[0])

print(temp)

url = pyqrcode.create(temp)
url.svg("QR.svg", scale = 10) 
